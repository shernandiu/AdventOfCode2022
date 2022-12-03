let fs = require("fs");
let total;

const scores = {}
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach((i, j) => scores[i] = j + 1);

// console.log(scores);

fs.readFile("input/day3.sql", "utf8", (err, data) => {
    let lines = data.trim().split('\n').map(i => i.trim());
    // PART 1
    total = 0
    for (let line of lines) {
        const first_half = new Set(line.substring(0, Math.floor(line.length / 2)));
        const second_half = new Set(line.substring(Math.floor(line.length / 2)));
        const char = new Set([...first_half].filter((x) => second_half.has(x)));
        total += scores[char.keys().next().value];
    }
    console.log("1) Total score:", total);
    // PART 2
    total = 0

    for (let i = 0; i < lines.length; i += 3) {
        const frst = new Set(lines[i + 0]);
        const scnd = new Set(lines[i + 1]);
        const thrd = new Set(lines[i + 2]);
        const char = new Set([...frst].filter((x) => scnd.has(x) && thrd.has(x)));
        total += scores[char.keys().next().value];
    }
    console.log("2) Total score:", total);
});
