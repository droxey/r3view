

var editor = ace.edit("editor");
editor.setOptions({
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
editor.session.setMode('ace/mode/javascript');


