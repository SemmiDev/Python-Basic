def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse2(s[1:]) + s[0]


s = "hello"
print(s[::-1])

# print(reversed(s))