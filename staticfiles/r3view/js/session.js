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
        this.sendDataToServer('hi', 'hello');
    };

    socket.onmessage = function(data) {
        console.log('[info] Client received data:', data.message);
    };

    return socket;
  }

  initDocs() {
    var devDocs = jQuery('#devdocs');
    devDocs.css({ 'zoom': '150%', 'width': '100%', 'height': '266px'});

    return devDocs;
  }

  sendDataToServer(channel, message) {
      var send = {
        channel: channel,
        message: message
      };
      this.socket.send(JSON.stringify(send));
    }
}
