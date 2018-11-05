const modelInterpreter = async (text, pythonFile) => {
    const spawn = require('child_process').spawn;
    const pythonProcess = spawn('python3', [pythonFile, text]);
    let result = [];
    await pythonProcess.stdout.on('data', (data) => {
      result.push(data.toString());
    });
    return result;
};

export { modelInterpreter };
