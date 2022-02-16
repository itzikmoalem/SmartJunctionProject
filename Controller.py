import csv
from Junction import Junction


class Controller:
    def __init__(self):
        # csv_file = input("Please Enter CSV File: ")
        # self.createJunctionsByCSV("csv_file")
        _JunctionsList = []
        _JunctionsList = self.createJunctionsByCSV("INPUT_JUNCTION.csv")

    # this method read csv file, and create junctions
    def createJunctionsByCSV(self, path):
        # ** כאן צריך לקרוא את הקובץ ולייצר JUNCTIONS
        # לכל צומת נשלח ארגיומנטים מתוך הקובץ לבנאי
        print(path)
        junction_list = []
        Jtype = "R"
        Jname = "Junction 01"

        junction_list.append(Junction(Jtype, Jname))

        return junction_list








