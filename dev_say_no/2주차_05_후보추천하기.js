const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let N = Number(input[0]); 
let R = Number(input[1]); 
let students = input[2].split(' ').map(Number); 

let picture = [];
let count = {}; 

for (let i = 0; i < students.length; i++) {
  let currentStudent = students[i];

  if (count[currentStudent]) {
    count[currentStudent]++;
  } else {
    if (picture.length === N) {
      let minStudent = picture[0];
      for (let j = 1; j < picture.length; j++) {
        if (count[picture[j]] < count[minStudent]) {
          minStudent = picture[j];
        }
      }
      picture = picture.filter(student => student !== minStudent);
      delete count[minStudent];
    }
    picture.push(currentStudent);
    count[currentStudent] = 1;
  }
}

console.log(...picture.sort((a, b) => a - b));
