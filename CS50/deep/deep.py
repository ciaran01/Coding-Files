ans = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
ans = ans.strip().lower()
if ans == "42" or ans.lower() == "forty two" or ans.lower() == "forty-two":
    print("Yes")
else:
    print("No")
