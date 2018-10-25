# Python-DSRC-BSM-Mapping
# Python-DSRC-BSM-Mapping

Quick script, to read data from a json file exported from WireShark with a custom SAE J2735 Wireshark Dissector plugin, and plot BasicSafetyMessage GPS Coordinates to map.

Tested on live data picked up in an urban city. 


JSON File not provided.

Steps to recreate: 

1.) Obtain data in wireshark and dissect using an SAE J2735 Dissector plugin. 

2.) Export the packets from wireshark to JSON Format 

3.) Run script using python mapDSRC.py 

4.) Script will auto open map in browser after it creates it. 
