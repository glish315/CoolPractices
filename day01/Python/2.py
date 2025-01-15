def reverse_string(s):
    string = ""
    index = len(s)
    while index:
        index -= 1
        string += s[index]
    return string


x = reverse_string("123456789")
print(x)
