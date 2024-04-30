import pandas as pd
from collections import Counter


def get_retracted_articles(retraction_file):
    """
    This function reads in a csv file with the columns "RetractionDate" and "RetractionNature" and returns only rows
    where the retraction nature is retraction.
    :param retraction_file: A csv file with retraction data
    :return: All retracted articles from the dataset
    """
    file = pd.read_csv(retraction_file, usecols=['RetractionDate', 'RetractionNature'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def get_date_range(retracted_articles):
    """
    This function takes retracted articles and returns only articles retracted between 2000 and 2023.
    :param retracted_articles: A variable containing retracted articles
    :return: All retracted articles retracted between 2000 and 2023.
    >>> data = ['3/21/2024', '7/5/2023', '8/7/2000', '12/31/1979']
    >>> df = pd.DataFrame(data, columns=['RetractionDate'])
    >>> new_df = get_date_range(df)
    >>> new_df
      RetractionDate  RetractionYear
    0      3/21/2024            2024
    1       7/5/2023            2023
    2       8/7/2000            2000
    """
    years = []
    for datetime in retracted_articles['RetractionDate']:
        date = datetime.split(' ')
        day_month_year = date[0].split('/')
        year = day_month_year[2]
        years.append(int(year))
    retracted_articles['RetractionYear'] = years

    retracted_articles = retracted_articles.loc[retracted_articles['RetractionYear'] >= 2000]
    return retracted_articles


def count_years(retracted_articles):
    """
    This function returns the count of retracted articles per year.
    :param retracted_articles: All retracted articles from the dataset.
    :return: A counter of all retracted articles per year.
    >>> data = ['2024', '2024', '2024', '2021', '2000', '2000', '1970']
    >>> df = pd.DataFrame(data, columns=['RetractionYear'])
    >>> new_df = count_years(df)
    >>> new_df
    Counter({'2024': 3, '2000': 2, '2021': 1, '1970': 1})
    """
    return Counter(retracted_articles['RetractionYear'])


if __name__ == '__main__':
    count_years(get_date_range(get_retracted_articles('data/retractions.csv')))

