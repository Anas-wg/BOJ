let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let arr = input.map(x => Number(x));


// 최댓값
let maxVal = arr.reduce((a, b) => Math.max(a, b));
console.log(maxVal);

// 순서
for (let i = 0; i < arr.length; i++){
  if(arr[i] == maxVal){
    console.log(i+1);
  }
}