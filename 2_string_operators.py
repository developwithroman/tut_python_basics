# some useful operators for string 
# + operator to concatenate strings
# * operator to repeat the string
# [] operator to access the characters in the string
# [:] operator to slice the string
# in operator to check if the string contains a specific substring
# not in operator to check if the string does not contain a specific substring
# r/R operator to print the raw string
# find operator to find the index of a substring
# replace operator to replace a substring with another substring
# split operator to split the string into a list of substrings
# join operator to join the substrings in a list into a single string
# count operator to count the occurrences of a substring in the string

# program to demonstrate the use of string operators
string1 = "Hello"
string2 = "World"
string3 = string1 + string2 # concatenation
print(string3) 
print(string1 * 3) # repetition
print(string1[1]) # accessing the character at index 1
print(string1[1:4]) # slicing the string
print("Hello" in string1) # checking if the string contains "Hello"
print("Hello" not in string1) # checking if the string does not contain "Hello"
print(r"Hello\nWorld") # printing the raw string
print(string1.find("l")) # finding the index of the first occurrence of "l" in the string
print(string1.replace("l", "L")) # replacing "l" with "L" in the string
print(string1.split("l")) # splitting the string into a list of substrings
print("-".join(string1)) # joining the substrings in a list into a single string
print(string1.count("l")) # counting the occurrences of "l" in the string