var http = require('http');
var fs = require('fs');
var url = require('url');
var app = http.createServer(function (request, response) {
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var title = queryData.id;
    console.log(url.parse(_url, true).pathname);
    fs.readFile(`data/${queryData.id}`, 'utf8', function (err, description) {
        var template = `<!doctype html>
<html> .. .. .. .. </html>`;
        response.writeHead(200);
        response.end(template);
    });
});
app.listen(3000);
