# Nobel Prize Analysis - Python Project
## Introduction
This analysis is just practice. I've improved a lot since my last python project and also learned how to better mask and so I wanted to work on that as well as getting better at aggragating data among other tricks I've picked up. 

The description of this guided project is here, taken from the project environment:

![Project Description](https://github.com/user-attachments/assets/cdd03fb3-7a34-49fe-a08e-24e1b3115652)


## Data Sources
The dataset used in this project was given to me by DataCamp in the Project section titled "Hypothesis Testing with Men's and Women's Soccer Matches". Unfortunately, the dataset only really exists inside of the project environment so I will be unable to share that here.

## Analysis Report
This section is a quick summary of my findings. You can find the full code and comments in the [Analysis](https://github.com/stgordillo/FIFA_python/blob/main/ANALYSIS.py).

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
You can find my visualizations for the the analysis in [Visualizations](https://github.com/stgordillo/FIFA_python/blob/main/VISUALIZATIONS.md).

RESULT
{'p_val': array([0.00510661]), 'result': 'reject'}
