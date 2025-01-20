def main():
    tweet = str(input("Input: "))
    twt = x_vowel(tweet)
    print("Output:", twt)

def x_vowel(text):
    txt = ""
    check = False
    vowel = ["a", "e", "i", "o", "u"]
    #search through text input
    for c in text:
        #check against vowel list
        for v in vowel:
            if c.lower() == v:
                check = True
        #add to output if not a vowel
        if check == False:
            txt = txt + c
        else:
            check = False

    return txt

main()