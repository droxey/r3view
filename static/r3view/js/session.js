class CodeSession {
  constructor(accessToken, websocketUrl, userData) {
    this.userData = userData;
    this.websocketUrl = websocketUrl;
    this.token = accessToken;
    this.channel = this.userData.channel;
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
        enableLiveAutocompletion: false,
        readOnly: false
    });
    codeEditor.session.setMode('ace/mode/javascript');
    return codeEditor;
  }

  initSocket() {
    let socket = new SockJS(this.websocketUrl);
    let chatUL = $('#chat-ul');
    let chatForm = $('#chat-form');

    function objectifyForm(formArray) {
      var returnArray = {};
      for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
      }
      return returnArray;
    };

    chatForm.on('submit', function(e) {
      e.preventDefault();
      var data = objectifyForm(chatForm.serializeArray());
      data.datetime = moment().calendar();
      sendChatMessage(data);
      chatForm.find('[name="comment"]').val('');
    });

    let sendChatMessage = function(data) {
      buildChatUI(data);
      return JSON.stringify({
          "channel": self.channel,
          "data": data,
          "event": "CHAT_MESSAGE",
          "token": self.accessToken
      });
    };

    let buildChatUI = function(data) {
      var template =
        `<li class="animated slideInDown">
          <small class="pull-right">${data.datetime}</small>
          <h4 class="sender">${data.username}</h4>
          <small>${data.comment}</small>
        </li>`;

        chatUL.prepend($(template));
    };

    let tinyChatbot = function() {
      let chatbotCopy = [
        'Welcome to r3view! Wondering how it works? Paste some JavaScript code in the editor!',
        'Not too shabby, right? It gets better. The link in your browser? You can share it with friends and collegues anytime you want to talk about code!',
        'Anyone who has the secret link can join in on the live discussion, or leave a message you can look back on later.',
        'Why not give it a try now? :)',
      ];

      var counter = 0;
      let intervalId = setInterval(sendBotMessage, 4000);

      function sendBotMessage() {
        if (counter >= chatbotCopy.length - 1) {
          clearInterval(intervalId);
        }

        socket.send(sendChatMessage({
          'username': 'system',
          'comment': chatbotCopy[counter],
          'datetime': moment().calendar()
        }));

        counter++;
      };
    }

    socket.onopen = function(e) {
      console.log('[info] Client WebSocket connection established.');
    };

    socket.onmessage = function(data) {
      let initialized = false;
      if (!initialized) {
        initialized = true;
        tinyChatbot();
      }
      else {
        buildChatUI(data);
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
