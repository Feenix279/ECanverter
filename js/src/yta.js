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

    //fills spaces in AIS Position reports to avoid unwanted additional characters
    if (json.pgn == 129794 || json.pgn == 129809 || json.pgn == 129810){
        //console.log("Position Report")
        const keys = ["name", "callsign", "destination"];
        const targetLength = [20,7,20];

        keys.forEach(key => {
          if (json.fields[key] !== undefined) {
            json.fields[key] = String(json.fields[key]).padEnd(targetLength[keys.indexOf(key)], " ");
          }
        });
    }
    
    //console.log(json)
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
