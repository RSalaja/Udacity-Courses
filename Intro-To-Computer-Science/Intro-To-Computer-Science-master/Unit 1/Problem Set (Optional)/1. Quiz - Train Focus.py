# Given a string s = "CidatyUcityda",
# which of the following expressions is
# equivalent to the string "Udacity"?

s = "CidatyUcityda"

print(s[6] + s[-2:] + s[7:12])
print(s[-7] + s[2:4] + s[7:11])
print(s[6] + s[-2:] + s[7:11])
print(s[6] + s[-2] + s[3] + s[:2] + s[4:6])
print(s[6] + s[2:4] + s[7:13])
print(s[6] + s[2] + s[3] + s[7:11])
