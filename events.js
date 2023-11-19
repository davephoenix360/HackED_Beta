const { spawn } = require('child_process');
const { text } = require('stream/consumers');
require("isomorphic-fetch");
let items = [];

const pythonScript = 'events.py';

const scriptArgs = ['Arts'];

const pythonProcess = spawn('python', [pythonScript, ...scriptArgs]);

// Initialize 'descrip' variable
let descrip = '';

// Listen for stdout data from the Python process
pythonProcess.stdout.on('data', (data) => {
    let myArr = (data.toString()).split("-"); // Convert data to string and store it in 'descrip'
    let text = "";
    let count = 0;
    for (let index of myArr) {
        if (count % 2 == 0) {
            text += index;
        } 
        else
        {
            text += ' <a href="' + index + '"><br>';
        }
        count++;
    }
    console.log(text)

});