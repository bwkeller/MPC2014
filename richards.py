import sys
import re
import string

if __name__ == "__main__":
	instr = sys.stdin.readline()
	instr = re.sub(' +',' ',instr)#Remove multiple spaces
	puncstack = []
	puncpos = []
	wordcount = 0
	for char in instr:
		if char == ' ':
			wordcount += 1
		if char == '.' or char == ',' or char =='?' or char == '!':
			puncstack.append(char)
			puncpos.append(wordcount)
	if len(puncstack) > 0:
		instr = string.translate(instr,None,reduce(lambda x,y: x+y, puncstack))
	instr = string.translate(instr,None,'\n')#Remove newline
	words = instr.split(' ')
	out = ""
	idx = 0
	for word in words:
		out += word[::-1]
		if len(puncpos) > 0:
			if idx == puncpos[0]:
				puncpos.remove(puncpos[0])
				out += puncstack.pop()
		out += ' '
		idx += 1
	print out	
