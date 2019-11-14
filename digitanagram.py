#Program to find digit anagrams
#@author - Abhik Dey

def breaknumintolist(num):
	#Break number into list
	#@author - Abhik Dey
	l = []
	while num > 0:
		l.append(num%10)
		num = num // 10

	l.sort()
	print (l)
	return l;


def digitanagram(arr):
	#Find digit anagram
	#@author - Abhik Dey
	
	arr1 = []

	for i in range(len(arr)):
		arr1.append(breaknumintolist(arr[i]))

	print (arr1)
	dic = {}


	for i in arr1:
		if (str(i) in dic):
			dic[str(i)] = dic[str(i)] + 1 
		
		else:
			dic[str(i)] = 1

	print("Hello Dictionary:")
	print (dic)

	sum = 0
	for key in dic:
		if dic[key] > 1:
			sum = sum + dic[key]

	print ("Anagram count - ", sum)

def main():
	arr = [23,32,514,145,451,199,154,200,2,991]
	digitanagram(arr)


if __name__ == '__main__':
	main()