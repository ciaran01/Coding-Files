def main():
    camelCase = str(input("camelCase: "))
    snake_case = conv_snake(camelCase)
    print("snake_case: ", snake_case)

def conv_snake(camel):
    snake = ""
    for c in camel:
        if c.isupper() == False:
            snake = snake + c
        else:
            snake = snake + "_" + c.lower()
    return snake



main()