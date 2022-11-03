def opcode_to_shellcode(opcode):
	shellcode = []
	for i in range(0, len(opcode), 2):
		shellcode.append('\\x' + opcode[i : i+2])
	return ''.join(shellcode)
