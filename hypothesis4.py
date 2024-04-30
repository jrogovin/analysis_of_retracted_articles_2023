import pandas as pd


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
    >>> data = [['3/21/2024', '2/4/2020'], ['3/18/2024 0:00', '2/17/2020']]
    >>> df = pd.DataFrame(data, columns=['RetractionDate', 'OriginalPaperDate'])
    >>> new_df = convert_columns_to_datetime(df)
    >>> new_df
      RetractionDate OriginalPaperDate
    0     2024-03-21        2020-02-04
    1     2024-03-18        2020-02-17
    >>> new_df.dtypes
    RetractionDate       datetime64[ns]
    OriginalPaperDate    datetime64[ns]
    dtype: object
    """
    retracted_articles['RetractionDate'] = retracted_articles['RetractionDate'].apply(pd.to_datetime)
    retracted_articles['OriginalPaperDate'] = retracted_articles['OriginalPaperDate'].apply(pd.to_datetime)

    return retracted_articles


def get_time_between_dates(retracted_articles):
    retracted_articles['TimeLag'] = ((retracted_articles['RetractionDate'] - retracted_articles['OriginalPaperDate'])
                                     .dt.days)
    retracted_articles['TimeLag'] = retracted_articles['TimeLag'] / 365
    return retracted_articles


if __name__ == '__main__':
    get_time_between_dates(convert_columns_to_datetime(get_retracted_articles('data/retractions.csv')))
