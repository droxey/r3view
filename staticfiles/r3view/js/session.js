class CodeSession {
  constructor(accessToken, websocketUrl) {
    this.websocketUrl = websocketUrl;
    this.token = accessToken;
    this.socket = this.initSocket();
    this.editor = this.initEditor();
    this.docViewer = this.initDocs();
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
        enableLiveAutocompletion: false
    });
    codeEditor.session.setMode('ace/mode/javascript');
    return codeEditor;
  }

  initSocket() {
    let socket = new SockJS(this.websocketUrl);

    socket.connection = function() {
        console.log('[info] Client WebSocket connection established.')
        // TODO: Send data to server with the access_token for github,
        // if the logged in user owns this repository
    };

    socket.onmessage = function(msg) {
        console.log('[info] Client received data:', msg.data);
    };

    return socket;
  }

  initDocs() {
    var devDocs = jQuery('#devdocs');
    devDocs.css({ 'zoom': '120%', 'width': '100%', 'height': '285px', 'border-bottom': '1px solid #e4e7ea'});

    return devDocs;
  }

  sendDataToServer(channel, message) {
    // TODO: implement
  }
}
