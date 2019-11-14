#Code to merge two strings using Python

string1 = ["a","b","c","d"]
string2v  = ["d","e","f","z"]
new_string =""

for i,j in zip(string1, string2v):
	new_string = new_string + i + j

print (new_string)

# Tuple examples:

# Heterogenious
t1 = (123,234,"Hello World", 46.56)
print (type(t1))

#Nested
u = (1,2,3,4,5)
z = t1,u
print (z)
print (type(z))

#Typle contains mutable objects
xt = ([1,2,3,4,5],[23,45,67,8])
print (xt)

# Reverse Tupple
tp_reverse = ("abcd",1234,45.6)
x,y,z = tp_reverse
print("x-",x)
print("y-",y)
print("z-",z)

# Dictionary:
dictionary = {"Key1":12345678, "key2":678912}
print (dictionary)

# looping through dictionary:
for key, value in dictionary.items():
	print ("key - ",key)
	print ("value - ", value)