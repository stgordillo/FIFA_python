# Start your code here!
import pandas as pd
import matplotlib.pyplot as plt
import pingouin

men = pd.read_csv('men_results.csv')
women = pd.read_csv('women_results.csv')

# Filtering the data for the date and tournament
men['date'] = pd.to_datetime(men['date'])
men_subset = men[(men['date'] > '2002-01-01') & (men['tournament'].isin(['FIFA World Cup']))]
women['date'] = pd.to_datetime(women['date'])
women_subset = women[(women['date'] > '2002-01-01') & (women['tournament'].isin(['FIFA World Cup']))]

# Create group and goals_scored columns
men_subset['group'] = 'men'
women_subset['group'] = 'women'
men_subset['goals_scored'] = men_subset['home_score'] + men_subset['away_score']
women_subset['goals_scored'] = women_subset['home_score'] + women_subset['away_score']

# Determine normality using histograms
men_subset['goals_scored'].hist()
plt.show()

# Goals scored is not normally distributed, so use Wilcoxon-Mann-Whitney test of two groups

# Comine women's and men's data and calculate goals scored in each match
both = pd.concat([women_subset, men_subset], axis=0, ignore_index=True)

# Transform the data for the pingouin Mann-Whitney U t-test/Wilcoxon-Mann-Whitney test
both_subset = both[['goals_scored', 'group']]
both_subset_wide = both_subset.pivot(columns = 'group', values = 'goals_scored')

# Perform right-tailed Wilcoxon-Mann-Whitney test with pingouin
results_pg = pingouin.mwu(x = both_subset_wide['women'], y = both_subset_wide['men'], alternative = 'greater')

# Extract p-value as a float
p_val = results_pg['p-val'].values

# Determine hypothesis test result using sig. level
if p_val <= 0.01:
    result = 'reject'
else:
    result = 'fail to reject'
    
result_dict = {'p_val': p_val, 'result': result}
print(result_dict)
