import sys
from math import sin,cos,pi
g = 9.81

if __name__ == "__main__":
	num = int(sys.stdin.readline().strip())
	obstacles = []
	for i in range(num):
		obstacles.append(map(lambda x: int(x.strip()), sys.stdin.readline().split(' ')))
	maxx = 0
	for obs in obstacles:
		if obs[0] > maxx:
			maxx = obs[0]
	for obs in obstacles:
		if obs[0] == maxx:
			targ = obs
			obstacles.remove(obs)
	angles = range(0,76)
	bags = range(1,7)
	stop = False
	for j in bags:
		if stop:
			break
		for i in angles:
			v_tot = 150*j
			v_x = v_tot*cos(float(i)*pi/180)
			v_y = v_tot*sin(float(i)*pi/180)
			for obs in obstacles:
				if v_y*(obs[0]/v_x)-0.5*g*(obs[0]/v_x)*(obs[0]/v_x) <= obs[1]+10:
					fail = True
					break
				else:
					fail = False
			if fail:
				continue
			if v_y*(targ[0]/v_x)-0.5*g*(targ[0]/v_x)*(targ[0]/v_x) >= targ[1]-10 and v_y*(targ[0]/v_x)-0.5*g*(targ[0]/v_x)*(targ[0]/v_x) <= targ[1]+10:
				print i, j
				stop = True
				break
	if not stop:
		print "No Solution"
