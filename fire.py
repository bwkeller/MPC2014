import sys
if __name__ == "__main__":
	grid = []
	for i in range(10):
		grid.append(list(sys.stdin.readline().strip()))
	spreadable = True
	time = 0
	while spreadable:
		time += 1
		spreadable = False
		for i in range(10):
			for j in range(10):
				if grid[i][j] == 'T':
					burn = True
					for k in [-1,1]:
						if grid[i+k][j] == 'W':
							burn=False
						if grid[i][j+k] == 'W':
							burn=False
					if burn:
						for k in [-1,1]:
							if grid[i+k][j] == 'F':
								grid[i][j] = 'f'
								spreadable = True
							if grid[i][j+k] == 'F':
								grid[i][j] = 'f'
								spreadable = True
				if grid[i][j] == 'W':
					for k in [-1,0,1]:
						for l in [-1,0,1]:
							if grid[i+k][j+l] == 'F':
								grid[i][j] = ','
								spreadable = True
		for i in range(10):
			for j in range(10):
				if grid[i][j] == 'f':
					grid[i][j] = 'F'
				if grid[i][j] == ',':
					grid[i][j] = '.'
	alive = False
	for i in range(10):
		for j in range(10):
			if grid[i][j] == 'T':
				alive = True
	if alive:
		print -1
	else:
		print time-1
