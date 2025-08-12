Ecanverter can be used to load [CAN BUS](https://en.wikipedia.org/wiki/CAN_bus) data from the [ECAN-W01](https://www.cdebyte.com/products/ECAN-W01) into [OpenCPN](https://opencpn.org/).

# Manual
+ [Usage](##usage)
+ [Setup](##setup)

## Usage
1. Near instant translation from ECAN-W01 to OpenCPN
2. Broadcasts the NMEA2000 data to the whole network via UDP
3. Can be used for a JSON-dump of the whole traffic (or filtered) into a textfile
4. Currently working on the ability to controll Autopilots via any OpenCPN-pilot-plugin.
5. Includes some test-python-files that may be used for different things

## Setup

### Requirements:
+ [Node JS](https://nodejs.org/en) (check with ```node -v```)
+ Canboatjs library: 
```
cd js
npm install @canboat/canboatjs
```
### ECAN-W01 Setup
+ You need to configure the ECAN-W01 with the tool provided by [EBYTE](https://www.cdebyte.com/).
+ Make sure to set it to UDP-Server on whatever port you chose (I use port 8881, you can change it in the *config.ini*-file).
+ It's best to test the datastream. You can do that with any UDP-Client-Tool. You might have to send a message after connecting to activate the ECAN-W01.

### OpenCPN
+ Set an incoming UDP connection to another port (I use 8888) with the NMEA2000 Protocoll

### Start
You can use the .exe file *_main.py*
<sub>For building an exe from *_main.py* yourself, only the js and src folders as well as config.ini are required</sub>

+ Start the exe or *_main.py* and you should see the datastream in the terminal after a few seconds.
+ OpenCPN should now display the data you're feeding into the ECAN-W01.

## Additional Information
+ The project uses the [Canboatjs](https://github.com/canboat/canboatjs) package to transform the received data into the *Actisense N2K*-format required by OpenCPN.
+ This has also been tested with the SeaTalk to SeaTalk<sup>ng</sup> converter added to the CAN-Bus. It worked without any further errors and OpenCPN was able to read both the original CAN-Bus and added SeaTalk data.