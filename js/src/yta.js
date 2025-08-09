//YDGW to ACTISENSE

const { FromPgn } = require('@canboat/canboatjs');
const { pgnToActisenseN2KAsciiFormat } = require('@canboat/canboatjs');
const readline = require('readline');

// Create parser instance
const parser = new FromPgn()

// Handle warnings
parser.on('warning', (pgn, warning) => {;
  //console.log(`[WARNING] PGN ${pgn.pgn}: ${warning}`)
})


//actual decoding            
function YDGWtoactisense(line) {
    //ydgw->json->n2k
    const json = parser.parseString(line);
    const acti = pgnToActisenseN2KAsciiFormat(json)
    return acti;
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
        const decoded = YDGWtoactisense(line);
        //console.log(decoded)        
        process.stdout.write(decoded + "\n");
        
    } catch (err) {
        // Erorrmessages
        process.stdout.write("\n");
    }
});
