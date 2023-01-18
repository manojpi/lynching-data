import pandas as pd
import csv

crime_to_data = {}
crime_stack = []

def structure_raw_data():

    with open("raw_data_2.txt", "rt") as file:
        for line in file:
            if not line.isspace():
                if line.isupper():
                    line = line.strip("\n")
                    crime_stack.append(line.capitalize())
                    crime_to_data[crime_stack[-1]] = []
                    continue
                

                for crime in line.split("; "):
                    crime = crime.strip("\n")
                    crime = crime.split(", ")
                    for index in range(len(crime)):
                            
                        crime[index] = crime[index].strip()

                    crime_to_data[crime_stack[-1]].append(crime)
                    crime.append(crime_stack[-1])
                    crime_to_data[crime_stack[-1]].append(crime)


def create_csv():

    with open("processed_data_2.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Date","Name","Location","State","Crime"])

        for crime in crime_to_data:
            for data in crime_to_data[crime]:
                writer.writerow(data)


def create_excel():

    read_file = pd.read_csv("processed_data_2.csv")
    read_file.to_excel("processed_data_2.xlsx", header = True, index = None)

if __name__ == "__main__":
    structure_raw_data()
    create_csv()
    create_excel()