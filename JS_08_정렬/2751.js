let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = Number(input[0]);
let arr = [];

for(let i = 1; i <= N; i++){
  arr.push(input[i])
}

arr.sort((a , b) => a - b);

// for(let i = 0; i < arr.length; i++){
//   console.log(arr[i]);
// }

answer = "";

for(let i = 0; i < arr.length; i++){
  answer += arr[i] + '\n';
}

console.log(answer);
