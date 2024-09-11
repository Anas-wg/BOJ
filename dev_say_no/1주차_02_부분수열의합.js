let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n').map((el) => el.split(" ").map(Number));


// 수열 이루는 숫자 개수
let N = input[0][0];
//  수열의 원소를 다 더한 값(목표)
let S = input[0][1];
//  수열
let sequence = input[1];
//  경우의 수 count
let count = 0;



// 배열 에서 합이 되는 숫자를 고르는 것 -> 조합?
function getCombinations (arr, selectNumber){
  const result = [];
  if(selectNumber === 1) return arr.map((el) => [el])
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combinations = getCombinations(rest, selectNumber -1);
    const attached = combinations.map((el) => [fixed, ...el]);
    result.push(...attached);
  });
  return result;
  }

// 조합으로 나온 결과의 배열의 원소의 합이 S와 동일하면 count ++
for(let i = 1; i <= N; i++) {
  let part_sequence = getCombinations(sequence, i);
  part_sequence.forEach((seq) => {
    const sum = seq.reduce((prev, curr) => prev + curr, 0);
    if(sum === S) count++;
  })

}

console.log(count);