import pandas as pd
from hypothesis1 import get_date_range
from collections import Counter


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


def split_retraction_reasons(retracted_articles):
    """
    This function splits the cells containing retraction reason into new rows for each reason.
    :param retracted_articles: A dataframe containing retracted articles
    :return: All retracted articles with each retraction reason expanded to a new row.
    """
    retracted_articles['Reason'] = retracted_articles['Reason'].str.split(';')
    file = retracted_articles.explode('Reason')
    return file


def count_total_retraction_reasons(retracted_articles):
    """
    This function returns the count of retraction reasons
    :param retracted_articles: All retracted articles from the dataset
    :return: A counter of all retraction reasons
    """
    return Counter(retracted_articles['Reason'])


def count_misconduct_by_year(retracted_articles):
    misconduct = retracted_articles.loc[retracted_articles['Reason'] == '+Misconduct by Author']
    return Counter(misconduct['RetractionYear'])


if __name__ == '__main__':
    count_misconduct_by_year(split_retraction_reasons(get_date_range(get_retracted_articles('data/retractions.csv'))))
