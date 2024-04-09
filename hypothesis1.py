
import pandas as pd


def process_datafile():
    file = pd.read_csv('data/retractions.csv', usecols=['RetractionDate', 'RetractionNature'])
    print(file)



if __name__ == '__main__':
    process_datafile()

