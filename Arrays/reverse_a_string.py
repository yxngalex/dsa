'''
Create a function that reverses a string:
'Hello My name is John' should be:
'nhoJ si eman yM olleH'
'''

# Strings are just arrays of characters

#O(n)
def reverse(s):
    # Check input if its empty, if it has less than 2 characters or if its not instance of string
    if not s or len(s) < 2 or not isinstance(s, str):
        return None

    reversed_chars = []

    for i in range(len(s)-1, -1, -1): # go backwards from string and append it to an array
        reversed_chars.append(s[i])

    return ''.join(reversed_chars)


#O(n)
def pythonWayReverse(s):
    if not s or len(s) < 2 or not isinstance(s, str):
        return None
    return s[::-1] # Creates a new string which is reversed from original, works in O(n)

#O(n)
def withReverseFunction(s):
    if not s or len(s) < 2 or not isinstance(s, str):
        return None

    chars = list(s) # Turn string into an array of characters
    chars.reverse() # Reverse an array in-place
    return ''.join(chars) #Return back in string

if __name__ == "__main__":
    print(reverse("Hello My name is John"))
    print(pythonWayReverse("Hello My name is John"))
    print(withReverseFunction("Hello My name is John"))
