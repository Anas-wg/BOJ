let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

let N = Number(input[0]);
let arr = input[1].split(' ').map(Number);

// 최댓값 고르기
let maxval = arr.reduce((a, b) => Math.max(a, b));

// 점수 고치기 & 총합
let sum = 0
for(let i =0; i < arr.length; i++){
  arr[i] = arr[i] / maxval * 100
  sum += arr[i]
}

console.log(sum / N)

