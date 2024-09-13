const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('Enter an odd number: ', (input) => {
    let n = parseInt(input, 10);
    let k = Math.floor(n / 2);
    if (n % 2 === 0) {
        console.log("This is an even number but here's the pattern for the next number:");
        n += 1;
        k = Math.floor(n / 2);
    }
    for (let i = 0; i <= k; i++) {
        let space = " ".repeat(k - i);
        let stars = "*".repeat((2 * i) + 1);
        console.log(space + stars);
    }
    for (let i = 0; i < k; i++) {
        let space = " ".repeat(i + 1);
        let stars = "*".repeat(n - 2 * (i + 1));
        console.log(space + stars);
    }
    rl.close();
});