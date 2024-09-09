let fs = require('fs');

let input = fs.readFileSync('input.txt').toString().trim().split('\n').map((el) => el.split(" ").map(Number));

let H = input[0][0]; // 종이의 높이
let W = input[0][1]; // 종이의 너비
let N = input[1][0]; // 스티커의 수

let paper_size = H * W; // 종이의 전체 면적
let stickers = input.slice(2); // 스티커 배열
let sizes = [];

for (let i = 0; i < stickers.length; i++) {
    for (let j = i + 1; j < stickers.length; j++) {
        let sticker1 = stickers[i];
        let sticker2 = stickers[j];

        // 첫 번째 경우: 스티커가 종이 안에 나란히 들어가는지 확인 (가로, 세로 그대로)
        if (
            (sticker1[0] + sticker2[0] <= H && Math.max(sticker1[1], sticker2[1]) <= W) || 
            (sticker1[0] + sticker2[0] <= W && Math.max(sticker1[1], sticker2[1]) <= H)
        ) {
            let sum = sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1];
            sizes.push(sum);
        }

        // 두 번째 경우: 스티커를 하나만 가로, 세로를 뒤집었을 때
        if (
            (sticker1[0] + sticker2[1] <= H && Math.max(sticker1[1], sticker2[0]) <= W) || 
            (sticker1[0] + sticker2[1] <= W && Math.max(sticker1[1], sticker2[0]) <= H)
        ) {
            let sum = sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1];
            sizes.push(sum);
        }

        // 세 번째 경우: 둘 다 뒤집어서 넣을 수 있는 경우
        if (
            (sticker1[1] + sticker2[0] <= H && Math.max(sticker1[0], sticker2[1]) <= W) || 
            (sticker1[1] + sticker2[0] <= W && Math.max(sticker1[0], sticker2[1]) <= H)
        ) {
            let sum = sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1];
            sizes.push(sum);
        }

        // 네 번째 경우: 둘 다 가로, 세로를 뒤집어서 넣는 경우
        if (
            (sticker1[1] + sticker2[1] <= H && Math.max(sticker1[0], sticker2[0]) <= W) || 
            (sticker1[1] + sticker2[1] <= W && Math.max(sticker1[0], sticker2[0]) <= H)
        ) {
            let sum = sticker1[0] * sticker1[1] + sticker2[0] * sticker2[1];
            sizes.push(sum);
        }
    }
}

if (sizes.length === 0) {
    console.log(0); 
} else {
    console.log(Math.max(...sizes));
}
