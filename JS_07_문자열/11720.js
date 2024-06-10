let fs  = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let N = Number(input[0]);
let sum = input[1].split('').map(Number).reduce((a ,b) => a + b);
console.log(sum);
