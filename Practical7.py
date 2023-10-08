#Function that accepts two strings and returns the indices of all occurences of second stirng in the first string as a list
str1= "Hello means, hey Hello"
 
str2 = "Hello"
 
print("The original string is : ", str1)

print("The substring to find : " , str2)
 

res = [i for i in range(len(str1)) if str1.startswith(str2, i)]
 

print("The start indices of the substrings are : " + str(res))
    