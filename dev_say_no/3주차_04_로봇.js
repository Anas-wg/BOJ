const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  // 1. 문제의 Input을 받습니다.
  const [r, c] = input[0].split(' ').map(Number);
  const visited = Array.from(Array(r), () => Array(c).fill(false));

  let k = parseInt(input[1]);
  for (let i = 0; i < k; i++) {
    const [x, y] = input[i + 2].split(' ').map(Number);
    visited[x][y] = true;
  }

  let [x, y] = input[k + 2].split(' ').map(Number);
  visited[x][y] = true;
  let order = input[k + 3].split(' ').map(Number);

  // 2. index 활용을 위해 입력 받은 order 배열의 값을 조정합니다.
  for (let i = 0; i < order.length; i++) {
    order[i] -= 1;
  }

  let dir = 0;
  while (true) {
    let moved = false;
    for (let i = 0; i < 4; i++) {
      // 3. 현재방향 부터 4방향 탐색을 진행합니다.
      // 4. 탐색 중인 방향에 맞게 다음 위치를 지정합니다.
      const now_dir = (dir + i) % 4;
      const nx = x + dx[order[now_dir]];
      const ny = y + dy[order[now_dir]];
      // 5. 다음 위치가 방문가능한 곳인지 판단합니다.
      if (nx >= 0 && nx < r && ny >= 0 && ny < c && !visited[nx][ny]) {
        // 6. 방문 가능한 곳이라면 위치와 방향을 업데이트 합니다.
        x = nx;
        y = ny;
        dir = now_dir;
        visited[x][y] = true;
        // 7. 이동 가능했다는 표기를 합니다.
        moved = true;
        break;
      }
    }
    // 8. 이동하지 못했다면 탐색을 종료합니다.
    if (!moved) {
      break;
    }
  }
  console.log(x, y);
  process.exit();
});
