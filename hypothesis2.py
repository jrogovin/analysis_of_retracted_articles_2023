import pandas as pd
from hypothesis1 import get_date_range


def get_retracted_articles(retraction_file):
    """
    This function reads in a csv file with the columns "RetractionDate" and "RetractionNature" and returns only rows
    where the retraction nature is retraction.
    :param retraction_file: A csv file with retraction data
    :return: All retracted articles from the dataset
    """
    file = pd.read_csv(retraction_file, usecols=['Reason', 'RetractionDate', 'RetractionNature'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def count_retraction_reasons(retracted_articles):
    reasons = retracted_articles['Reason']
    for reason in reasons:
        reason = reason.split(';')
        print(reason)


if __name__ == '__main__':
    count_retraction_reasons((get_date_range(get_retracted_articles('data/retractions.csv'))))


