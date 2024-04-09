import pandas as pd


def get_retracted_articles(retraction_file):
    file = pd.read_csv(retraction_file, usecols=['RetractionDate', 'RetractionNature'])
    retracted_articles = file.loc[file['RetractionNature'] == 'Retraction']
    return retracted_articles


def get_2023_and_earlier(retracted_articles):
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

