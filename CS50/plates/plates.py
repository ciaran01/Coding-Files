def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Must start with at least 2 letters
    if len(s) >= 2:
        if s[0].isdigit() == True or s[1].isdigit() == True:
            return False
    #max 6 characters and min 2 characters:
    if len(s) < 2 or len(s) > 6:
        return False
    #Numbers not in the middle and 1st number cannot be a 0
    for i in range(len(s)):
        if s[i].isdigit() == True:
            s_1, s_2 = s.split(s[i-1])
            if s_2.isnumeric() == False:
                return False
            if s[i] == "0":
                return False
            break


    #no periods, spaces or punctuation

    for c in s:
        if c.isdigit() == False and c.isalpha() == False:
            return False

    else:
        return True



main()
