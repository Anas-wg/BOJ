let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

// 테스트 케이스
let T = Number(input[0]);
// N과 점수를 따로 받기
for(let i = 1; i <= T; i++){
  let arr = input[i].split(' ').map(Number);
  let N = arr.shift(arr[0]);
  // 평균 계산
  let total = 0
  for (let i = 0; i < arr.length; i++){
    total += arr[i];
  }
  let avg = total / arr.length
  // // 평균 넘는 학생들 비율 계산
  let count = 0;
  for(let i = 0; i < N; i++){
    if(arr[i] > avg){
      count ++;
    }
  } 
  let answer = (count / arr.length * 100).toFixed(3);
  console.log(`${answer}%`);
}




