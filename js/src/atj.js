//ANYTHINGs TO JSON

const { FromPgn } = require('@canboat/canboatjs');
const readline = require('readline');

// Create parser instance
const parser = new FromPgn()

// Handle warnings
parser.on('warning', (pgn, warning) => {;
  //console.log(`[WARNING] PGN ${pgn.pgn}: ${warning}`)
})


//actual decoding            
function anytojson(line) {
    //ydgw->json->n2k
    const json = parser.parseString(line);
    const convd = JSON.stringify(json)
    return convd;
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
        const decoded = anytojson(line);        
        process.stdout.write(decoded + "\n");
        
    } catch (err) {
        // Erorrmessages
        process.stdout.write("Error with decoding\n");
    }
});
