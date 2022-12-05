let fs = require("fs");
const { join } = require("path");

fs.readFile("input/day5", "utf8", (err, data) => {
    const lines = data.trim().split('\n').map(i => i.trim());
    const stacks = [];
    let i;
    for (i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (/^\d+$/.test(line[0])) {
            line.split(' ').forEach(j => (j != '') && (stacks.push([])));

            for (let i2 = i - 1; i2 >= 0; i2--) {
                lines[i2].replaceAll('    ', ' ').split(' ').forEach((j, k) => (j != '') && (stacks[k].push(j.replace('[', '').replace(']', ''))));
            }
            break;
        }
    }

    const stacks2 = stacks.map(j => [...j]);
    // console.log(stacks);
    lines.slice(i + 2).forEach((line => {
        let [how_much, origin, dest] = line.split(' ').filter(j => /^\d+$/.test(j)).map(j => parseInt(j));
        [...Array(how_much)].forEach(_ => stacks[dest - 1].push(stacks[origin - 1].pop()));

        stacks2[dest - 1].push(...stacks2[origin - 1].slice(stacks2[origin - 1].length - how_much));
        stacks2[origin - 1] = stacks2[origin - 1].slice(0, stacks2[origin - 1].length - how_much);
    }));
    console.log('1) Last crates', stacks.map(j => j[j.length - 1]).join(''));
    console.log('2) Last crates', stacks2.map(j => j[j.length - 1]).join(''));
});
