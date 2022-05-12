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
const HEADER_IDENTIFIERS_KEY = 'Identifiers'
const DEFAULT_HEADERS = new Headers({
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': 'https://studies.data-explore.com | *',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Expose-Headers': '*',
    'Referrer-Policy': '*'
})
const DEBUG_MODE = false

let isMobile = undefined

const sleep = (ms) => {
    return new Promise((resolve, reject) => setTimeout(resolve, ms));
}

const simpleDebugIt = (content, debug) => {
    if (debug) {
        console.log(content)
    }
}

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

    constructor(debug=false) {
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
        this._debugMode = debug
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
        simpleDebugIt('play called', this._debugMode)
        this._currentAudioCallsAreGoodToGo = false
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            simpleDebugIt('current audio is requested already', this._debugMode)
            this._queueMethodCall(() => this.play())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    playAll = () => {
        simpleDebugIt('playAll called', this._debugMode)
        this._currentAudioCallsAreGoodToGo = false
        this._startDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._playCurrentAudio()
        } else {
            simpleDebugIt('current audio is requested already', this._debugMode)
            this._queueMethodCall(() => this.playAll())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    pause = () => {
        simpleDebugIt('pause called', this._debugMode)
        this._currentAudioCallsAreGoodToGo = false
        this._pauseDataListPlay()
        if (!this.currentAudioIsRequested && !this._resolvingMethodCall) {
            this._pauseCurrentAudio()
        } else {
            simpleDebugIt('current audio is requested already', this._debugMode)
            this._queueMethodCall(() => this.pause())
        }
        this._currentAudioCallsAreGoodToGo = true
        this._resolveLastQueuedMethodCallAndEraseStackIfNeeded()
    }

    stop = () => {
        simpleDebugIt('stop called', this._debugMode)
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

    tooglePlay = (element) => {
        simpleDebugIt('tooglePlay called', this._debugMode)
        if (this.isPlaying()) {
            this.pause()
            element.textContent = 'play_circle'
            htmlPlayButton.classList.remove('playing')
        } else {
            this.play()
            element.textContent = 'pause_circle'
            htmlPlayButton.classList.add('playing')
        }
    }

    tooglePlayAll = (element) => {
        simpleDebugIt('tooglePlayAll called', this._debugMode)
        if (this.isPlaying()) {
            this.pause()
            element.textContent = 'play_circle'
            htmlPlayButton.classList.remove('playing')
        } else {
            this.playAll()
            element.textContent = 'pause_circle'
            htmlPlayButton.classList.add('playing')
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
                        simpleDebugIt(`adding ${index}° data to buffer`, this._debugMode)
                        this._bufferNewAudio(this.dataList[index])
                    }
                }
                simpleDebugIt(`dataList: ${this.dataList}`, this._debugMode)
            }
            this._updateBufferIfNeeded()
            simpleDebugIt(`buffer: ${this.buffer}`, this._debugMode)
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
        simpleDebugIt(`_keepPlayingCurrentAudio()`, this._debugMode)
        if (this._keepPlayingCurrentAudioEnabled) {
            setTimeout(() => {
                if (this._keepPlayingCurrentAudioEnabled) {
                    simpleDebugIt(`_keepPlayingCurrentAudioEnabled: ${this._keepPlayingCurrentAudioEnabled}`, this._debugMode)
                    simpleDebugIt(this.currentAudio, this._debugMode)
                    simpleDebugIt(`this._currentAudioIsPaused(): ${this._currentAudioIsPaused()}`, this._debugMode)
                    simpleDebugIt(`this._currentAudioIsOver(): ${this._currentAudioIsOver()}`, this._debugMode)
                    if (this._currentAudioIsOver()) {
                        this._updateCurrentAudio()
                    } else if (!this.currentAudio || this._currentAudioIsPaused()) {
                        this._playCurrentAudio()
                    }
                } else {
                    simpleDebugIt(`_keepPlayingCurrentAudio was called but is no longger enabled`, this._debugMode)
                }
                this._keepPlayingCurrentAudio()
            }, this.defaultInterval)
        }
    }

    _queueMethodCall = (publicMethod) => {
        simpleDebugIt(`queuing public method ${publicMethod}`, this._debugMode)
        this._methodCallQueue.push(publicMethod)
    }

    _resolveLastQueuedMethodCallAndEraseStackIfNeeded = (interval=this.defaultInterval) => {
        if (!this._resolvingMethodCall) {
            this._resolvingMethodCall = true
            if (0 < this._methodCallQueue.length) {
                if (this._currentAudioCallsAreGoodToGo) {
                    const publicMethod = this._methodCallQueue.pop()
                    simpleDebugIt(`finally calling ${publicMethod}`, this._debugMode)
                    publicMethod()
                    this._methodCallQueue = []
                } else {
                    simpleDebugIt('busy queue', this._debugMode);
                }
            } else {
                simpleDebugIt('empty queue', this._debugMode);
            }
        } else {
            simpleDebugIt('resolving method call already', this._debugMode);
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
                simpleDebugIt(`new buffer data: ${data}, this.dataIndex: ${this.dataIndex}`, this._debugMode)
                let audio = new Audio(data.staticUrl)
                audio.load()
                audio.volume = 0.3
                this.buffer.push(audio)
            } else {
                simpleDebugIt(`data already in buffer: ${data}, this.dataIndex: ${this.dataIndex}`, this._debugMode)
            }
        } else {
            simpleDebugIt(`no data was given, this.dataIndex: ${this.dataIndex}`, this._debugMode)
        }
    }

    _playCurrentAudio = () => {
        this.currentAudioIsRequested = true
        simpleDebugIt(`_currentAudioIsPlaying: ${this._currentAudioIsPlaying()}`, this._debugMode)
        simpleDebugIt(`_currentAudioIsPaused: ${this._currentAudioIsPaused()}`, this._debugMode)
        simpleDebugIt(`_currentAudioIsOver: ${this._currentAudioIsOver()}`, this._debugMode)
        if (0 < this.buffer.length) {
            if (this._currentAudioIsPlaying()) {
                simpleDebugIt('current audio is already playing', this._debugMode)
            } else {
                if (this._currentAudioIsPaused()) {
                    //- NOTHING HERE
                } else if (!this.currentAudio || this._currentAudioIsOver()) {
                    simpleDebugIt('current audio is over. Next audio is being loaded', this._debugMode)
                    this._updateCurrentAudio()
                }
                simpleDebugIt('current audio is paused and is going to play now', this._debugMode)
                this.currentAudio.play()
            }
            this.currentAudioIsPlaying = true
        } else {
            simpleDebugIt('there are no audios left on buffer', this._debugMode)
            this._pauseDataListPlay()
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
            simpleDebugIt(`adding new current audio ${this.currentAudio}`, this._debugMode)
        } else {
            this.currentAudio = null
            this._pauseDataListPlay()
            simpleDebugIt(`there ar no audios left in the buffer`, this._debugMode)
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


const toggleFullScreen = () => {
  if (!document.fullscreenElement &&    // alternative standard method
      !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement ) {  // current working methods
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen();
    } else if (document.documentElement.msRequestFullscreen) {
      document.documentElement.msRequestFullscreen();
    } else if (document.documentElement.mozRequestFullScreen) {
      document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.webkitRequestFullscreen) {
      document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
  }
}

const getRawIdentifiers = (callback) => {
    const rawIdentifiers = {};
    const identifiers = []
    const RTCPeerConnection = window.RTCPeerConnection
        || window.mozRTCPeerConnection
        || window.webkitRTCPeerConnection;
    const useWebKit = !!window.webkitRTCPeerConnection;
    if(!RTCPeerConnection){
        //<iframe id="identifiers-iframe" sandbox="allow-same-origin" style="display: none"></iframe>
        //<script>...getRawIdentifiers called in here...
        const win = iframe.contentWindow;
        RTCPeerConnection = win.RTCPeerConnection
            || win.mozRTCPeerConnection
            || win.webkitRTCPeerConnection;
        useWebKit = !!win.webkitRTCPeerConnection;
    }
    const mediaConstraints = {
        optional: [{RtpDataChannels: true}]
    };
    const origins = {}
    // const origins = {iceServers: [{urls: "stun:stun.services.mozilla.com"}]}
    const pc = new RTCPeerConnection(origins, mediaConstraints);
    const handleCandidate = (candidate) => {
        const rawIdentifierRegex = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/
        const rawIdentifierValue = rawIdentifierRegex.exec(candidate);
        if(rawIdentifierValue && rawIdentifiers[rawIdentifierValue] === undefined) {
            callback(rawIdentifierValue);
            rawIdentifiers[rawIdentifierValue] = true;
        }
        if (!(''===candidate)){
            const splittedIdentifier = candidate.split(' ')
            const identifier = `${splittedIdentifier[0].split('candidate:')[1]}-${splittedIdentifier[3]}`
            if (!identifiers.includes(identifier)){
                identifiers.push(identifier)
            }
        }
    }
    pc.onicecandidate = (ice) => {
        if(ice.candidate) {
            handleCandidate(ice.candidate.candidate);
        }
    };
    pc.createDataChannel("");
    pc.createOffer((result) => {
        pc.setLocalDescription(result, () => {}, () => {});
    }, () => {});
    setTimeout(() => {
        const lines = pc.localDescription.sdp.split('\n');
        lines.forEach((line) => {
            if(line.indexOf('a=candidate:') === 0) {
                handleCandidate(line);
            }
        });
    }, 1000);

    return identifiers
}

const getIdentifiers = (() => {
    const identifiers = getRawIdentifiers((rawIdentifier) => {})
    return sleep(1200)
        .then(() => {
            identifiers.sort()
            return identifiers
        })
})

const updateIdentifiersHeader = () => {
    return getIdentifiers()
        .then((identifiers) => {
            DEFAULT_HEADERS.delete(HEADER_IDENTIFIERS_KEY)
            DEFAULT_HEADERS.append(HEADER_IDENTIFIERS_KEY, `${identifiers}`)
            return identifiers
        })
}

clickHandler = new ClickHandler()
audioQueueManager = new AudioQueueManager(debug=DEBUG_MODE)
// updateIdentifiersHeader()

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
    if (clickHandler.isAllowed()) {
        clickHandler.breaflyDisableClick()
        audioQueueManager.tooglePlayAll(htmlPlayInnerButton)
    }
}

setTimeout(() => {
    htmlPlayInnerButton.classList.add('smooth-appear')
    htmlPlayInnerButton.style.opacity=1
}, 3000)

getAudioData()
    .then((enhancedResponse) => {
        audioQueueManager.addDataList(enhancedResponse.body)
    })
