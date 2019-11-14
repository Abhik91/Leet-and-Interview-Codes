#Sliding window Technique:

def maxSumofSubArray(arr,k):
	if (len(arr) < k):
		print ("INvalid")
		return -1

	#Compute the sum of the first window:
	#max_sum = INT_MIN 
	window_max = sum([arr[i] for i in range(k)])
	max_sum = window_max

	for i in range(len(arr)-k):
		window_max = window_max - arr[i] + arr[i+k]
		max_sum = max([window_max, max_sum])
	return max_sum


arr = [10,50,20,40,30]
s = maxSumofSubArray(arr, 3)
print (s)
