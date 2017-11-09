let opensearch = require('opensearch-browser');

//opensearch.config({ useXHR: true, });

module.exports = {
    searchDocumentation: function(searchTerm) {
        opensearch.discover('http://devdocs.io/').then((service) => {
            var mimeType = null;
            var raw = true;
            service.search({
                searchTerms: searchTerm,
                startIndex: 1
            }, mimeType, raw).then((results) => {
                console.log(results);
            });
        });
    }
};
