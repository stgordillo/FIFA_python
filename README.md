# FIFA Men's and Women's Soccer - Python Project
## Introduction
This analysis is more practice as I finish my final semester at university. This project had me using a lot of subsetting and some statistics. 

The description of this guided project is here, taken from the project environment:

![Project Description](https://github.com/user-attachments/assets/cdd03fb3-7a34-49fe-a08e-24e1b3115652)


## Data Sources
The dataset used in this project was given to me by DataCamp in the Project section titled "Hypothesis Testing with Men's and Women's Soccer Matches". Unfortunately, the dataset only really exists inside of the project environment so I will be unable to share that here.

## Analysis Report
This section is a quick summary of my findings. You can find the full code and comments in the [Analysis](https://github.com/stgordillo/FIFA_python/blob/main/ANALYSIS.py).

### Initial
This practice analysis was guided from DataCamp and so already had a question it wanted me to answer which was "Are more goals scored in women's international soccer matches than men's?" I would need to find the appropriate hypothesis test and find the p-value. They told me to use a 10% confidence level and also the null hypothesis being "The mean number of goals scored in women's international soccer matches is the same as men's" and the alternative hypothesis being "The mean number of goals scored in women's international soccer matches is greater than men's".

I used the packages pandas, matplotlib and pingouin for this analysis. 

### Exploration
After loading up the two datasets, one for men's soccer and one for women's, I used .head() & .tail(), .shape(), .describe(), and checked .value_counts() for a few columns I thought would be pertinent to the analysis, namely date, home_score & away_score.

### Method
I started by filtering my data for matches from 2002 onwards as well as matches in the FIFA World Cup. Additionally, there was no total goals scored column, just one for home and one for away games, so I needed to combine those scores together in each dataset into goals_scored. Once that was done, I created a histogram so I could see the distribution and help determine what hypothesis test I needed to use.

I ended up using the Wilcoxon-Mann-Whitney test since the scores weren't distributed normally. To prepare for it, I concatenated the two datasets together and created a wide dataset. Here I used pingouin in order to create the right-tailed Wilcoxon-Mann-Whitney test, which took me a few tries to get settled right, as I previously had little practice using this kind of analysis. 

After this I found my p-value (0.00510661) which is below the significance level and used a if-else function to determine the p-value and result, which rejected my null hypothesis. 

## Visualizations
You can find my visualizations for the the analysis in [Visualizations](https://github.com/stgordillo/FIFA_python/blob/main/VISUALIZATIONS.md).

## RESULT
{'p_val': array([0.00510661]), 'result': 'reject'}
