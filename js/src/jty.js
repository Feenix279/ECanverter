//JSON TO YDGW

const { pgnToYdgwRawFormat } = require('@canboat/canboatjs');
const readline = require('readline');


//actual decoding            
function jsontoydgw(line) {
    //ydgw->json->n2k
    const json = JSON.parse(line)
    const ydgw = pgnToYdgwRawFormat(json)
    return ydgw;
}
//creates interface
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

//reads from stdin and iterates through lines
rl.on('line', (line) => {
    //Ignore empty lines
    if (!line.trim()) return;

    try {
        //console.log("Data read : " + line.toString());

        //convert and write back to stdout
        const decoded = jsontoydgw(line);        
        process.stdout.write(decoded + "\n");
        
    } catch (err) {
        // Erorrmessages
        process.stdout.write("Error with decoding\n");
    }
});
