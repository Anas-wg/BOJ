fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split(' ').map(Number);


//  시계수 뽑기
function getClockNumber(numList){
  let numStr = numList.join('');

  let rotations = [
    numStr, // 0123
    numStr.slice(1) + numStr[0],        // 1230
    numStr.slice(2) + numStr.slice(0, 2), // 2301
    numStr.slice(3) + numStr.slice(0, 3)  // 3012
  ];
  return Math.min(...rotations.map(Number));
}


// 모든 시계수 중 입력 카드의 시계수가 몇번째로 작은가


function solve(targetNumList) {
  let targetSmallestRotation = getClockNumber(targetNumList);
  
  let uniqueNumbers = new Set();

  for (let i = 1111; i <= 9999; i++) {
      let digits = i.toString().split('').map(Number);
      
      if (digits.includes(0)) continue;
      
      let smallestRotation = getClockNumber(digits);

      uniqueNumbers.add(smallestRotation);
  }

  let sortedUniqueNumbers = Array.from(uniqueNumbers).sort((a, b) => a - b);
  
  return sortedUniqueNumbers.indexOf(targetSmallestRotation) + 1; // 인덱스이므로 +1
}

let result = solve(input);
console.log(result);