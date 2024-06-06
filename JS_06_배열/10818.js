let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let N = Number(input[0]);
let str = input[1];
let arr = str.split(' ');


console.log(`${arr[0]} ${arr[N-1]}`);

