fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

let [C, R] = input[0].split(' ').map(Number);
let K = Number(input[1]);

let concert_hall = Array.from(Array(R), () => Array(C).fill(0));

const [dx, dy] = [[-1, 0, 1, 0], [0, 1, 0, -1]]; // 북, 동, 남, 서 순서
let currentValue = 1;
let x = R - 1, y = 0; 
let direction = 0; 

let result = -1;

if (K > C * R) {
  result = 0; 
} else {
  while (currentValue <= C * R) {
    concert_hall[x][y] = currentValue;

    if (currentValue === K) {
      result = `${y + 1} ${R - x}`; 
      break;
    }

    currentValue++;

    let nx = x + dx[direction];
    let ny = y + dy[direction];

    if (nx < 0 || nx >= R || ny < 0 || ny >= C || concert_hall[nx][ny] !== 0) {
      direction = (direction + 1) % 4; 
      nx = x + dx[direction];
      ny = y + dy[direction];
    }

    x = nx;
    y = ny;
  }
}

console.log(result);
