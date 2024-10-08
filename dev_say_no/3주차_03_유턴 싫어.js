fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

// 입력 받기
let [R, C] = input[0].split(' ').map(Number);

