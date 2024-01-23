"""
Authors:      Suze Frikkee, Luca Pouw, Eva Nieuwenhuis
University:   UvA
Course:       Project Computational Science
Student ID's: 14773279 , 15159337, 13717405
Description:  In this code the functions are given to do statistical tests in
visualisation.py with the data from the runned simulations.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro
from scipy import stats
import matplotlib.patches as patches

def significant_test_school_size(df):
    """Function that determines if there is a significant difference in killed
    herring between a large and small school in environment with and without rocks.

    Parameters:
    -----------
    df: Dataframe
        Datafframe with the values obtaint from the simulated experiments.
    """
    df['Proportion killed herring'] = pd.to_numeric(df['Proportion killed herring'], errors='coerce')

    # Extract the killing values for the small and larg school
    values_small_school_rocks = df.loc[(df['School size'] == 200) & (df['Rocks'] == 'yes'), 'Proportion killed herring']
    values_large_school_rocks = df.loc[(df['School size'] == 400) & (df['Rocks'] == 'yes'), 'Proportion killed herring']
    values_small_school_no_rocks = df.loc[(df['School size'] == 200) & (df['Rocks'] == 'no'), 'Proportion killed herring']
    values_large_school_no_rocks = df.loc[(df['School size'] == 400) & (df['Rocks'] == 'no'), 'Proportion killed herring']

    # Determine if the data is normally distributed
    statistic_small_school_rocks, p_value_small_school_rocks = shapiro(values_small_school_rocks)
    statistic_large_school_rocks, p_value_large_school_rocks = shapiro(values_large_school_rocks)
    statistic_small_school_no_rocks, p_value_small_school_no_rocks = shapiro(values_small_school_no_rocks)
    statistic_large_school_no_rocks, p_value_large_school_no_rocks = shapiro(values_large_school_no_rocks)
    print(df)
    print('rocks', values_small_school_rocks, values_large_school_rocks)
    print('no rocks', values_small_school_no_rocks, values_large_school_no_rocks)
    # Influence school size in environment with rocks. Check if both data is normally
    # distributed to determine the statistic test
    if  p_value_large_school_rocks >= 0.05 and p_value_small_school_rocks >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_small_school_rocks, values_large_school_rocks)
        print(f'Small vs large school in environment with rocks. T-Statistic: {t_statistic}, p-Value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_small_school_rocks, values_large_school_rocks)
        print(f'Small vs large school in environment with rocks. Mann-Whitney U Statistic: {mw_statistic}, p-Value: {p_value}')

    # Influence school size in environment without rocks. Check if both data is normally
    # distributed to determine the statistic test
    if  p_value_large_school_no_rocks >= 0.05 and p_value_small_school_no_rocks >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_small_school_no_rocks, values_large_school_no_rocks)
        print(f'Small vs large school in environment without rocks. T-Statistic: {t_statistic}, p-Value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_small_school_no_rocks, values_large_school_no_rocks)
        print(f'Small vs large school in environment without rocks. Mann-Whitney U Statistic: {mw_statistic}, p-Value: {p_value}')


def significant_test_close(df):
    """Function that determines if there is a significant difference in herring
    within the perception distance of 6 when the perception distance changes and
    when a preadator gets introduced. It is tested in an envionment without rocks.

    Parameters:
    -----------
    df: Dataframe
        Datafframe with the values obtaint from the simulated experiments.
    """
    df['Times within separation distance'] = pd.to_numeric(df['Times within separation distance'], errors='coerce')

    # Extract the killing values for the different environments
    values_no_p_6_no_r = df.loc[(df['Predator and separation distance'] == 'no p + no r + s d = 6'), 'Times within separation distance']
    values_no_p_6_r = df.loc[(df['Predator and separation distance'] == 'no p + 20 r + s d = 6'), 'Times within separation distance']
    values_p_6_no_r = df.loc[(df['Predator and separation distance'] == '2 p + no r + s d = 6'), 'Times within separation distance']
    values_no_p_3_no_r = df.loc[(df['Predator and separation distance'] == 'no p + no r + s d = 3'), 'Times within separation distance']
    values_no_p_12_no_r = df.loc[(df['Predator and separation distance'] == 'no p + no r + s d = 12'), 'Times within separation distance']

    # Determine if the data is normally distributed
    statistic_no_p_6_no_r, p_value_no_p_6_no_r = shapiro(values_no_p_6_no_r)
    statistic_no_p_6_r, p_value_no_p_6_r = shapiro(values_no_p_6_r)
    statistic_p_6_no_r, p_value_p_6_no_r = shapiro(values_p_6_no_r)
    statistic_no_p_3_no_r, p_value_no_p_3_no_r = shapiro(values_no_p_3_no_r)
    statistic_no_p_12_no_r, p_value_no_p_12_no_r = shapiro(values_no_p_12_no_r)

    # Determine if introducing predators has significant influence. Check if both data
    # is normally distributed to determine the statistic test
    if p_value_no_p_6_no_r >= 0.05 and p_value_p_6_no_r >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_no_p_6_no_r, values_p_6_no_r)
        print(f'Effect introduction predators. T-Statistic: {t_statistic}, p-value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_no_p_6_no_r, values_p_6_no_r)
        print(f'Effect introduction predators. Mann-Whitney U Statistic: {mw_statistic}, p-value: {p_value}')

    # Determine if introducing rocks has significant influence. Check if both data
    # is normally distributed to determine the statistic test
    if p_value_no_p_6_no_r >= 0.05 and p_value_no_p_6_r >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_no_p_6_no_r, values_no_p_6_r)
        print(f'Effect introduction rocks. T-Statistic: {t_statistic}, p-value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_no_p_6_no_r, values_no_p_6_r)
        print(f'Effect introduction rocks. Mann-Whitney U Statistic: {mw_statistic}, p-value: {p_value}')

    # Determine if a lower seperation distance has a significant influence. Check if
    # both data is normally distributed to determine the statistic test
    if p_value_no_p_6_no_r >= 0.05 and p_value_no_p_3_no_r >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_no_p_6_no_r, values_no_p_3_no_r)
        print(f'Effect smaller separation distance. T-Statistic: {t_statistic}, p-Value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_no_p_6_no_r, values_no_p_3_no_r)
        print(f'Effect smaller separation distance. Mann-Whitney U Statistic: {mw_statistic}, p-value: {p_value}')

    # Determine if a higher seperation distance has a significant influence. Check if
    # both data is normally distributed to determine the statistic test
    if p_value_no_p_6_no_r >= 0.05 and p_value_no_p_12_no_r >= 0.05:
        t_statistic, p_value = stats.ttest_ind(values_no_p_6_no_r, values_no_p_12_no_r)
        print(f'Effect larger separation distance. T-Statistic: {t_statistic}, p-Value: {p_value}')
    else:
        mw_statistic, p_value = stats.mannwhitneyu(values_no_p_6_no_r, values_no_p_12_no_r)
        print(f'Effect larger separation distance. Mann-Whitney U Statistic: {mw_statistic}, p-value: {p_value}')