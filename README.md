aquarimeter
===========

The Fall 2014 Capstone project written by Robert O’Connor(@robbyoconnor), Mark Stein (@mystycs) and Sudish Itwaru (@SI37)

The hardware control software lives in this repository.

MCP3008 connection to raspberry pi(based on bcm pin layout):
MCP3008 VDD -> 3.3V (red), 
MCP3008 VREF -> 3.3V (red), 
MCP3008 AGND -> GND (black), 
MCP3008 CLK -> #18 (orange), 
MCP3008 DOUT -> #23 (yellow), 
MCP3008 DIN -> #24 (blue), 
MCP3008 CS -> #25 (violet), 
MCP3008 DGND -> GND (black), 

connect ph sensor to ch0 on MCP3008
connect pir sensor to ch1 on MCP3008

SN754410 connection to raspberry pi:
SN754410 1 -> #2, 
SN754410 2 -> #17, 
SN754410 3 -> peltio(red), 
SN754410 4 -> GND, 
SN754410 5 -> GND, 
SN754410 6 -> peltio(black), 
SN754410 7 -> #27, 
SN754410 8 -> 5v, 
SN754410 9 -> #3, 
SN754410 10 -> #10, 
SN754410 11 -> peltio(red), 
SN754410 12 -> GND, 
SN754410 13 -> GND, 
SN754410 14 -> peltio(black), 
SN754410 15 -> #9, 
SN754410 16 -> 5v, 