const fs = require('fs');

// 1. Read input
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let K = parseInt(input[0].trim());
let arr = input[1].trim().split(' ');
let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

// Variables to store the min and max values
let minValue = null;
let maxValue = null;

// 2. Function to check if a permutation satisfies the inequality
function checkOk(numbers) {
  for (let i = 0; i < K; i++) {
    if (arr[i] === '<' && !(numbers[i] < numbers[i + 1])) {
      return false;
    }
    if (arr[i] === '>' && !(numbers[i] > numbers[i + 1])) {
      return false;
    }
  }
  return true;
}

// 3. Backtracking function to generate permutations on the fly
function generatePermutations(current, used) {
  if (current.length === K + 1) {
    if (checkOk(current)) {
      let numberStr = current.join('');
      
      // Check for min and max
      if (minValue === null || numberStr < minValue) {
        minValue = numberStr;
      }
      if (maxValue === null || numberStr > maxValue) {
        maxValue = numberStr;
      }
    }
    return;
  }

  // Recursively build permutations
  for (let i = 0; i < numbers.length; i++) {
    if (!used[i]) {
      used[i] = true;
      current.push(numbers[i]);
      generatePermutations(current, used);
      current.pop();
      used[i] = false;
    }
  }
}

// 4. Start the backtracking process
generatePermutations([], Array(numbers.length).fill(false));

// 5. Print the results
console.log(maxValue);
console.log(minValue);
