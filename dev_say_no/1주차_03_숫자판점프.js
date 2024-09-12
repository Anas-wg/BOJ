fs = require("fs");
let num_board = fs.readFileSync('input.txt').toString().trim().split('\n').map((el) => el.split(" ").map(Number));
let num_set = new Set();

const [row, col] = [num_board.length, num_board[0].length];
const [dx, dy] = [
  [-1, 1 , 0, 0],
  [0, 0, -1, 1]
];

// dfs
function dfs(x, y, current_num){
  if(current_num.length == 6){
    num_set.add(current_num);
    return;
  }
  for(let i = 0; i < 4; i++){
    let [nx, ny] = [x + dx[i], y + dy[i]];
    if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
    dfs(nx, ny, current_num + num_board[nx][ny]);
  }
}

// x, y를 반복문 활용, 모든 좌표서 시작하도록
for(let i = 0; i < row; i++){
  for(let j = 0;j < col; j++){
    dfs(i, j,num_board[i][j].toString());
  }
}

console.log(num_set.size);