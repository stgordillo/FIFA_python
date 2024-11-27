import pandas as pd
import matplotlib.pyplot as plt
import pingouin

# Importing both datasets
men = pd.read_csv('men_results.csv')
women = pd.read_csv('women_results.csv')

# Exploring datasets
men.head()
men.tail()
men.shape()
men.describe()
print(men['date'].value_counts())
print(men['away_score'].value_counts())
print(men['home_score'].value_counts())

women.head()
women.tail()
women.shape()
women.describe()
print(women['date'].value_counts())
print(women['away_score'].value_counts())
print(women['home_score'].value_counts())

# Filtering the data for the date and tournament
men['date'] = pd.to_datetime(men['date'])
men_subset = men[(men['date'] > '2002-01-01') & (men['tournament'].isin(['FIFA World Cup']))]
women['date'] = pd.to_datetime(women['date'])
women_subset = women[(women['date'] > '2002-01-01') & (women['tournament'].isin(['FIFA World Cup']))]

# Creating group and goals_scored columns
men_subset['group'] = 'men'
women_subset['group'] = 'women'
men_subset['goals_scored'] = men_subset['home_score'] + men_subset['away_score']
women_subset['goals_scored'] = women_subset['home_score'] + women_subset['away_score']

# Determining hypothesis testing needed using histograms
men_subset['goals_scored'].hist()
plt.show()

# Found that the goals scored was not normally distributed but had a right-tail, which should mean I need to use
# the Wilcoxon-Mann-Whitney test 

# Concatenating men's and women's datasets and then figure out the goals scored for each match
both = pd.concat([women_subset, men_subset], axis=0, ignore_index=True)

# Transforming the dataset for the pingouin Wilcoxon-Mann-Whitney test
both_subset = both[['goals_scored', 'group']]
both_subset_wide = both_subset.pivot(columns = 'group', values = 'goals_scored')

# Testing the hypothesis test
results_pg = pingouin.mwu(x = both_subset_wide['women'], y = both_subset_wide['men'], alternative = 'greater')

# Extracting p-value for use in if-else function
p_val = results_pg['p-val'].values

# Determining hypothesis testing using the significance level
if p_val <= 0.01:
    result = 'reject'
else:
    result = 'fail to reject'
    
result_dict = {'p_val': p_val, 'result': result}
print(result_dict)
