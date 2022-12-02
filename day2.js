const score_movement = [1, 2, 3]    // X:1, Y:2, Z:3
const win_lose = [0, 3, 6]          // Lose, Draw, Win
const what_should_I_do = [2, 0, 1]  // 2: Lose, 0: Draw, 1: Win

fs = require("fs");
fs.readFile("input/day2.sql", "utf8", (err, data) => {
    let total_part1 = 0;
    let total_part2 = 0;
    const listData = data.trim().split("\n");
    listData.forEach((element) => {
        let it = ["A", "X"];
        let [oponent, mine] = element
            .split(" ")
            .map((a, id) => a.charCodeAt(0) - it[id].charCodeAt(0));

        total_part1 += win_lose[(mine - oponent + 1 + 3) % 3] + score_movement[mine];
        total_part2 += win_lose[mine] + score_movement[(oponent + what_should_I_do[mine]) % 3];
    });
    console.log("1) Total points:", total_part1);
    console.log("2) Total points:", total_part2);
});
