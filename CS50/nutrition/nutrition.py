fruits = [
    {"fruit": "apple", "cal": "130"},
    {"fruit": "avocado", "cal": "50"},
    {"fruit": "banana", "cal": "110"},
    {"fruit": "cantaloupe", "cal": "50"},
    {"fruit": "grapefruit", "cal": "60"},
    {"fruit": "grapes", "cal": "90"},
    {"fruit": "honeydew melon", "cal": "50"},
    {"fruit": "kiwifruit", "cal": "90"},
    {"fruit": "lemon", "cal": "15"},
    {"fruit": "lime", "cal": "20"},
    {"fruit": "nectarine", "cal": "60"},
    {"fruit": "orange", "cal": "80"},
    {"fruit": "peach", "cal": "60"},
    {"fruit": "pear", "cal": "100"},
    {"fruit": "pineapple", "cal": "50"},
    {"fruit": "plums", "cal": "70"},
    {"fruit": "strawberries", "cal": "50"},
    {"fruit": "sweet cherries", "cal": "100"},
    {"fruit": "tangerine", "cal": "50"},
    {"fruit": "watermelon", "cal": "80"}
]

item = str(input("Item: "))

for f in fruits:
    if f["fruit"] == item.lower():
        print("Calories:", f["cal"])