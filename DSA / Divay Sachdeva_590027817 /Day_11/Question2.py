# Modify a string by removing all vowels, converting consonants to lowercase, and adding a dot (.) before each consonant.

s = input()

vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch not in vowels:
        result += "." + ch.lower()

print(result)
