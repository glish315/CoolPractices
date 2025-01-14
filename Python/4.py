def is_valid_brackets(s):

    x = "{[()]}"

    if x == s:
        print("True")
    else: 
        print("False")


is_valid_brackets("()[]{}")
is_valid_brackets("([]}")
is_valid_brackets("{[()]}")



