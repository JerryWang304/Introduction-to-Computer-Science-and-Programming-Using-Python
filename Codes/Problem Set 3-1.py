def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)
	
def radiationExposure(start, stop, step):
    ans = 0.0
    num = int((stop-start)/step)
    for i in range(num):
        ans += f(start+i*step)*step
    return round(ans,14)
print radiationExposure(14, 20, 0.1)