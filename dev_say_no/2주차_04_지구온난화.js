const { mkdirSync } = require('fs');

fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

// 입력받기
let [R, C] = input[0].split(' ').map(Number);
let map = [];
for (let i = 1; i <= R; i++) {
  map.push(input[i].split(''));
}


// dx, dy 4방향
const [row, col] = [R, C];
const [dx, dy] = [
  [-1, 1 , 0, 0],
  [0, 0, -1, 1]
];

// 바다 탐색
function search_sea(x, y){
  let sea_count = 0;
  for(let i = 0; i< 4; i++){
    let nx = x + dx[i];
    let ny = y + dy[i];    
    if (nx < 0 || nx >= row || ny < 0 || ny >= col) {
      sea_count++
    } else if(map[nx][ny] == '.') {
      sea_count++
    };
  }
  return sea_count;
}

// 잠긴 부분의 좌표 저장
let sink = [];

for(let i = 0; i < R; i++){
  for(let j = 0; j < C ; j++){
    if(map[i][j] == 'X'){
      if(search_sea(i, j) >= 3){
        sink.push([i, j]);
      }
    }
  }
}

// 잠긴부분 바다로 만들기
for (let [x, y] of sink) {
  map[x][y] = '.';
}

// 출력범위 구하기
let minX = R
let maxX = 0
let minY = C
let maxY = 0

for(let i = 0; i < R; i++){
  for(let j = 0; j < C; j++){
    if(map[i][j] == 'X'){
      minX = Math.min(minX,i); // 가장 작은 row idx
      maxX = Math.max(maxX,i); // 가장 큰 row idx
      minY = Math.min(minY,j);
      maxY = Math.max(maxY,j);
    }
  }
}

// 출력

for (let i = minX; i <= maxX; i++) {  // row 반복
  let row = '';
  for (let j = minY; j <= maxY; j++) {  // 각 row의 col 반복
    row += map[i][j];
  }
  console.log(row); 
}

