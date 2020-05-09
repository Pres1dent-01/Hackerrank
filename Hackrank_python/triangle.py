#That a median on the hypotenuse divides the right angled triangle in two isoceles triangle.** 
#*Means AM=BM=CM * 
#So, ∡MBC = ∡MCB
import math
ab = int(input())
bc = int(input())
#The purpose of using two arguments instead of one is to gather information on the signs of the inputs in order to return the appropriate quadrant of the computed angle, which is not possible for the single-argument arctangent function. It also avoids the problems of division by zero.
print(str(int(round(math.degrees(math.atan2(ab, bc)))))+ '°')
