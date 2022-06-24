const { assert } = require('console');
const fs = require('fs');
const path = require('path');

console.log(path.resolve('./'));

// fs.readFile
var input = fs.readFileSync('./1/input.txt', 'utf8').split('\n')


function how_many_increases(input, offset=1){
    var counter = 0;
    for (let i = offset; i < input.length; i++) {
        if(parseInt(input[i]) > parseInt(input[i-offset])){
            counter +=1; 
        }
    }
    return counter
}

rslt1 = how_many_increases(input, 1)
rslt2 = how_many_increases(input, 3)

console.log(rslt1)
console.log(rslt2)



