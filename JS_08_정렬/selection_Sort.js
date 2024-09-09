function selectionSort(arr){
  for(let i = 0; i < arr.length; i++){
    let minIndex = i; // 가장 작은 원소의 인덱스 확인
    for(let j = minIndex; j < arr.length; j++){
      if(arr[minIndex] > arr[j]){
        minIndex = j;
      }
    }
    // Swap i의 값과 minindex의 값과 교체
      let temp = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
  }
}