def check_name(x):
    loi = ['l', 'O', 'I']
    if x in loi:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif x.islower():
        print("It is a common variable")
    elif x.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
