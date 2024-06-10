let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let T = Number(input[0]);

for(let i = 1; i <= T; i++) {
  // R, S 받아오기
  let R = input[i].split(' ')[0];
  let S = input[i].split(' ')[1];
  let answer = '';
  for(let j = 0; j <S.length; j++){
    let cnt = 0;
    while(cnt < R){
      answer += S[j]
      cnt += 1;
    }
  }
  console.log(answer);
}
