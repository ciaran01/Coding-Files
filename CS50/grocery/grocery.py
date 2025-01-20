
list = {

}

def main():
    while True:
        try:
            item = input().upper()
            find_item(item)
        except EOFError:
            sorted_list = dict(sorted(list.items(), key=lambda item: item[0]))
            for i in sorted_list:
                print(sorted_list[i], i)
            break


def find_item(x):
    if x in list:
        list[x] = list[x] + 1
    else:
        list[x] = 1



main()