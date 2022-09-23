var fs = require('fs');
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function executeCode(code) {
  var result = eval(code);
  console.log(result);
}

rl.question('Enter some code: ', function(code) {
  executeCode(code);
  rl.close();
});
