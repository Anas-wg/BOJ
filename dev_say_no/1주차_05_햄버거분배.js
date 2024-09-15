fs = require('fs');
let input = fs.readFileSync("input.txt").toString().split('\n')

let N = Number(input[0].split(' ')[0]);
let K = Number(input[0].split(' ')[1]);

let array = input[1].split('')

let answer = 0;

for(let i = 0; i < N; i++){
  if(array[i] === 'P'){
    for(let j = i - K; j < i + K + 1; j++){
      if(j >= 0 && array[j] === 'H'){
        array[j] = 'X';
        answer += 1;
        break;
      }
    }
  }
}

console.log(answer);