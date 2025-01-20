def main():
    inp = str(input(""))
    convert(inp)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    print(text)

main()