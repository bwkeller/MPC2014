import sys


if __name__ == "__main__":
	N, M = map(lambda x: int(x), sys.stdin.readline().split(' '))
	strands = []
	for i in range(N):
		strands.append(map(lambda x: int(x), sys.stdin.readline().split(' ')))
	B = 0
	perms = [[0]*M]*N
	i = 0
	for strand in strands:
		for j in range(M):
			if strand[1] <= j:
				perms[i][j] = max(perms[i-1][j], perms[i-1][j-strand[1]] + strand[0])
			else:
				perms[i][j] = perms[i-1][j]
		i+=1
	print perms[N-1][M-2]
