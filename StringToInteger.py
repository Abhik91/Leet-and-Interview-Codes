'''
Leet Question:
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as 
possible, and interprets them as a numerical value.@akd

The string can contain additional characters after those that form the integral number, which are ignored and have no 
effect on the behavior of this function.@akd

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.@akd

If no valid conversion could be performed, a zero value is returned.@akd

Note:

Only the space character ' ' is considered as whitespace character.@akd
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) 
is returned.@akd

Author - Abhik Dey
'''

INT_MAX = (2**31) - 1
INT_MIN = -(2**31)

def stringToInteger(s):
	sti =s.strip()
	new_str = ''
	ret_val = 0

	if s is None or len(s) == 0:
		return 0

	#print (sti.index('+'))


	try:

		i = sti[0]		

		if i != '+' and i != '-' and not(ord(i) >= 48 and ord(i) <=57):
			return 0

		for i in range (len(sti)):

			if (sti[i] == '+' or sti[i] == '-') and (i!=0):
				break

			if (sti[i] == '+' or sti[i] == '-') or (ord(sti[i]) >= 48 and ord(sti[i]) <=57 ):
				new_str = new_str + sti[i]
			else:
				break

		print ("Hello New String - ",new_str)

		ret_val = int(new_str)

		if ret_val > INT_MAX:
			ret_val = INT_MAX
		elif ret_val < INT_MIN:
			ret_val = INT_MIN
	except:
		return 0

	return ret_val

def main ():
	s = stringToInteger("42")
	print (s)

if __name__ == '__main__':
	main()