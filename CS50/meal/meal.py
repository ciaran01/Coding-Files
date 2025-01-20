def main():
    t = input("What time is it? ")
    hours = convert(t)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    hours = int(hours) + minutes
    return hours


if __name__ == "__main__":
    main()