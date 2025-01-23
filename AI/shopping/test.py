import csv
import sys


def main():
    
    
    data = load_data()
    evidence, labels = data
    count = 1
    for e in evidence:
        for item in e:
            if item == None:
                print("ERROR")
                print(item)
                print(count)
                print(e)
                print("ERROR")
                return
        count += 1
    # print(data)

def load_data():
    with open("shopping.csv") as f:
        reader = csv.reader(f)
        next(reader)

        evidence = []
        labels = []
        for row in reader:
            evidence.append(
                [int(row[0]), float(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5]), float(row[6]),
                         float(row[7]), float(row[8]), float(row[9]), month_num(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), 1 if row[15] == "Returning_Visitor" else 0, 1 if row[16] == "TRUE" else 0])
            labels.append(1 if row[17] == "TRUE" else 0)

    print(evidence[0])
    data = (evidence, labels)
    return data

def month_num(month):
    """
    Translates month abbreviation to index number (0 = Jan to 11 = Dec)
    """
    if month == "Jan":
        return 0
    elif month == "Feb":
        return 1
    elif month == "Mar":
        return 2
    elif month == "Apr":
        return 3
    elif month == "May":
        return 4
    elif month == "June":
        return 5
    elif month == "Jul":
        return 6
    elif month == "Aug":
        return 7
    elif month == "Sep":
        return 8
    elif month == "Oct":
        return 9
    elif month == "Nov":
        return 10
    elif month == "Dec":
        return 11
    
if __name__ == "__main__":
    main()


# array = [0,1,2,3,4,5]
# evidence = []
# labels = []
# evidence.append({
#     [int(array[:4])]
# })

# labels.append({
#     [int(array[4:])]
# })

#evidence.append(array[:4])


# print(evidence)
# print(labels)


# data.append({
#                 "evidence": [int(row[0]), float(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5]), float(row[6]),
#                          float(row[7]), float(row[8]), float(row[9]), month_num(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), 1 if row[15] == "Returning_Visitor" else 0, 1 if row[16] == "TRUE" else 0],
#                 "label": 1 if row[17] == "TRUE" else 0
#                 })