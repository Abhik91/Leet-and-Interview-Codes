
#Program to Check String Prefix
#@author - Abhik Dey

def checkPrefix(s1,s2):
	#@author - Abhik Dey
	retval = False
	for i in range(len(s1)):
		for j in range(i+1,len(s1)):
			concatString = s1[i]+s1[j]
			if concatString in s2:
				retval = True
				break


	return retval

if __name__ == '__main__':
	
	s1 = ["one", "two", "three"]
	s2 = ["one", "onetwo", "three", "twothree"]

	res = checkPrefix(s1,s2)

	print (res)