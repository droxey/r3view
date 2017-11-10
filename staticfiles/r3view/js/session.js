class CodeSession {
  constructor(accessToken, websocketUrl) {
    this.websocketUrl = websocketUrl;
    this.token = accessToken;
    this.socket = this.initSocket();
    this.editor = this.initEditor();
    this.docViewer = this.initDocs();
    this.eventTypes = {
        SelectRepo: 'USER_SELECT_REPO'
    };
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

    socket.onopen = function(e) {
        console.log('[info] Client WebSocket connection established.')
        console.log(e);

        var send = {
            channel: 'channel',
            message: 'message'
          };

          socket.send(JSON.stringify(send));
        // TODO: Send data to server with the access_token for github,
        // if the logged in user owns this repository
    };

    socket.onmessage = function(received) {
        console.log(JSON.parse(JSON.stringify(received.data)));
      //  console.log('[info] Client received data:', JSON.parse(JSON.stringify(received.data)));

    };

    return socket;
  }

  initDocs() {
    var devDocs = jQuery('#devdocs');
    devDocs.css({ 'zoom': '150%', 'width': '100%', 'height': '266px'});
    return devDocs;
  }
}
