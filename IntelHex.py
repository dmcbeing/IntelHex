#!/bin/python
#Convert binary file to Intel Hex
import sys

if len(sys.argv) not in range(2,4):
	print("Usage:\n\t",sys.argv[0],"<input.bin> [output.hex]")
	exit()

in_bin = open(sys.argv[1],"rb")
out_hex = sys.stdout
if len(sys.argv) == 3:
	out_hex = open(sys.argv[2],"w")

try:
	addr = 0
	bytes32 = in_bin.read(32)
	while bytes32 != b'':
		line = ":"+"%0.2X"%(len(bytes32))
		line = line + "%0.4X"%(addr)+"00"
		chk = len(bytes32) + (addr & 255) + (addr>>8)&255 + (addr>>16)&255 + (addr>>24)&255
		for byte in bytes32:
			line = line + "%0.2X"%byte
			chk = chk + int(byte)
		chk = (256-(chk & 255)) & 255
		out_hex.write(line+"%0.2X"%(chk)+"\n")
		addr = addr + len(bytes32)
		bytes32 = in_bin.read(32)
	out_hex.write(":00000001FF\n")
finally:
	in_bin.close()
	out_hex.close()
