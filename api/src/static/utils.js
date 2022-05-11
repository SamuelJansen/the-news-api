const htmlBody = document.querySelector('body')

const VOICE_API_BASE_URL = `${document.URL}`
const DEFAULT_REQUEST_TIMEOUT = 15000
const SMALL_TIMEOUT = DEFAULT_REQUEST_TIMEOUT / 5
const DEFAULT_AUDIO_TIMEOUT = 350
const DEFAULT_ANIMATION_TIMEOUT = 200
const DEFAULT_MESSAGE_TIME_DURATIONT = 5000
const HEADER_SESSION_KEY = 'Context'
const HEADER_IDENTIFIERS_KEY = 'Identifiers'
const DEFAULT_HEADERS = new Headers({
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': 'https://studies.data-explore.com | *',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Expose-Headers': '*',
    'Referrer-Policy': '*'
})

let isMobile = undefined

class ClickHandler {
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

    constructor() {
        this.currentAudioIsPlaying = false
        this.dataIndex = -1
        this.dataList = []
        this.currentAudio = null
        this.buffer = []
        this.maxBuffer = 10
        this.bufferUpdateInterval = 500
        this.defaultInterval = 600
        this._dataListPlayStarted = false
        this._currentAudioCallsAreGoodToGo = true
        this.currentAudioIsRequested = false
        this._keepPlayingCurrentAudioEnabled = false
        this._methodCallQueue = []
        this._resolvingMethodCall = false
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
        this._updateBufferIfNeeded()
    }

    addDataList = (dataList) => {
        if (dataList) {
            dataList.forEach((data, index) => {
                this.addData(data)
            });
        }
    }

    addData = (data) => {
        this.dataList.push(data)
    }

    play = () => {
        this._currentAudioCallsAreGoodToGo = false
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            console.log('current audio is requested already')
            this._queueMethodCall(() => this.play())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    playAll = () => {
        this._currentAudioCallsAreGoodToGo = false
        this._startDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            console.log('current audio is requested already')
            this._queueMethodCall(() => this.playAll())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    pause = () => {
        this._currentAudioCallsAreGoodToGo = false
        this._pauseDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._pauseCurrentAudio()
        } else {
            console.log('current audio is requested already')
            this._queueMethodCall(() => this.pause())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    stop = () => {
        this._currentAudioCallsAreGoodToGo = false
        this._pauseDataListPlay()
        this._pauseCurrentAudio()
        this.buffer = []
        this.dataIndex = -1
        this._pauseCurrentAudio()
        this._pauseDataListPlay()
        this.dataIndex = -1
        this.buffer = []
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    tooglePlay = () => {
        if (this.isPlaying()) {
            this.pause()
        } else {
            this.play()
        }
    }

    tooglePlayAll = () => {
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
            if ((0 < this.dataIndex || (0 > this.dataIndex && 0 < this.dataList.length)) && this.maxBuffer > this.buffer.length) {
                const desiredNextIndex = this.dataIndex + this.maxBuffer - this.buffer.length + 1
                const maxIndex = this.dataList.length - 1
                const fromIndex = this.dataIndex + 1
                const toIndex = maxIndex >= desiredNextIndex ? desiredNextIndex : maxIndex
                if (this.dataList.length >= fromIndex && fromIndex <= toIndex) {
                    for (let index=fromIndex; index<toIndex; index++) {
                        console.log(`adding ${index}° data to buffer`)
                        this._bufferNewAudio(this.dataList[index])
                    }
                }
                // console.log(`dataList: ${this.dataList}`)
            }
            this._updateBufferIfNeeded()
            // console.log(`buffer: ${this.buffer}`)
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
            this._dataListPlayStarted = false
            this._keepPlayingCurrentAudioEnabled = false
        }
    }

    _keepPlayingCurrentAudio = () => {
        // console.log(`this._keepPlayingCurrentAudio()`)
        if (this._keepPlayingCurrentAudioEnabled) {
            setTimeout(() => {
                // console.log(`this._keepPlayingCurrentAudioEnabled`)
                // console.log(this.currentAudio)
                // console.log(this._currentAudioIsPaused())
                // console.log(this._currentAudioIsOver())
                if (this._currentAudioIsOver()) {
                    this._updateCurrentAudio()
                } else if (!this.currentAudio || this._currentAudioIsPaused()) {
                    this._playCurrentAudio()
                }
                this._keepPlayingCurrentAudio()
            }, this.defaultInterval)
        }
    }

    _queueMethodCall = (publicMethod) => {
        console.log(`queuing public method ${publicMethod}`)
        this._methodCallQueue.push(publicMethod)
    }

    _resolveLastQueuedMethodCallAndEraseStackIfNeeded = (interval=this.defaultInterval) => {
        if (!this._resolvingMethodCall) {
            this._resolvingMethodCall = true
            if (0 < this._methodCallQueue.length) {
                if (this._currentAudioCallsAreGoodToGo) {
                    const publicMethod = this._methodCallQueue.pop()
                    console.log(`finally calling ${publicMethod}`)
                    publicMethod()
                    this._methodCallQueue = []
                } else {
                    console.log('busy queue');
                }
            } else {
                console.log('empty queue');
            }
        } else {
            console.log('resolving method call already');
        }
        this._resolvingMethodCall = false
        if (0 < this._methodCallQueue.length) {
            setTimeout(() => {
                this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
            }, interval)
        }
    }

    _bufferNewAudio = (data) => {
        if (data) {
            if (!this.buffer.map((d) => {d.key}).includes(data.key)) {
                this.dataIndex = this.dataIndex + 1
                console.log(`new buffer data: ${data}, this.dataIndex: ${this.dataIndex}`)
                let audio = new Audio(data.staticUrl)
                audio.load()
                audio.volume = 0.3
                this.buffer.push(audio)
            } else {
                console.log(`data already in buffer: ${data}, this.dataIndex: ${this.dataIndex}`)
            }
        } else {
            console.log(`no data was given, this.dataIndex: ${this.dataIndex}`)
        }
    }

    _playCurrentAudio = () => {
        this.currentAudioIsRequested = true
        console.log(`_currentAudioIsPlaying: ${this._currentAudioIsPlaying()}`)
        if (0 < this.buffer.length) {
            if (this._currentAudioIsPlaying()) {
                console.log('current audio is already playing')
            } else {
                if (this._currentAudioIsPaused()) {
                    console.log('current audio is paused and is going to play')
                } else if (!this.currentAudio || this._currentAudioIsOver()) {
                    console.log('current audio is over and is going to play')
                    this._updateCurrentAudio()
                }
                this.currentAudio.play()
            }
            this.currentAudioIsPlaying = true
        } else {
            console.log('there are no audios left on buffer')
            this.currentAudioIsPlaying = false
        }
        this.currentAudioIsRequested = false
    }

    _pauseCurrentAudio = () => {
        this.currentAudioIsRequested = true
        if (this.currentAudio) {
            this.currentAudio.pause()
            this.currentAudioIsPlaying = false
        }
        this.currentAudioIsRequested = false
    }

    _updateCurrentAudio = () => {
        this.currentAudioIsRequested = true
        if (this.currentAudio) {
            this.currentAudio.remove()
            delete this.currentAudio
            this.currentAudio = null
        }
        if (0 < this.buffer.length) {
            this.currentAudio = this.buffer.shift()
            console.log(`adding new current audio ${this.currentAudio}`)
        } else {
            this.currentAudio = null
            console.log(`there ar no audios left in the buffer`)
        }
        this.currentAudioIsPlaying = false
    }

    _currentAudioIsPlaying = () => {
        return this.currentAudio && !this._currentAudioIsPaused() && 0 <= this.currentAudio.currentTime && this.currentAudio.currentTime < this.currentAudio.duration
    }

    _currentAudioIsPaused = () => {
        return this.currentAudio && this.currentAudio.duration > 0 && 0 <= this.currentAudio.currentTime && this.currentAudio.currentTime < this.currentAudio.duration && this.currentAudio.paused
    }

    _currentAudioIsOver = () => {
        return this.currentAudio && !this._currentAudioIsPaused() && !this._currentAudioIsPlaying() && this.currentAudio.currentTime === this.currentAudio.duration
    }
}

clickHandler = new ClickHandler()
audioManager = new AudioQueueManager()

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
    return fetchWithTimeout(`${VOICE_API_BASE_URL}/the-news/today`,
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
    if (clickHandler.isAllowed()) {
        clickHandler.breaflyDisableClick()
        audioManager.tooglePlayAll()
    }
}

getAudioData()
    .then((enhancedResponse) => {
        audioManager.addDataList(enhancedResponse.body)
    })



// const buttonElement = document.createElement('button')
// buttonElement.addEventListener('click', () => handlePlayClick(buttonElement))
//
// htmlBody.append(buttonElement)
