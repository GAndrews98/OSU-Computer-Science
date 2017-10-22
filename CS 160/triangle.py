import time
stars = int(input("What is the max number of odd stars you want? "))

i = 1
for i in range(1,stars+1,2):
	print(((stars+1-i)//2)*" " + i*"*")
	time.sleep(0.1)
