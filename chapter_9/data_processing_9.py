import pandas as pd
import csv

crime_to_data = {}
crime_stack = []

def structure_raw_data():

    with open("raw_data_9.txt", "rt") as file:
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

                        if index == 1:
                            crime.extend(crime[index].split(maxsplit=1))
                            
                        crime[index] = crime[index].strip()
                    
                    crime.pop(1)
                    crime.insert(0,crime_stack[-1])
                    crime.insert(0, len(crime_stack))
                    crime.append(".")
                    crime_to_data[crime_stack[-1]].append(crime)



def create_csv():

    with open("processed_data_9.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Charge_ID", "Charge", "Date", "City", "State" , "First_Name", "Last_Name", "Gender"])

        for crime in crime_to_data:
            for data in crime_to_data[crime]:
                writer.writerow(data)


def create_excel():

    read_file = pd.read_csv("processed_data_9.csv")
    read_file.to_excel("processed_data_9.xlsx", header = True, index = None)

if __name__ == "__main__":
    structure_raw_data()
    create_csv()
    create_excel()