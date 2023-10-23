// var http = require('http');
// var fs = require('fs');
// var app = http.createServer(
//     function(requrest, response) {
//         var url = requrest.url;

//         if (url == '/') {
//             url = '/index.html';
//         }
//         if (url == '/favicon.ico') {
//             return response.writeHead(404);
//         }
//         response.writeHead(200);

//         fs.readFile('sample.txt', 'utf8', function(err, data) {
//             console.log(data);
//         });
//         response.end(fs.readFileSync(__dirname + url));
//         console.log(url);
//     }
// );
// app.listen(3000);

var http = require('http');
var fs = require('fs');
var url = require('url');
const path = require('path');
var app = http.createServer(function(request, response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname =  url.parse(_url, true).pathname;
    var title =  queryData.id;

    if(pathname === '/' || pathname === '/index.html')
    {
      if(title === undefined)
      {
        fs.readdir("./data", function(error, filelist){

        title = "Welcome";
        var description = "Hello, dimigo!";
        var list = "<ol>";
        var i = 0;
        while(i < filelist.length) {
          list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
          i++;
        }
        list = list+"</ol>";

        var template = `<!doctype html>
        <html>
        <head>
          <title>WEB1 - HTML </title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="index.html">WEB</a></h1>
          ${list}
          <h2>${title}</h2>
          <p>${description}</p>
        </body>
        </html>
        `;
        response.writeHead(200);
        response.end(template);
        });
      }
      else
      {
        fs.readFile(`data/${queryData.id}`, 'utf8', function(err, description){
        var template = `<!doctype html>
        <html>
        <head>
          <title>WEB1 - HTML </title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="index.html">WEB</a></h1>
          <ol>
            <li><a href="/?id=HTML">HTML</a></li>
            <li><a href="/?id=CSS">CSS</a></li>
            <li><a href="/?id=Javascript">JavaScript</a></li>
          </ol>
          <h2>${title}</h2>
          <p>${description}</p>
        </body>
        </html>
        `;
        response.writeHead(200);
        response.end(template);
      });
    }
  }
  else{
    response.writeHead(404);
    response.end('Page Not Found');
  }
});
app.listen(3000);
