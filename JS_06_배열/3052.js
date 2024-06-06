let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let arr = input.map(x => Number(x))
let answerSet = new Set();

for (let i = 0; i < arr.length; i++) {
  answerSet.add(arr[i] % 42);
}

console.log(answerSet.size);