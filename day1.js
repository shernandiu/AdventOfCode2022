fs = require("fs");
fs.readFile("input/day1.sql", "utf8", (err, data) => {
  let listData = data.split("\n\n");
  listData = listData.map((i) =>
    i.split("\n").reduce((a, b) => parseInt(a) + parseInt(b), 0)
  );
  listData.sort((a, b) => b - a);
  console.log("A) Max elf:", listData[0]);
  console.log(
    "B) Max elf:",
    listData.slice(0, 3).reduce((a, b) => a + b)
  );
});
