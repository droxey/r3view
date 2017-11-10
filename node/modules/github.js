const GitHub = require('github-api');


module.exports = function(socket, token) {
    let selectedRepo = {};

    var gh = new GitHub({
        token: token
    });

    var me = gh.getUser(); // no user specified defaults to the user for whom credentials were provided

    var userRepos;
    me.listRepos(function(err, repos) {
        repoList = repos;
    });

    var repo = gh.getRepo('droxey', 'instascraper');
    repo.getRef('heads/master', function(err, sha) {
        if (err) {
            throw err;
        }

        repo.getTree('master', function(err, tree) {
            socket.data({
                'channel': 'abcde',
                'data': JSON.parse(tree.tree),
                'event': 'GET_REPO_TREE'
            });
        });
    });
};
