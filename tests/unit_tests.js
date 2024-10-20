const{add, sub ,mul, div} = require('./javascript_example');

describe('Unit tests', () => {

    it ('should add two numbers', () => {
        expect(add(1,2)).toBe(3);
    });

    it ('should subtract two numbers', () => {
        expect(sub(2,1)).toBe(1);
    });

    it ('should multiply two numbers', () => {
        expect(mul(2,3)).toBe(6);
    });

    it ('should divide two numbers', () => {
        expect(div(6,3)).toBe(2);
    });


});