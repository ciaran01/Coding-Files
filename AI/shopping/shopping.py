import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Open and read file
    with open(filename) as f:
        reader = csv.reader(f)
        # Skip header line
        next(reader)

        #initialise evidence and labels lists
        evidence = []
        labels = []
        #Read file and populate data lists 
        for row in reader:
            evidence.append(
                [int(row[0]), float(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5]), float(row[6]),
                 float(row[7]), float(row[8]), float(row[9]), month_num(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), 1 if row[15] == "Returning_Visitor" else 0, 1 if row[16] == "TRUE" else 0])
            labels.append(1 if row[17] == "TRUE" else 0)

    #add lists to single data tuple
    data = (evidence, labels)

    #return data tuple
    return data

    raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    #initialise knn model using k = 1
    model = KNeighborsClassifier(n_neighbors=1)
    #train model using training data
    model.fit(evidence, labels)
    #return model
    return model
    raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # initialise count values
    total = 0
    pos_count = 0
    pos_total = 0
    neg_count = 0
    neg_total = 0
    #find length of labels list
    length = len(labels)
    #count correct positive and negative predictions and totals for whole of data set
    while total < length:
        if labels[total] == 1:
            if labels[total] == predictions[total]:
                pos_count += 1
            pos_total += 1
        elif labels[total] == 0:
            if labels[total] == predictions[total]:
                neg_count += 1
            neg_total += 1
        total += 1

    #calculate sensitivity and specificity values
    sensitivity = float(pos_count/pos_total)
    specificity = float(neg_count/neg_total)

    # store values in metrics tuple
    metrics = (sensitivity, specificity)
    #return metrics
    return metrics
    raise NotImplementedError


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
