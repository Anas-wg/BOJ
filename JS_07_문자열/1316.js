let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');
let N = Number(input[0]);
console.log(input);

let arr = [];
for (let i = 1; i <= N; i++){
  arr = [].push(input[i])
}
// 그룹 단어 = 각 문자가 연속해서 나타나는 경우
// 각 철자가 연속해서 등장한 횟수가 1번인지 체크
let alphabet = 'abcdefghijklmnopqrstuvwxyz'
let answer = 0;
for (let i = 0; i < N; i++) {
  let cnt = 0;
  if(arr in alphabet){
    cnt++;
  }
}