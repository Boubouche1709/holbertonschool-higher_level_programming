#!/usr/bin/node
const x = process.argv.slice(2);
const number = parseInt(x);

if ((!isNaN(number)) && number > 0) {
    for (let index = 0; index < number; index++) {
        console.log('C is fun');
    }
} else if (!x) {
    console.log('Missing number of occurrences');
}
