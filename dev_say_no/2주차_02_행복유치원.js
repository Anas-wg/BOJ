const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let [N, K] = input[0].split(' ').map(Number);
let students = input[1].split(' ').map(Number);

// 키 차이를 고르는 방향
let gaps = [];

for(let i = 1; i < students.length; i++){
  gaps.push(students[i] - students[i - 1]);
}

gaps.sort((a, b) => a- b);


if(K == 1) {
  console.log(gaps.reduce((a, b) => a + b, 0));
} else {
  console.log(gaps.slice(0, -(K - 1)).reduce((a, b) => a + b, 0));
}