import pandas as pd
from hypothesis1 import get_date_range


def get_retracted_articles(retraction_file):
    """
    This function reads in a csv file and returns only rows where the retraction nature is retraction.
    :param retraction_file: A csv file with retraction data
    :return: All retracted articles from the dataset
    """
    file = pd.read_csv(retraction_file, usecols=['Reason', 'RetractionDate', 'OriginalPaperDate'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def get_