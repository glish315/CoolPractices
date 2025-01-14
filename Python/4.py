def is_valid_brackets(s):

    brackets = ["(", ")", "{", "}", "[", "]"]

    if all(x in s for x in brackets):
        print("True")
    else:
        print("False")





is_valid_brackets("()[]{}")
is_valid_brackets("([]}")



