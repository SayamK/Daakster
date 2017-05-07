var textrank = require('textrank-node');
var summarizer = new textrank();
var output = summarizer.summarize('some document here', 4);

console.log(output);