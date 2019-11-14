# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair = 0
    unique_val = []
    unique_val = unique_list(ar)

    for i in unique_val:

        pair = pair + int(ar.count(i)/2)
    
    return pair

# Check for unique values in the array:
def unique_list(ar):
    unique_list_val = []

    for i in ar:
        if i not in unique_list_val:
            unique_list_val.append(i)
    
    return unique_list_val


if __name__ == "__main__":
	ar = [10, 20, 20,10, 10, 30, 50, 10, 20]
	n = 9
	result = sockMerchant(n,ar)

	print(result)

