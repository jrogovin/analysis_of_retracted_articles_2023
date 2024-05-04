# Analysis of Retracted Articles in 2023
The goal of this project is to expand on the work done by Van Noorden (2023). This article argues that retraction rates in 2023 are on the rise, citing a large number of retractions from the publisher, Hindawi, and breaks down retraction by country. The specific goals of this project are to take Van Noorden's work further by analyzing retraction by publisher, year, retraction reason, author, country, and time from original publication to retraction notice. In addition I propose several hypotheses:
  1. Overall Retraction Rates: Retraction rates have increased in 2023 from previous years.
  2. Reason for Retraction: The main reason for retraction is scientific misconduct.
  3. Author Group Size: Previous studies (https://dl.acm.org/doi/10.1007/s11192-021-04125-4) have shown that the larger the group of authors, the lower the rate of retraction. I will study team size and retraction rate by year. My hypothesis is that team size versus retraction rate has stayed consistent over time and that the larger the team size, the lower the retraction rate.
  4. Time from publication to retraction: There is about a 2 year lag from publication to retraction.

## Dependencies
  Pandas
  Counter from Collections
  Matplotlib.pyplot

## How to run
There is a pycharm module for each hypothesis but these do not need to be run. In order to run the program, you can run the main.ipynb file to see the visualizations.

## Hypothesis 1 Results
Aside from a record number of retractions in 2010 due to scientific misconduct, the graph shows an overall upward trajectory of retractions since 2000. The last bar in the graph is 2024 and is incomplete, since this analysis is being completed in April 2024.

## Hypothesis 2 Results
We can see that scientific misconduct is not explicitly mentioned until the 21st instance in the counter. There are many reasons that also indicate misconduct such as plagiarism or "euphemisms for plagiarism". 
  Retraction due to misconduct by author has generally increased over time but was actually lower in 2023. A big factor here is probably due to there being many retraction reasons that encompass misconduct but do not explicitly say misconduct.

## Hypothesis 3 Results
Retractions decrease overall the higher the author group size gets, with the exception of one author to two authors.

## Hypothesis 4 Results
The majority of papers have been retracted within 2 years from the publication date.


