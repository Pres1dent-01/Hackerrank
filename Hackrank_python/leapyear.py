"""year = int(input())
def leapyr():
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return 'True'
	else:
		return 'False'
print(leapyr())"""

#The more logical way!
year = int(input())
def leapyr(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #Since the return keyword returns boolena we can get the answer directly without any conditional ifelse loop
print(leapyr(year))