from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

# sends get http request to the site for the data
response = requests.get("https://americanlynchingdata.com/data/Project_HAL.csv")

# to store the well formatted response in to a text file i.e. "lynching-data.txt"
text_file = open("./american-lynching-data/lynching_data.txt", "at")
text_file.write(response.text)
text_file.close()

# function to format "lynching-data.txt" into .csv file
def create_csv():

    with open("./american-lynching-data/lynching_data.txt") as text_file:
        with open("./american-lynching-data/lynching_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)

            for line in text_file:
                line = line.split(",")
                line.pop()
                for index in range(len(line)):
                    line[index] = line[index].strip()
                    line[index] = line[index].strip("'")
                    line[index] = line[index].strip('"')
                
                writer.writerow(line)


# function to convert the "lynching-data.csv" file into .xlsx file
def create_excel():

    read_file = pd.read_csv("./american-lynching-data/lynching_data.csv",on_bad_lines='skip')
    read_file.to_excel("./american-lynching-data/lynching_data.xlsx", header = True, index = None)


if __name__ == "__main__":
    create_csv()
    create_excel()
