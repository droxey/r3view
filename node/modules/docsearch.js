XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest; // not required if we don't need XHR
let opensearch = require('opensearch-browser');

opensearch.config({ useXHR: true, }); // may not be nessessary

// schema located at: http://devdocs.io/opensearch.xml
module.exports = {
    searchDocumentation: function(searchTerm) {
        opensearch.discover('http://devdocs.io/#q=').then((service) => {
            var mimeType = 'text/html';
            var raw = true;
            service.search({
                searchTerms: searchTerm
            }, mimeType, raw).then((results) => {
                if (error) throw error;
                console.log(results);
            });
        });
    }
};
