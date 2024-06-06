let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let number = Number(input);
let number_a = Number(input[0]);

let sum = 0;

for(let i = 1; i <= number; i++){
  sum += i
}
console.log(sum);

console.log(number_a, number);