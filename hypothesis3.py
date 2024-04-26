import pandas as pd
from hypothesis1 import get_date_range
from collections import Counter


def get_retracted_articles(retraction_file):
    """
    This function reads in a csv file and returns only rows where the retraction nature is retraction.
    :param retraction_file: A csv file with retraction data
    :return: All retracted articles from the dataset
    """
    file = pd.read_csv(retraction_file, usecols=['Reason', 'RetractionDate', 'Author', 'RetractionNature'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def get_author_counts(retracted_articles):
    """
    This function gets the number of authors per retracted article
    :param retracted_articles: All retracted articles from the dataset
    :return: A dataframe with a column with the number of authors per retracted article
    """
    author_counts = []
    for author in retracted_articles['Author']:
        if ';' in author:
            authors = author.split(';')
            author_counts.append(len(authors))
        elif ')' in author:
            authors = author.split(')')
            author_counts.append(len(authors))
        else:
            author_counts.append(1)

    retracted_articles['AuthorCounts'] = author_counts
    return retracted_articles


def get_author_counts_total(retracted_articles):
    """
    This function returns a counter for the number of retractions per author count.
    :param retracted_articles: All retracted articles from the dataset, including an author count column
    :return: A counter with the number of retractions per author count.
    """
    return Counter(retracted_articles['AuthorCounts'])


if __name__ == '__main__':
    get_author_counts_total(get_author_counts(get_date_range(get_retracted_articles('data/retractions.csv'))))
