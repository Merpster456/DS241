import pandas as pd

# Load the dataset
data = pd.read_csv("C:\\Users\\mepst\\Documents\\DS241\\hw4\\drug_data.csv")

# View the first few rows
print(data.head())


print(data.groupby('group').describe())
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Pre-treatment scores
sns.boxplot(x='group', y='pre_treatment_score', data=data)
plt.title('Pre-treatment Scores by Group')
plt.show()

# Post-treatment scores
sns.boxplot(x='group', y='post_treatment_score', data=data)
plt.title('Post-treatment Scores by Group')
plt.show()
"""

"""
sns.histplot(data=data, x='recovery_time', hue='group', kde=True)
plt.title('Recovery Time Distribution')
plt.show()
"""

"""
sns.countplot(x='side_effects', hue='group', data=data)
plt.title('Side Effects by Group')
plt.show()
"""


from scipy.stats import ttest_ind

# Split the data into two groups
new_drug_group = data[data['group'] == 'new_drug']['recovery_time']
placebo_group =  data[data['group'] == 'placebo']['recovery_time']

# Perform an independent t-test
t_stat, p_value = ttest_ind(new_drug_group, placebo_group)
#print(f"T-statistic: {t_stat}, P-value: {p_value}")

from scipy.stats import chi2_contingency

# Create a contingency table
contingency_table = pd.crosstab(data['group'], data['side_effects'])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)
#print(f"Chi-Square Statistic: {chi2}, P-value: {p}")

from statistics import mean
import numpy as np

# Compute the mean and standard error for both groups
mean_diff = mean(new_drug_group) - mean(placebo_group)
se_diff = np.sqrt(np.var(new_drug_group)/len(new_drug_group) + np.var(placebo_group)/len(placebo_group))

# 95% confidence interval
conf_interval = (mean_diff - 1.96 * se_diff, mean_diff + 1.96 * se_diff)
#print(f"95% Confidence Interval: {conf_interval}")


# Calculate the pooled standard deviation
pooled_std = np.sqrt((np.var(new_drug_group) + np.var(placebo_group)) / 2)

# Calculate Cohen's d
cohen_d = (np.mean(new_drug_group) - np.mean(placebo_group)) / pooled_std
print(f"Cohen's d: {cohen_d}")





