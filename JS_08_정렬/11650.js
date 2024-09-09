let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let N = Number(input[0]);
let arr = []; 
// x좌표 순 정렬
// x좌표 동일하면 y 좌표 순서로 진행

for (let i = 1; i <= N; i++){
  arr.push(input[i].split(' ').map(Number))
}

arr.sort(function(a, b){
  if(a[0] != b[0]) return a[0] - b[0];
  else return a[1] - b [1]
})

for (item of arr){
  console.log(...item);
}