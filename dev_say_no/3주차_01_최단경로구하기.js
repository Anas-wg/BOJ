fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n');

// 도시(노드)개수
let N = Number(input[0]);
let M = Number(input[1]);

console.log(input);
let edges = [];

for (let i = 2 ; i < M + 2; i++) {
  let info = input[i].split(' ').map(Number);
  edges.push(info);
}

let A = input[M+2].split(' ').map(Number)[0];
let B = input[M+2].split(' ').map(Number)[1];



class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(element, priority) {
    this.queue.push({ element, priority });
    this.sort();
  }

  dequeue() {
    return this.queue.shift();
  }

  sort() {
    this.queue.sort((a, b) => a.priority - b.priority);
  }

  isEmpty() {
    return this.queue.length === 0;
  }
}


const graph = Array.from({ length: N + 1 }, () => []);


for (let i = 0; i < M; i++) {
  const [x, y, cost] = edges[i];
  graph[x].push([y, cost]);
}

const INF = 1e9;
const distance = Array(N + 1).fill(INF);

function dijkstra(start) {
  const pq = new PriorityQueue();
  pq.enqueue(start, 0);
  distance[start] = 0;

  while (!pq.isEmpty()) {
    const { element: now, priority: dist } = pq.dequeue();

    if (distance[now] < dist) continue;

    for (let i = 0; i < graph[now].length; i++) {
      const [next_node, weight] = graph[now][i];
      const cost = dist + weight;

      if (cost < distance[next_node]) {
        distance[next_node] = cost;
        pq.enqueue(next_node, cost);
      }
    }
  }
}

dijkstra(A);

console.log(distance[B]);
