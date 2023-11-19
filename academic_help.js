const { spawn } = require('child_process');
require("isomorphic-fetch");
let items = [];

const pythonScript = 'course_info.py';

const scriptArgs = ['MATH 209'];

const pythonProcess = spawn('python', [pythonScript, ...scriptArgs]);

// Initialize 'descrip' variable
let descrip = '';

// Listen for stdout data from the Python process
pythonProcess.stdout.on('data', (data) => {
    descrip = data.toString(); // Convert data to string and store it in 'descrip'
    var googleBooks = require('google-books-search');
    googleBooks.search(descrip, function(error, results) {
        if ( ! error ) {
            console.log(results);
        } else {
            console.log(error);
        }
    });
    
});


/* // Listen for the Python process to exit
pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
}); */

