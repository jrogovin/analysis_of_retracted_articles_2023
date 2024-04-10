import pandas as pd


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


def get_2023_and_earlier(retracted_articles):
    """
    This function takes retracted articles and returns only articles retracted in 2023 and earlier.
    :param retracted_articles: A variable containing retracted articles
    :return: All retracted articles retracted in 2023 and earlier.
    """
    years = []
    for datetime in retracted_articles['RetractionDate']:
        date = datetime.split(' ')
        day_month_year = date[0].split('/')
        year = day_month_year[2]
        years.append(int(year))
    retracted_articles['RetractionYear'] = years

    retracted_articles = retracted_articles.loc[retracted_articles['RetractionYear'] < 2024]
    return retracted_articles


if __name__ == '__main__':
    get_2023_and_earlier(get_retracted_articles('data/retractions.csv'))

