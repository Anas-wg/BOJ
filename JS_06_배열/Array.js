// 2차원 리스트 초기화
// ES6 이상에서 활용 가능
let arr = Array.from(Array(4), () => new Array(5))
console.log(arr);

// 반복문을 통한 2차원 배열(3 X 4) 초기화
let arr2 = new Array(3);
for (let i = 0; i < arr2.length; i++) {
  arr2[i] = Array.from(
    { length: 4 },
    (undefined, j) => i * 4 + j
  );
}
console.log(arr2);

// push : 배열 가장 뒤 원소 추가
let arr = [5, 6, 7, 8, 9];
arr.length = 8;
arr[7] = 3;
arr.push(1);
for (let x of arr) {
  console.log(x);
}

// concat : 여러개의 배열 이어 붙이기
let arr1 = [1, 2, 3, 4, 5];
let arr2 = [6, 7, 8, 9, 10];
let arr = arr1.concat(arr2, [11, 12], [13]);
console.log(arr);

// slice : 특정 구간의 원소를 꺼낸 배열을 반환
let arr = [1, 2, 3, 4, 5];
let result = arr.slice(2, 4); // [3, 4]
console.log(result);

// indexOf(): 특정한 값을 갖는 원소의 "첫번째" 인덱스를 반환
let arr = [7, 3, 5, 6, 6, 2, 1];
console.log(arr.indexOf(5)); //2
console.log(arr.indexOf(6)); //3
console.log(arr.indexOf(8)); //-1 (JS에는 음수인덱스가 없음)


// 배열을 통한 Stack 구현
// push() -> 마지막 위치에 원소를 삽입
// pop() -> 마지막 위치에서 원소를 추출
let stack = [];
// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.push(5);
stack.push(2);
stack.push(3);
stack.push(7);
stack.pop();
stack.push(1);
stack.push(4);
stack.pop();
let reversed = stack.slice().reverse();
console.log(reversed); // 최상단 원소부터 출력
console.log(stack);


// 배열을 통한 Queue 구현
class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0;
    this.tailIndex = 0;
  }
  // 삽입
  enqueue(item) {
    this.items[this.tailIndex] = item; // 꼬리에 원소를 삽입
    this.tailIndex++; // 꼬리 인덱스 증가
  }
  // 추출 , 삭제
  dequeue() {
    const item = this.items[this.headIndex]; // 헤드의 원소
    delete this.items[this.headIndex]; // 아이템을 추출(메모리 할당 해제)
    this.headIndex++; // 헤드 인덱스 증가, 다음에 아이템 들어가도록
    return item;
  }
  peek() {
    return this.items[this.headIndex]; // 다음으로 꺼내고자 하는 원소 = 현재 헤드 원소
  }
  getLength() {
    return this.tailIndex - this.headIndex;
  }
}


queue = new Queue();
// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7)
// - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.enqueue(5);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(7);
queue.dequeue();''
queue.enqueue(1);
queue.enqueue(4);
queue.dequeue();

// 먼저 들어온 순서대로 출력
while (queue.getLength() != 0) {
  console.log(queue.dequeue());
}