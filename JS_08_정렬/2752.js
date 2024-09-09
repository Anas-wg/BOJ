let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split(' ');
console.log(input);
let arr= input.map(x => Number(x));
arr.sort((a,b) => a - b)
console.log(...arr)