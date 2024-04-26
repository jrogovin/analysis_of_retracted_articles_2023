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

    years = []
    for datetime in retracted_articles['RetractionDate']:
        date = datetime.split(' ')
        day_month_year = date[0].split('/')
        year = day_month_year[2]
        years.append(int(year))
    retracted_articles['RetractionYear'] = years

    return retracted_articles


def convert_columns_to_datetime(retracted_articles):
    """
    This function converts the values in RetractionDate and OriginalPaperDate to datetime objects.
    :param retracted_articles: A dataframe containing retracted articles
    :return: Columns with dates as datetime objects
    """
    retracted_articles['RetractionDate'] = retracted_articles['RetractionDate'].apply(pd.to_datetime)
    retracted_articles['OriginalPaperDate'] = retracted_articles['OriginalPaperDate'].apply(pd.to_datetime)

    return retracted_articles


def get_time_between_dates(retracted_articles):
    retracted_articles['TimeLag'] = ((retracted_articles['RetractionDate'] - retracted_articles['OriginalPaperDate'])
                                     .dt.days)
    retracted_articles['TimeLag'] = retracted_articles['TimeLag'] / 365
    return retracted_articles


def get_mean_article_age_per_year(retracted_articles):
    years = set(retracted_articles['RetractionYear'])
    for year in years:
        df = retracted_articles.loc[retracted_articles['RetractionYear'] == year, ['TimeLag']]
        mean_time_lag = df['TimeLag'].mean()
        return year, mean_time_lag


if __name__ == '__main__':
    get_mean_article_age_per_year(get_time_between_dates(convert_columns_to_datetime(get_retracted_articles('data/retractions.csv'))))
