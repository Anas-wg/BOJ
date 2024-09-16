fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\n');

// 입력받기
const [N, A, B] = input[0].split(' ').map(Number);
let square_2 = input[1].split(' ').map(Number);
let square_4 = input[2].split(' ').map(Number);

// 정렬
square_2.sort((a , b) => (b - a));
square_4.sort((a , b) => (b - a));

let answer = 0; 

// N이 홀수인 경우
// 무조건 2 * 1 하나가 들어가야함.
if(N % 2 != 0){
  answer += square_2[0];
  square_2.shift();
}

for(let i = 0; i <Math.floor(N / 2); i++){
  let case1 = 0;
  let case2 = 0;
// 2 * 1 짜리 두개
  if(square_2.length >= 2) {
    case1 = square_2[0] + square_2[1];
  }
// 2 * 2 짜리 하나
  if(square_4.length >= 1) {
    case2 = square_4[0]
  }

// 둘중 더 큰거
  if(case1 > case2) {
    answer += case1;
    square_2.shift();
    square_2.shift();
  } else {
    answer += case2;
    square_4.shift();
  }
}

console.log(answer);
