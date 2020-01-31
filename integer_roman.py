# Code to print Roman Numeral to Integer and vice versa
# Integer Range - 1-3999
# Author - Abhik Dey

# Method to print Roman Numeral from Integer - @akd
def intToRoman(num):
	
	romanDic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
	div = 1000
	romanNumeral = ""
	
	while (num != 0):
		quotient, temp = divmod(num, div)
		if quotient == 9:
			romanNumeral += romanDic[div] + romanDic[div*10]
		elif quotient == 4:
			romanNumeral +=romanDic[div] + romanDic[div*5]
		elif quotient >= 5:
			romanNumeral += romanDic[div*5] + romanDic[div]*(quotient - 5)
		else:
			romanNumeral += romanDic[div]*quotient        
		div = div//10
		num = temp

	return romanNumeral

# Method to print Integer from Roman - @akd
def romanToInt(roman):
	romanDic = {"I": 1, "V":5, "X":10, "L": 50 , "C":100 , "D":500 , "M":1000 }
	num = []
	curr = len(roman)-1
	prev = curr - 1
	
	while curr >=0:
		
		#print ('prev - ', prev)
		#print ('curr - ', curr)
		#print ('roman[curr] - ', roman[curr])
		#print ('roman[prev] - ',roman[prev])

		if (romanDic[roman[prev]] < romanDic[roman[curr]]) and (prev >= 0):
			# print ('if - ')
			# print (roman[curr],'---->',romanDic[roman[curr]])
			# print (roman[prev],'---->',romanDic[roman[prev]])
			# val = romanDic[roman[curr]]-romanDic[roman[prev]]
			# print ('Value - ',val)
			num.append(romanDic[roman[curr]]-romanDic[roman[prev]])
			curr = prev - 1
			prev = curr - 1
		else:
			#print ('else - ',roman[curr])
			num.append(romanDic[roman[curr]])
			curr = curr - 1
			prev = curr - 1


	print (sum(num))
	return 0


if __name__ == '__main__':
	print (intToRoman(3999))
	#print (romanToInt("MMMCMXCIX"))
	romanToInt("MMMCM")