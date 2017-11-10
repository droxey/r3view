class CodeSession {
  constructor(accessToken, websocketUrl) {
    this.websocketUrl = websocketUrl;
    this.token = accessToken;
    this.channel = 'asdf';
    this.socket = this.initSocket();
    this.editor = this.initEditor();
    this.docViewer = this.initDocs();
    this.eventTypes = {
        GH_USER_GET_REPOS: 'GH_USER_GET_REPOS',
        GH_USER_SELECT_REPO: 'GH_USER_SELECT_REPO',
        GH_USER_SELECT_FILE: 'GH_USER_SELECT_FILE',
        GH_RENDER_REPO_TREE: 'GH_RENDER_REPO_TREE',

        CHAT_SEND_MESSAGE: 'SEND_CHAT_MESSAGE',
        CHAT_RECEIVED_MESSAGE: 'CHAT_RECEIVED_MESSAGE',
        CHAT_LOAD_STREAM: 'CHAT_LOAD_STREAM',
    };
  }

  buildMessage(event, data={}) {
    return JSON.stringify({
        channel: this.channel,
        data: data,
        event: event,
        token: this.accessToken
    });
  }

  initEditor() {
    let codeEditor = ace.edit(editor);
    codeEditor.setOptions({
        selectionStyle: 'line',
        highlightActiveLine: true,
        fadeFoldWidgets: true,
        showFoldWidgets: true,
        showGutter: true,
        tabSize: 4,
        displayIndentGuides: true,
        showPrintMargin: false,
        fixedWidthGutter: true,
        animatedScroll: true,
        theme: 'ace/theme/tomorrow',
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: false,
        readOnly: true
    });
    codeEditor.session.setMode('ace/mode/javascript');
    return codeEditor;
  }

  initSocket() {
    let socket = new SockJS(this.websocketUrl);

    socket.onopen = function(e) {
        console.log('[info] Client WebSocket connection established.')
        console.log(e);

        var initChatMessage = this.buildMessage(this.eventTypes.CHAT_LOAD_STREAM, {});
        socket.send(initChatMessage);
    };

    socket.onmessage = function(received) {
        var message = JSON.parse(JSON.stringify(received.data));
        console.log('[info] Client received data:', message);

        switch(message.event) {
            case 'GH_USER_GET_REPOS':
            break;
            case 'GH_USER_SELECT_REPO':
            break;
            case 'GH_USER_SELECT_FILE':
            break;
            case 'GH_RENDER_REPO_TREE':
            break;
            case 'CHAT_SEND_MESSAGE':
            break;
            case 'CHAT_RECEIVED_MESSAGE':
            break;
            case 'CHAT_LOAD_STREAM':
            break;
            default:
                console.log('Unkown event type:', message.event);
                break;
        }
    };

    return socket;
  }

  initDocs() {
    var devDocs = jQuery('#devdocs');
    devDocs.css({ 'zoom': '150%', 'width': '100%', 'height': '266px'});
    return devDocs;
  }
}
