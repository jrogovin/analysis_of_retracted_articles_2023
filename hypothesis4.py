import pandas as pd
from hypothesis1 import get_date_range


def get_retracted_articles(retraction_file):
    """
    This function reads in a csv file and returns only rows where the retraction nature is retraction.
    :param retraction_file: A csv file with retraction data
    :return: All retracted articles from the dataset
    """
    file = pd.read_csv(retraction_file, usecols=['Reason', 'RetractionDate', 'OriginalPaperDate', 'RetractionNature'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def convert_columns_to_datetime(retracted_articles):
    """
    This function converts the values in RetractionDate and OriginalPaperDate to datetime objects.
    :param retracted_articles: A dataframe containing retracted articles
    :return: Columns with dates as datetime objects
    """
    retracted_articles['RetractionDate'] = retracted_articles['RetractionDate'].apply(pd.to_datetime)
    retracted_articles['OriginalPaperDate'] = retracted_articles['RetractionDate'].apply(pd.to_datetime)


def get_time_between_dates(retracted_articles):



if __name__ == '__main__':
    convert_columns_to_datetime(get_date_range(get_retracted_articles('data/retractions.csv')))
