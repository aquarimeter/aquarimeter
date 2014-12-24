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

DRV8833 connection to raspberry pi:

B1 in - > #27
B2 in -> #17
A1 in -> #14
A2 in -> #15
vin -> power supply
gnd(same side as vin) - >gnd
gnd(side as a1 a2 b1 b2) ->pi gnd

peltier cooler connection to DRV8833:

B1 out - > red wire
B2 out -> black wire
A1 out -> red wire
A2 out -> black wire

thermometer connection to raspberry pi:

ds18b20 (yellow) -> #4
