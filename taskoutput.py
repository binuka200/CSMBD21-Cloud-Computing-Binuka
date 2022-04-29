#Install Pandas library to get Task Outputs as CSV files(pip install pandas)
import pandas as pd

def task1output(list):
    """ Output the total number of flights from each airport as a CSV file(Task1_Output.csv)
        Args:
			list : list of total number of flights from each airport
		Return:
			CSV file : Task1_Output.csv """

    dicts = {
        "Airport Name":[],
        "Number of Flights":[]
    }

    #loop through the number of flights from each airport and adds it to the dictonary
    for k,v in list:
        dicts["Airport Name"].append(k)
        dicts["Number of Flights"].append(v)

    #Writes the Output dataframe to CSV file
    df = pd.DataFrame(dicts)
    df.to_csv("./Task1_Output.csv",index=False)


def task2output(list):
    """Output the passengers with the highest number of flights as a CSV file(Task1_Output.csv)
        Args:
			list : list of passengers with the highest number of flights
		Return:
			CSV file : Task2_Output.csv """

    dicts = {
        "Passengers with highest number of flights": [],
        "Number of Flights": []
    }

    # loop through the passengers with the highest number of flights and adds it to the dictonary
    for k, v in list:
        dicts["Passengers with highest number of flights"].append(k)
        dicts["Number of Flights"].append(v)

    # Writes the Output dataframe to CSV file
    df = pd.DataFrame(dicts)
    df.to_csv("./Task2_Output.csv",index=False)


