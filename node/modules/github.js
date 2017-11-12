const GitHub = require('github-api');


module.exports = function(socket, token, username, repo, branch) {
    var gh = new GitHub({ token: token });
    var repo = gh.getRepo(username, repo);
    var ref = 'heads/' + branch;
    
    repo.getRef(ref, function(err, sha) {
        if (err) { throw err; }
        repo.getTree(branch, function(err, tree) {
            socket.data({
                'channel': 'abcde',
                'data': JSON.parse(tree.tree),
                'event': 'GET_REPO_TREE'
            });
        });
    });
};
