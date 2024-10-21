# Nobel Prize Analysis - Python Project
## Introduction
This analysis is just practice. I've improved a lot since my last python project and also learned how to better mask and so I wanted to work on that as well as getting better at aggragating data among other tricks I've picked up. 

The description of this guided project is here:
You're working as a sports journalist at a major online sports media company, specializing in soccer analysis and reporting. You've been watching both men's and women's international soccer matches for a number of years, and your gut instinct tells you that more goals are scored in women's international football matches than men's. This would make an interesting investigative article that your subscribers are bound to love, but you'll need to perform a valid statistical hypothesis test to be sure!

While scoping this project, you acknowledge that the sport has changed a lot over the years, and performances likely vary a lot depending on the tournament, so you decide to limit the data used in the analysis to only official FIFA World Cup matches (not including qualifiers) since 2002-01-01.

You create two datasets containing the results of every official men's and women's international football match since the 19th century, which you scraped from a reliable online source. This data is stored in two CSV files: women_results.csv and men_results.csv.

The question you are trying to determine the answer to is:

    Are more goals scored in women's international soccer matches than men's?

You assume a 10% significance level, and use the following null and alternative hypotheses:

H_0: The mean number of goals scored in women's international soccer matches is the same as men's.

H_A: The mean number of goals scored in women's international soccer matches is greater than men's.

## Data Sources
The dataset used in this project was retrieved from a Kaggle dataset found here: [Nobel Prize Dataset](https://www.kaggle.com/datasets/imdevskp/nobel-prize).

This data has both raw and cleaned versions of a csv, since this was practice for filtering, etc and not for cleaing, I opted to start from the cleaned dataset this time. It contains demographic data for winners, years awarded, affliations, etc which we can use for our insights.

## Analysis Report
This section is a quick summary of my findings. You can find the full code and comments in the [Analysis](https://github.com/stgordillo/nobel_python/blob/main/ANALYSIS.py).

### Initial
For this practice analysis, I wanted to practice more with looking for the answers to "business questions" or rather have some sort of goal that I initially give myself to try and solve. Here, I had five questions in total to find in the dataset:
What is the most commonly awarded gender and birth country?
Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
Which decade and Nobel Prize category combination had the highest proportion of female laureates?
Who was the first woman to receive a Nobel Prize, and in what category?
Which individuals or organization have won more than one Nobel Prize throughout the years?

I also have recently taken a small course learning more about seaborn so I loaded up the following packages for this analysis: pandas, matplotlib, seaborn and numpy. 

### Exploration
Exploration wasn't too involved in coding, but I did sift through the dataset for awhile so I could determine what my five questions would be that I couldn't get the answers to just from looking at the data in a table. In this case, I just used .head() to look at column names and get an idea of what I wanted to look into and came to the questions above. 

### Findings
Looking at my first question, "What is the most commonly awarded gender and birth country?" I just used .mode() on the columns of 'sex' and 'birth_country' to find the answers as Male and United States of America respectively. 

The second question, "Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?" I created a new column that had a boolean value if the person listed there was born in America or not, then I created a second column that "bins" the years into decades and finally I grouped the data by decades and found the mean of US winners by decade and found the max to find the the decade with the most being 2000s. I also used a relplot with sns to visualize this information. 

Third question, "Which decade and Nobel Prize category combination had the highest proportion of female laureates?" was found using something similar as my last question, creating a boolean column for female winners, using groupby and mean to find the average per decade and category, and finding the top decade with max. Then turned into into a dictionary and finally plotted the data with another relplot in sns. The finding was 2020 in Literature with a proportion of 68 winners. 

Question 4, "Who was the first woman to receive a Nobel Prize, and in what category?", I filtered the dataframe for only female winners, filtered down to the minimum (earliest) year and extracted her name and category being the famous Madame Curie in Physics. 

Finally the last question was "Which individuals or organization have won more than one Nobel Prize throughout the years?" and I obtained that information by using the full_name column to count the values of unique names. Then I used filtering and indexing to find anyone who's named appeared more than once, changing the index into a list to find 6 returners to getting a Nobel Prize. The Red Cross and the Office of the UN High Commissioner for Refugees being the returning organizations and the returning individuals being Linus Carl Pauling, John Bardeen, Frederick Sanger, and Marie Curie.

## Visualizations
You can find my visualizations for the the analysis in [Visualizations](https://github.com/stgordillo/nobel_python/blob/main/VISUALIZATIONS.md).

RESULT
{'p_val': array([0.00510661]), 'result': 'reject'}
