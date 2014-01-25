import sys

def component(A,B,part):
	if part[0] == 'I':
		return not A
	if part[0] == 'O':
		return A or B
	if part[0] == 'A':
		return A and B
	if part[0] == 'X':
		return (A and not B) or (not A and B)

def get_output(A,B,Apin,Bpin,outpin,net):
	if len(net) == 1:
		if net[0][0] == 'I' and Bpin == net[0][1]:
			return component(B,A,net[0])
		else:
			return component(A,B,net[0])
	else:
		for i in net:
			if i[3]==outpin:
				final_part = i
				net.remove(final_part)
		return component(get_output(A,B,Apin,Bpin,final_part[1], list(net)), get_output(A,B,Apin,Bpin,final_part[2], list(net)), final_part)

def parse_input():
	clk_mode, num = map(lambda x: int(x), sys.stdin.readline().split(' '))
	binary = map(lambda x: int(x), sys.stdin.readline()[:-1].strip())
	network = []
	for i in range(num):
		instr = sys.stdin.readline().split(' ')
		if instr[0] == 'I':
			network.append((instr[0], int(instr[1]), -1, int(instr[2])))
		else:
			network.append((instr[0], int(instr[1]), int(instr[2]), int(instr[3])))
	return (clk_mode, num, binary, network)

if __name__ == "__main__":
	clk_mode, num, instring, net = parse_input()
	outstring = [1]
	for i in range(10):
		if clk_mode == 0:
			clk = i % 2
		if clk_mode == 1:
			clk = (i % 4) / 2
		if clk_mode == 2:
			clk = (i % 8) / 4
		inpin = instring[i]
		outstring.append(get_output(not clk,inpin,1,2,0,list(net)))
	print reduce(lambda x,y: str(int(x))+str(int(y)), outstring)[1:]
