let fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let number = Number(input)
let result = 1

for (let i = 0; i < number; i++) {
    result += i
}

console.log(result)