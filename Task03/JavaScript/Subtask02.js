const fs = require('fs');

fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading input file:', err);
    return;
  }

  fs.writeFile('output.txt', data, 'utf8', (err) => {
    if (err) {
      console.error('Error writing output file:', err);
    } else {
      console.log('Content successfully copied to output.txt');
    }
  });
});
