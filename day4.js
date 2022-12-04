let fs = require("fs");
fs.readFile("input/day4.sql", "utf8", (err, data) => {
    const lines = data.trim().split('\n').map(i => i.trim());

    let total1 = 0, total2 = 0;
    for (let line of lines) {
        const pairs = line.split(",").map(i => i.split('-').map(j => parseInt(j)));

        // Put the pair that starts before on the first place,
        // if they start at the same time, longest one first
        if (pairs[0][0] > pairs[1][0] || (pairs[0][0] == pairs[1][0] && pairs[1][1] > pairs[0][1]))
            [pairs[0], pairs[1]] = [pairs[1], pairs[0]];
        // If the second pair ends before the first one, it's being completely overlapsed
        if (pairs[1][1] <= pairs[0][1])
            total1 += 1;
        // If the second pair starts before the first one ends, it's being overlapsed
        if (pairs[0][1] >= pairs[1][0])
            total2 += 1;
    }
    console.log("1) Total:", total1);
    console.log("2) Total:", total2);
});
