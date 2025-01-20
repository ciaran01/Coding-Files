
def main():
    perc = fuel_perc()
    if perc == 0 or perc == 1:
        print("E")
    elif perc == 100 or perc == 99:
        print("F")
    else:
        print("%d" % round(perc, 0), "%", sep="")

def fuel_perc():
    while True:
        try:
            x = input("Fraction: ")
            n, d = x.split("/")
            fuel = int(n) / int(d) * 100
            if 0 <= fuel <= 100:
                return fuel
        except (ValueError, ZeroDivisionError):
            pass


main()