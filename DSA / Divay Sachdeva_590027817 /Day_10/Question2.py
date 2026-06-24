# Count distinct characters in a string and print "CHAT WITH HER!" if even, "IGNORE HIM!" if odd.

s = input()

count = len(set(s))

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
