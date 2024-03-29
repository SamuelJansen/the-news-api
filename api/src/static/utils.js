const htmlBody = document.querySelector('body')
const htmlPlayButton = document.querySelector('div.audio-circle')
const htmlPlayInnerButton = htmlPlayButton.querySelector('#spam-audio-circle')

const THE_NEWS_BASE_URL = `${document.URL}`
const THE_NEWS_CDN_BASE_URL = `${THE_NEWS_BASE_URL}`.replace('studies', 'cdn')
const THE_NEWS_API_BASE_URL = `${THE_NEWS_BASE_URL}`.replace('studies', 'api').replace('the-news', 'the-news-api')

const DEFAULT_REQUEST_TIMEOUT = 15000
const SMALL_TIMEOUT = DEFAULT_REQUEST_TIMEOUT / 5
const DEFAULT_AUDIO_TIMEOUT = 350
const DEFAULT_ANIMATION_TIMEOUT = 200
const DEFAULT_MESSAGE_TIME_DURATIONT = 5000
const HEADER_SESSION_KEY = 'Context'
const DEFAULT_HEADERS = new Headers({
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': 'https://studies.data-explore.com | *',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Expose-Headers': '*',
    'Referrer-Policy': '*'
})
const DEFAULT_DEBUG_MODE = false
const DEBUG_MODE = false

class SimpleDebugger {
    constructor(active=DEFAULT_DEBUG_MODE) {
        this.isActive = active
    }

    logIt = (content) => {
        if (this.isActive) {
            console.log(content)
        }
    }
}

const simpleDebugger = new SimpleDebugger(active=DEBUG_MODE)
const warningDebugger = new SimpleDebugger(active=DEBUG_MODE)
const errorDebugger = new SimpleDebugger(active=true)

let isMobile = undefined

const sleep = (ms) => {
    return new Promise((resolve, reject) => setTimeout(resolve, ms))
}

const setPlayButtonToPauseIconState = () => {
    simpleDebugger.logIt(`setPlayButtonToPauseIconState`)
    htmlPlayInnerButton.textContent = 'play_circle'
    htmlPlayButton.classList.remove('playing')
}

const setPlayButtonToPlayIconState = () => {
    simpleDebugger.logIt(`setPlayButtonToPlayIconState`)
    htmlPlayInnerButton.textContent = 'pause_circle'
    htmlPlayButton.classList.remove('playing')
    htmlPlayButton.classList.add('playing')
}

const setPlayButtonToStopIconState = () => {
    simpleDebugger.logIt(`setPlayButtonToStopIconState`)
    htmlPlayInnerButton.textContent = 'stop_circle'
    htmlPlayButton.classList.remove('playing')
}

const tooglePlayButtonIconState = (isPlayingNow) => {
    if (isPlayingNow) {
        setPlayButtonToPauseIconState()
    } else {
        setPlayButtonToPlayIconState()
    }
}

class ClickManager {
    constructor() {
        this.defaultTimeout = 500
        this.clickEnabled = true
    }

    breaflyDisableClick = () => {
        this.clickEnabled = false
        setTimeout(() => {
            this.clickEnabled = true
        }, this.defaultTimeout)
    }

    isAllowed = () => {
        return this.clickEnabled
    }
}

class AudioQueueManager {

    constructor(debug=false) {
        this.dataList = []
        this.bufferDataIndex = -1
        this.dataIndex = -1
        this.currentAudioIsPlaying = false
        this.currentAudio = null
        this.buffer = []
        this.maxBuffer = 10
        this.bufferUpdateInterval = 500
        this.defaultInterval = 600
        self.volume = 0.95
        this._dataListPlayStarted = false
        this._currentAudioCallsAreGoodToGo = true
        this.currentAudioIsRequested = false
        this._keepPlayingCurrentAudioEnabled = false
        this._methodCallQueue = []
        this._resolvingMethodCall = false
        this.internalDebugger = new SimpleDebugger(active=debug)
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
        this._updateBufferIfNeeded()
    }

    addDataList = (dataList) => {
        if (dataList) {
            dataList.forEach((data, index) => {
                this.addData(data)
            })
        }
    }

    addData = (data) => {
        this.dataList.push(data)
    }

    play = () => {
        if (!this._currentAudioCallsAreGoodToGo) {
            warningDebugger.logIt(`play: invalid call`)
        }
        this._currentAudioCallsAreGoodToGo = false
        this.internalDebugger.logIt('play called')
        setPlayButtonToPlayIconState()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            this.internalDebugger.logIt('current audio is requested already')
            this._queueMethodCall(() => this.play())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    playAll = () => {
        if (!this._currentAudioCallsAreGoodToGo) {
            warningDebugger.logIt(`playAll: invalid call`)
        }
        this._currentAudioCallsAreGoodToGo = false
        this.internalDebugger.logIt('playAll called')
        setPlayButtonToPlayIconState()
        this._startDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            this.internalDebugger.logIt('current audio is requested already')
            this._queueMethodCall(() => this.playAll())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    pause = () => {
        if (!this._currentAudioCallsAreGoodToGo) {
            warningDebugger.logIt(`pause: invalid call`)
        }
        this._currentAudioCallsAreGoodToGo = false
        this.internalDebugger.logIt('pause called')
        setPlayButtonToPauseIconState()
        this._pauseDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._pauseCurrentAudio()
        } else {
            this.internalDebugger.logIt('current audio is requested already')
            this._queueMethodCall(() => this.pause())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    stop = () => {
        if (!this._currentAudioCallsAreGoodToGo) {
            this.internalDebugger.logIt(`stop: emergency call`)
            setPlayButtonToStopIconState()
        } else {
            this._currentAudioCallsAreGoodToGo = false
            this.internalDebugger.logIt('stop called')
            setPlayButtonToPauseIconState()
        }
        this.buffer = []

        this._pauseDataListPlay()
        this._removeCurrentAudio()

        this.bufferDataIndex = -1
        this.dataIndex = -1
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    tooglePlay = () => {
        this.internalDebugger.logIt('tooglePlay called')
        if (this.isPlaying()) {
            this.pause()
        } else {
            this.play()
        }
    }

    tooglePlayAll = () => {
        this.internalDebugger.logIt('tooglePlayAll called')
        if (this.isPlaying()) {
            this.pause()
        } else {
            this.playAll()
        }
    }

    isPlaying = () => {
        this._currentAudioCallsAreGoodToGo = false
        const isTrue = this._currentAudioIsPlaying()
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
        return isTrue
    }

    isPaused = () => {
        this._currentAudioCallsAreGoodToGo = false
        const isTrue = this._currentAudioIsPaused()
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
        return isTrue
    }

    _updateBufferIfNeeded = () => {
        setTimeout(() => {
            if ((0 < this.bufferDataIndex || (0 > this.bufferDataIndex && this.bufferDataIndex < this.dataList.length)) && this.maxBuffer > this.buffer.length) {
                const maxIndex = this.dataList.length - 1
                const desiredFromIndex = this.dataIndex + this.buffer.length + 1
                const desiredToIndex = this.dataIndex + this.maxBuffer
                const fromIndex = desiredFromIndex > maxIndex ? maxIndex : desiredFromIndex
                const toIndex = desiredToIndex > maxIndex ? maxIndex : desiredToIndex
                this.internalDebugger.logIt(`buffer analisys: this.dataIndex: ${this.dataIndex}, order: ${this.dataList[this.dataIndex]?.order} -> this.bufferDataIndex: ${this.bufferDataIndex}, bufferOrder: ${this.dataList[this.bufferDataIndex]?.order}`)
                this.internalDebugger.logIt(`buffer analisys: fromIndex: ${fromIndex}, toIndex: ${toIndex}, desiredToIndex: ${desiredToIndex}, maxIndex: ${maxIndex}, this.buffer.length: ${this.buffer.length}`)
                if (this.dataList.length >= fromIndex && fromIndex <= toIndex) {
                    for (let index=fromIndex; index<=toIndex; index++) {
                        this.internalDebugger.logIt(`adding ${this.bufferDataIndex + 1}° data to buffer`)
                        this._bufferNewAudio()
                    }
                } else {
                    this.internalDebugger.logIt(`no extra audo data needed. fromIndex: ${fromIndex}, toIndex: ${toIndex}, desiredToIndex: ${desiredToIndex}`)
                }
                this.internalDebugger.logIt(`dataList: ${this.dataList}`)
            }
            this._updateBufferIfNeeded()
            this.internalDebugger.logIt(`buffer.length: ${this.buffer.length}`)
        }, this.bufferUpdateInterval)
    }

    _startDataListPlay = () => {
        if (!this._dataListPlayStarted) {
            this._dataListPlayStarted = true
            this._keepPlayingCurrentAudioEnabled = true
            this._keepPlayingCurrentAudio()
        }
    }

    _pauseDataListPlay = () => {
        if (this._dataListPlayStarted) {
            this._pauseCurrentAudio()
        }
        this._dataListPlayStarted = false
        this._keepPlayingCurrentAudioEnabled = false
    }

    _keepPlayingCurrentAudio = () => {
        this.internalDebugger.logIt(`_keepPlayingCurrentAudio()`)
        if (this._keepPlayingCurrentAudioEnabled) {
            setTimeout(() => {
                if (this._keepPlayingCurrentAudioEnabled) {
                    // this.internalDebugger.logIt(`_keepPlayingCurrentAudio._keepPlayingCurrentAudioEnabled: ${this._keepPlayingCurrentAudioEnabled}`)
                    // this.internalDebugger.logIt(`_keepPlayingCurrentAudio.this.currentAudio: ${this.currentAudio}`)
                    // this.internalDebugger.logIt(`_keepPlayingCurrentAudio._currentAudioIsPaused(): ${this._currentAudioIsPaused()}`)
                    // this.internalDebugger.logIt(`_keepPlayingCurrentAudio._currentAudioIsOver(): ${this._currentAudioIsOver()}`)
                    if (this._currentAudioIsOver()) {
                        this._updateCurrentAudio()
                    } else if (this._thereIsNoCurrentAudioAndThererAreAudiosAvailableAtBuffer() || this._currentAudioIsPaused()) {
                        this._playCurrentAudio()
                    }
                    if (this._thereIsCurrentAudio()) {
                        this._keepPlayingCurrentAudio()
                    }
                } else {
                    this.internalDebugger.logIt(`_keepPlayingCurrentAudio was called but is no longger enabled`)
                }
            }, this.defaultInterval)
        }
    }

    _playCurrentAudio = () => {
        this.currentAudioIsRequested = true
        // this.internalDebugger.logIt(`_playCurrentAudio._currentAudioIsPlaying(): ${this._currentAudioIsPlaying()}`)
        // this.internalDebugger.logIt(`_playCurrentAudio._currentAudioIsPaused(): ${this._currentAudioIsPaused()}`)
        // this.internalDebugger.logIt(`_playCurrentAudio._currentAudioIsOver(): ${this._currentAudioIsOver()}`)
        if (this._bufferHasAvailableAudios() || this._currentAudioIsPaused()) {
            if (this._currentAudioIsPlaying()) {
                this.currentAudioIsPlaying = true
                this.internalDebugger.logIt('current audio is already playing')
            } else {
                if (this._thereIsNoCurrentAudio() || this._currentAudioIsOver()) {
                    this.internalDebugger.logIt('current audio is over. Next audio is being loaded')
                    this._updateCurrentAudio()
                }
                if (this._thereIsCurrentAudio() && this._currentAudioIsPaused()) {
                    this.dataIndex = this.dataIndex + 1
                    this.internalDebugger.logIt(`current audio is paused and is going to play now. this.dataIndex: ${this.dataIndex}, order: ${this.dataList[this.dataIndex]?.order} -> this.bufferDataIndex: ${this.bufferDataIndex}, bufferOrder ${this.dataList[this.bufferDataIndex]?.order}`)
                    this.currentAudio.play()
                    this.currentAudio.didStartedToPlay = true
                    this.currentAudioIsPlaying = true
                } else if (!this._currentAudioIsPlaying()) {
                    this.currentAudioIsPlaying = false
                    this.internalDebugger.logIt(`audio.play() would be called, but no audio is present. audio: ${this.currentAudio}`)
                    this.stop()
                }
            }
        } else {
            this.internalDebugger.logIt('there are no audios left on buffer')
            this.stop()
            this.currentAudioIsPlaying = false
        }
        this.currentAudioIsRequested = false
    }

    _pauseCurrentAudio = () => {
        this.currentAudioIsRequested = true
        if (this._thereIsCurrentAudio()) {
            this.currentAudio.pause()
            this.currentAudioIsPlaying = false
        } else {
            this.currentAudioIsPlaying = false
            this.internalDebugger.logIt(`audio.pause() would be called, but no audio is present. audio: ${this.currentAudio}`)
        }
        this.currentAudioIsRequested = false
    }

    _removeCurrentAudio = () => {
        this._pauseCurrentAudio()
        if (this._thereIsCurrentAudio()) {
            // this.currentAudio.remove()
        }
        delete this.currentAudio
        this.currentAudio = null
    }

    _updateCurrentAudio = () => {
        this.currentAudioIsRequested = true
        if (this._bufferHasAvailableAudios()) {
            this.internalDebugger.logIt(`adding new current audio. dataIndex: ${this.dataIndex}°`)
            this._removeCurrentAudio()
            this.currentAudio = this.buffer.shift()
        } else {
            this.internalDebugger.logIt(`there ar no audios left in the buffer`)
            this.stop()
        }
        this.currentAudioIsPlaying = false
    }

    _queueMethodCall = (publicMethod) => {
        this.internalDebugger.logIt(`queuing public method ${publicMethod}`)
        this._methodCallQueue.push(publicMethod)
    }

    _resolveLastQueuedMethodCallAndEraseStackIfNeeded = (interval=this.defaultInterval) => {
        if (!this._resolvingMethodCall) {
            this._resolvingMethodCall = true
            if (0 < this._methodCallQueue.length) {
                if (this._currentAudioCallsAreGoodToGo) {
                    const publicMethod = this._methodCallQueue.pop()
                    this.internalDebugger.logIt(`finally calling ${publicMethod}`)
                    publicMethod()
                    this._methodCallQueue = []
                } else {
                    this.internalDebugger.logIt('busy queue')
                }
            } else {
                this.internalDebugger.logIt('empty queue')
            }
        } else {
            this.internalDebugger.logIt('resolving method call already')
        }
        this._resolvingMethodCall = false
        if (0 < this._methodCallQueue.length) {
            setTimeout(() => {
                this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
            }, interval)
        }
    }

    _bufferNewAudio =  () => {
        const desiredDataIndex = this.bufferDataIndex + 1
        if (this.dataList.length > desiredDataIndex && this.dataList[desiredDataIndex]) {
            const data = this.dataList[desiredDataIndex]
            if (!this.buffer.map((d) => {d.key}).includes(data.key)) {
                this.bufferDataIndex = this.bufferDataIndex + 1
                this.internalDebugger.logIt(`new buffer data: ${data}, this.dataIndex: ${this.dataIndex}, order: ${this.dataList[this.dataIndex]?.order} -> this.bufferDataIndex: ${this.bufferDataIndex}, bufferOrder ${data.order}`)
                // const audio = new Audio(data.staticUrl)
                const audio = new Howl({
                    src: [data.staticUrl],
                    format: 'mp3',
                    volume: self.volume
                })
                audio.didStartedToPlay = false
                audio.isOver = false
                audio.load()
                this.buffer.push(audio)
            } else {
                this.internalDebugger.logIt(`data already in buffer: ${data}, this.dataIndex: ${this.dataIndex}, order: ${this.dataList[this.dataIndex]?.order} -> this.bufferDataIndex: ${this.bufferDataIndex}, bufferOrder ${data.order}`)
            }
        } else {
            this.internalDebugger.logIt(`no data was given, this.bufferDataIndex: ${this.bufferDataIndex}`)
        }
    }

    _bufferHasAvailableAudios = () => {
        return  this.buffer && 0 < this.buffer.length
    }

    _thereIsCurrentAudio = () => {
        return this.currentAudio && true
    }

    _thereIsNoCurrentAudio = () => {
        return !this._thereIsCurrentAudio()
    }

    _thereIsNoCurrentAudioAndThererAreAudiosAvailableAtBuffer = () => {
        return !this._thereIsCurrentAudio() && this._bufferHasAvailableAudios()
    }

    _currentAudioIsPlaying = () => {
        this._updateCurrentAutioIsOverAttributeValue()
        return this._thereIsCurrentAudio() && this.currentAudio?.playing()
        // return this._thereIsCurrentAudio() && !this._currentAudioIsPaused() && 0 <= this.currentAudio.seek() && this.currentAudio.seek() < this.currentAudio.duration()
    }

    _currentAudioIsPaused = () => {
        this._updateCurrentAutioIsOverAttributeValue()
        return this._thereIsCurrentAudio() && !this._currentAudioIsPlaying()
        // return this._thereIsCurrentAudio() && 0 < this.currentAudio.duration() && 0 <= this.currentAudio.seek() && this.currentAudio.seek() < this.currentAudio.duration() && !this.currentAudio.playing()
    }

    _currentAudioIsOver = () => {
        this._updateCurrentAutioIsOverAttributeValue()
        return this._thereIsNoCurrentAudio() || this._currentAudioIsPaused() && this.currentAudio.isOver
        // console.log(this.currentAudio?.seek());
        // console.log(this.currentAudio?.duration());
        // console.log(this.currentAudio?._duration);
        // return this._thereIsCurrentAudio() && !this._currentAudioIsPaused() && !this._currentAudioIsPlaying() && false
    }

    _updateCurrentAutioIsOverAttributeValue = () => {
        if (this._thereIsCurrentAudio() && this.currentAudio.didStartedToPlay && this.currentAudio.seek() == 0) {
            this.currentAudio.isOver = true
        }
    }
}

const toggleFullScreen = () => {
  if (!document.fullscreenElement &&    // alternative standard method
      !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement ) {  // current working methods
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen()
    } else if (document.documentElement.msRequestFullscreen) {
      document.documentElement.msRequestFullscreen()
    } else if (document.documentElement.mozRequestFullScreen) {
      document.documentElement.mozRequestFullScreen()
    } else if (document.documentElement.webkitRequestFullscreen) {
      document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT)
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen()
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen()
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen()
    }
  }
}

const fetchWithTimeout = (url, options={}) => {
    const { timeout = DEFAULT_REQUEST_TIMEOUT } = options
    const { handler = null } = options
    return Promise.race([
        fetch(url, options),
        new Promise((resolve, reject) => setTimeout(() => reject(new Error('Request timeout')), timeout))
    ])
        .catch(error => {
            if (!handler) {
                throw error
            }
            handler()
        })
}

const getEnhancedResponse = (response) => {
    return ((r) => r.json())(response)
        .then(body => {
            return {
                response: response,
                status: response.status,
                body: body
            }
        })
        .then((enhancedResponse) => {
            isMobile = '?1' === response.headers.get('sec-ch-ua-mobile')
            return enhancedResponse
        })
        .then(enhancedResponse => {
            if (400 <= enhancedResponse.status) {
                throw new Error(`Server error: ${enhancedResponse.body.message}`)
            }
            return enhancedResponse
        })
}

const handleAuthenticationHeader = (response) => {
    // DEFAULT_HEADERS.delete(HEADER_SESSION_KEY)
    // DEFAULT_HEADERS.append(HEADER_SESSION_KEY, `Bearer ${enhancedResponse.context}`)
}

const getAudioData = () => {
    simpleDebugger.logIt(`getAudioData`)
    return fetchWithTimeout(`${THE_NEWS_API_BASE_URL}/the-news/today`,
        {
            method: 'GET',
            headers: DEFAULT_HEADERS
        }
    )
        .then(response => getEnhancedResponse(response))
        .then(enhancedResponse => {
            handleAuthenticationHeader(enhancedResponse)
            return enhancedResponse
        })
}

const handlePlayClick = () => {
    if (clickManager.isAllowed()) {
        clickManager.breaflyDisableClick()
        audioQueueManager.tooglePlayAll()
    }
}

setTimeout(() => {
    htmlPlayInnerButton.classList.add('smooth-appear')
    htmlPlayInnerButton.style.opacity=1
}, 3000)


clickManager = new ClickManager()
audioQueueManager = new AudioQueueManager(debug=DEFAULT_DEBUG_MODE)

getAudioData()
    .then((enhancedResponse) => {
        audioQueueManager.addDataList(enhancedResponse.body)
        return enhancedResponse.body
    })
