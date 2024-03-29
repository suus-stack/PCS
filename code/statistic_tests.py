
"""
Authors:      Suze Frikkee, Luca Pouw, Eva Nieuwenhuis
University:   UvA
Course:       Project Computational Science
Student ID's: 14773279 , 15159337, 13717405
Description:  In this code the functions are given to do statistical tests in
              visualisation.py with the data from the runned simulations.
"""
import numpy as np
import pandas as pd
import matplotlib.patches as patches
from scipy.stats import shapiro, ttest_rel, wilcoxon

def significant_test_school_size(df):
    """Function that determines if there is a significant difference in killed
    herring between a large and small school in environments with and without rocks.

    Parameters:
    -----------
    df: Dataframe
        Datafframe with the values obtained from the simulated experiments.
    """
    df['Proportion killed herring'] = pd.to_numeric(df['Proportion killed herring'], \
                                                                    errors='coerce')

    # Extract the killing values for the small and large school with and without rocks
    v_small_school_rocks = df.loc[(df['School size'] == 200) & (df['Rocks'] == \
                                            'yes'), 'Proportion killed herring']
    v_large_school_rocks = df.loc[(df['School size'] == 400) & (df['Rocks'] == \
                                            'yes'), 'Proportion killed herring']
    v_small_school_no_rocks = df.loc[(df['School size'] == 200) & (df['Rocks'] == \
                                                'no'), 'Proportion killed herring']
    v_large_school_no_rocks = df.loc[(df['School size'] == 400) & (df['Rocks'] == \
                                                'no'), 'Proportion killed herring']

    # Determine if the data is normally distributed
    _, p_value_small_school_rocks = shapiro(v_small_school_rocks)
    _, p_value_large_school_rocks = shapiro(v_large_school_rocks)
    _, p_value_small_school_no_rocks = shapiro(v_small_school_no_rocks)
    _, p_value_large_school_no_rocks = shapiro(v_large_school_no_rocks)

    # Influence of school size in an environment with rocks.
    if  p_value_large_school_rocks >= 0.05 and p_value_small_school_rocks >= 0.05:
        t_statistic, p_value = ttest_rel(v_small_school_rocks, v_large_school_rocks)
        print(f'''Small vs large school in an environment with rocks; t-statistic:
                {t_statistic}, p-Value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_small_school_rocks, v_large_school_rocks)
        print(f'''Small vs large school in an environment with rocks; Wilcoxon
                 statistic: {w_statistic}, p-Value: {p_value}''')

    # Influence of school size in an environment without rocks.
    if  p_value_large_school_no_rocks >= 0.05 and p_value_small_school_no_rocks >= 0.05:
        t_statistic, p_value = ttest_rel(v_small_school_no_rocks, v_large_school_no_rocks)
        print(f'''Small vs large school in an environment without rocks; t-statistic:
                {t_statistic}, p-Value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_small_school_no_rocks, v_large_school_no_rocks)
        print(f'''Small vs large school in an environment without rocks; Wilcoxon
                statistic: {w_statistic}, p-Value: {p_value}''')


def significant_test_close(df):
    """Function that determines if there is a significant difference in herring within
    the original perception distance of 6 (density) when the perception distance
    changes, when more predators gets introduced or when rocks get introduced.

    Parameters:
    -----------
    df: Dataframe
        Dataframe with the values obtained from the simulated experiments.
    """
    df['Times within separation distance'] = pd.to_numeric(df[\
                            'Times within separation distance'], errors='coerce')

    # Extract the killing values for the different conditions
    v_1_p_6_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 6'), \
                                        'Times within separation distance']
    v_1_p_6_r = df.loc[(df['Conditions'] == '1 p + 20 r + s d = 6'), \
                                        'Times within separation distance']
    v_4_p_6_no_r = df.loc[(df['Conditions'] == '4 p + no r + s d = 6'), \
                                        'Times within separation distance']
    v_1_p_3_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 3'), \
                                        'Times within separation distance']
    v_1_p_12_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 12'), \
                                        'Times within separation distance']

    # Determine if the data is normally distributed
    statistic_1_p_6_no_r, p_value_1_p_6_no_r = shapiro(v_1_p_6_no_r)
    statistic_1_p_6_r, p_value_1_p_6_r = shapiro(v_1_p_6_r)
    statistic_4_p_6_no_r, p_value_4_p_6_no_r = shapiro(v_4_p_6_no_r)
    statistic_1_p_3_no_r, p_value_1_p_3_no_r = shapiro(v_1_p_3_no_r)
    statistic_1_p_12_no_r, p_value_1_p_12_no_r = shapiro(v_1_p_12_no_r)

    # Determine if introducing predators has a significant influence on the density
    if p_value_1_p_6_no_r >= 0.05 and p_value_4_p_6_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_4_p_6_no_r)
        print(f'''Effect introduction predators on the density; t-statistic:
               {t_statistic}, p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_4_p_6_no_r)
        print(f'''Effect introduction predators on the density; Wilcoxon statistic:
                {w_statistic}, p-value: {p_value}''')

    # Determine if introducing rocks has a significant influence on the density
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_6_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_6_r)
        print(f'''Effect introduction rocks on density; t-statistic: {t_statistic},
                p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_6_r)
        print(f'''Effect introduction rocks on the density; Wilcoxon statistic:
                {w_statistic}, p-value: {p_value}''')

    # Determine if a lower separation distance has a significant influence on the density
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_3_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_3_no_r)
        print(f'''Effect smaller separation distance on the density; t-statistic:
                {t_statistic}, p-Value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_3_no_r)
        print(f'''Effect smaller separation distance on the density; Wilcoxon
                statistic: {w_statistic}, p-value: {p_value}''')

    # Determine if a higher separation distance has a significant influence on the density
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_12_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_12_no_r)
        print(f'''Effect larger separation distance on the density; t-statistic:
                {t_statistic}, p-Value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_12_no_r)
        print(f'''Effect larger separation distance on the density; Wilcoxon statistic:
                {w_statistic}, p-value: {p_value}''')


def significant_test_killed(df):
    """Function that determines if there is a significant difference in the number
    of killed herring when the perception distance changes, when more predators gets
    introduced or when rocks get introduced.

    Parameters:
    -----------
    df: Dataframe
        Dataframe with the values obtained from the simulated experiments.
    """
    df['Killed herring'] = pd.to_numeric(df['Killed herring'], errors='coerce')

    # Extract the killing values for the different conditions
    v_1_p_6_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 6'), 'Killed herring']
    v_1_p_6_r = df.loc[(df['Conditions'] == '1 p + 20 r + s d = 6'), 'Killed herring']
    v_4_p_6_no_r = df.loc[(df['Conditions'] == '4 p + no r + s d = 6'), 'Killed herring']
    v_1_p_3_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 3'), 'Killed herring']
    v_1_p_12_no_r = df.loc[(df['Conditions'] == '1 p + no r + s d = 12'), 'Killed herring']

    # Determine if the data is normally distributed
    statistic_1_p_6_no_r, p_value_1_p_6_no_r = shapiro(v_1_p_6_no_r)
    statistic_1_p_6_r, p_value_1_p_6_r = shapiro(v_1_p_6_r)
    statistic_4_p_6_no_r, p_value_4_p_6_no_r = shapiro(v_4_p_6_no_r)
    statistic_1_p_3_no_r, p_value_1_p_3_no_r = shapiro(v_1_p_3_no_r)
    statistic_1_p_12_no_r, p_value_1_p_12_no_r = shapiro(v_1_p_12_no_r)

    # Determine if introducing predators has an influence on the killing rate
    if p_value_1_p_6_no_r >= 0.05 and p_value_4_p_6_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_4_p_6_no_r)
        print(f'''Effect introduction predators on the killing rate; t-statistic:
                {t_statistic}, p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_4_p_6_no_r)
        print(f'''Effect introduction predators on the killing rate; Wilcoxon
                statistic: {w_statistic}, p-value: {p_value}''')

    # Determine if introducing rocks has an influence on the killing rate
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_6_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_6_r)
        print(f'''Effect introduction rocks on the killing rate; t-statistic:
                {t_statistic}, p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_6_r)
        print(f'''Effect introduction rocks on the killing rate; Wilcoxon statistic:
                {w_statistic}, p-value: {p_value}''')

    # Determine if a lower separation distance has an influence on the killing rate
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_3_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_3_no_r)
        print(f'''Effect smaller separation distance on the killing rate; t-statistic:
                {t_statistic}, p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_3_no_r)
        print(f'''Effect smaller separation distance on the killing rate; Wilcoxon
                statistic: {w_statistic}, p-value: {p_value}''')

    # Determine if a higher separation distance has an influence on the killing rate
    if p_value_1_p_6_no_r >= 0.05 and p_value_1_p_12_no_r >= 0.05:
        t_statistic, p_value = ttest_rel(v_1_p_6_no_r, v_1_p_12_no_r)
        print(f'''Effect larger separation distance on the killing rate; t-statistic:
                {t_statistic}, p-value: {p_value}''')
    else:
        w_statistic, p_value = wilcoxon(v_1_p_6_no_r, v_1_p_12_no_r)
        print(f'''Effect larger separation distance on the killing rate; Wilcoxon
                statistic: {w_statistic}, p-value: {p_value}''')


def significant_test_boidsrules(data):
    """Function that determines if there is a significant difference in herring
    killing rate when one of the Boid rules is emphasised.

    Parameters:
    -----------
    data: Dataframe
        Datafframe with the values obtaint from the simulated experiments.
    """
    # Perform tests for each pair
    comparison_pairs = [('no weighted boid rules', 'weighted separation rule'),
                        ('no weighted boid rules', 'weighted alignment rule'),
                        ('no weighted boid rules', 'weighted cohesion rule')]

    for group1_name, group2_name in comparison_pairs:
        group1_data = data[group1_name]
        group2_data = data[group2_name]

        # Check if the data is normally distributed
        normality_group2 = shapiro(group2_data).pvalue >= 0.05

        if any(group1_data) and any(group2_data) and normality_group2:
            # Perform paired t-tests
            t_stat, p_value = ttest_rel(group1_data, group2_data)

            # Print the results of the paired t-test
            print(f'''Paired t-test between "{group1_name}" and "{group2_name}":
                    t-statistic = {t_stat}, p-value = {p_value}''')

        else:
            # Perform Mann-Whitney U test
            statistic, p_value_wilcoxon = wilcoxon(group1_data, group2_data,
                                                        alternative='two-sided')

            # Print the results for wilcoxon test
            print(f'''Wilcoxon test between "{group1_name}" and "{group2_name}":
                    Wilcoxon statistic = {statistic}, p-value = {p_value_wilcoxon}''')
