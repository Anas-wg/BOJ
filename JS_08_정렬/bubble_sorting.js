function bubbleSort(arr) {
  // 뒤에서 출발
  // 마지막 원소는 위치가 정해져있음
  for (let i = arr.length - 1; i > 0; i--) {
    for (let j = 0; j < i; j++) {
      // Swap
      if (arr[j] < arr[j + 1]) { // 내림차순 예시
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}