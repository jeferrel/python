def pangrams(s):
    # Write your code here
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in s:
            return "not pangram"
    return "pangram"

string = "We promptly judged antique ivory buckles for the next prize"
result = pangrams(string)
print(result)



