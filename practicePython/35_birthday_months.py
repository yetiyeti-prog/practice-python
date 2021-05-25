import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

NUM_TO_STRING_MOTNHS = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


def birthday_months():
    with open("birthday.json", 'r') as f:
        birthday_matrix = json.load(f)
    value_list = birthday_matrix.values()
    month_list = []
    string_month_list = []
    for i in value_list:
        month_list.append(i.split("-")[1])
    for i in month_list:
        key = NUM_TO_STRING_MOTNHS.get(i)
        string_month_list.append(key)
    print("Birthday Month Matrix:{}".format(Counter(string_month_list)))
    represent_graphically(string_month_list)


def represent_graphically(string_month_list):
    month_dictionary = Counter(string_month_list)
    total_list = list(NUM_TO_STRING_MOTNHS.values())
    keys = list(month_dictionary.keys())
    values = list(month_dictionary.values())
    output_file("plot.html")
    x_categories = total_list
    x = keys
    y = values
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)


if __name__ == '__main__':
    birthday_months()
