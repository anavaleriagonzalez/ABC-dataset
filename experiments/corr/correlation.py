import scipy.stats
import pandas as pd 
import numpy as np 
import argparse
import matplotlib.pyplot as plt
from operator import itemgetter
from numpy.polynomial import Polynomial



stats = pd.read_csv("../mt_outputs/stats_ungrouped.csv", sep="\t")
stats_en = pd.read_csv("../mt_outputs/occupations-stats.tsv", sep="\t")["bls_pct_female"].tolist()
percent_da = stats["Perc-da"].tolist()
percent_sv = stats["Perc-sv"].tolist()
percent_ru = stats["Perc-ru"].tolist()
#percent_en = [float(item) for item in stats["Perc-en"].tolist()]

sv = pd.read_csv("sv.csv")
da = pd.read_csv("da.csv")
ru = pd.read_csv("ru.csv")
zh = pd.read_csv("zh.csv")

mean_sv = sv.groupby(['occs']).mean()
mean_da = da.groupby(['occs']).mean()
mean_ru = ru.groupby(['occs']).mean()
mean_zh = zh.groupby(['occs']).mean()

def get_valid(means, percentage):

    new_means = []
    new_percentages = []
    bins = []
    for i in range(len(means)):
        try:
            int(percentage[i])
            new_means.append(means[i])
            new_percentages.append(percentage[i])
            
            if percentage[i]  < 20:
                bins.append(means[i],1)
            elif percentage[i] >=20  and  percentage[i]  <40:
                bins.append(means[i],2)
            elif percentage[i] >=40  and  percentage[i]  <60:
                bins.append(means[i],3)
            elif percentage[i] >=60  and  percentage[i]  <80:
                bins.append(means[i],4)
            else:
                bins.append(means[i],5)
       
        except Exception:
            pass

    return new_means, new_percentages, bins

print("correlations to US stats")
new_sv, per_sv , binssv = get_valid(mean_sv['differences'].tolist(), stats_en)
print("US STATS-SV")
print(scipy.stats.pearsonr(new_sv, per_sv))
mean_sv['bins'] = binssv
print(scipy.stats.pearsonr(mean_sv.groupby(['bins']).mean()['differences'].tolist(), [1,2,3,4,5]))

print("--------------")
new_da, per_da, binsda = get_valid(mean_da['differences'].tolist(), stats_en)
print("US STATS-DA")
print(scipy.stats.pearsonr(new_da, per_da))
mean_da['bins'] = binsda
print(scipy.stats.pearsonr(mean_da.groupby(['bins']).mean()['differences'].tolist(), [1,2,3,4,5]))

print("--------------")
new_ru, per_ru, binsru = get_valid(mean_ru['differences'].tolist(), stats_en)
print("US STATS-RU")
print(scipy.stats.pearsonr(new_ru, per_ru))
mean_ru['bins'] = binsru
print(scipy.stats.pearsonr(mean_ru.groupby(['bins']).mean()['differences'].tolist(), [1,2,3,4,5]))


print("--------------")
new_zh, per_zh, binszh = get_valid(mean_zh['differences'].tolist(), stats_en)
print("US STATS-ZH")
print(scipy.stats.pearsonr(new_zh, per_zh))


mean_zh['bins'] = binszh

print(scipy.stats.pearsonr(mean_zh.groupby(['bins']).mean()['differences'].tolist(), [1,2,3,4,5]))

print("--------------")


print("############################")
print("correlations to NATIONAL stats")

new_sv, per_sv , binssv = get_valid(mean_sv['differences'].tolist(), percent_sv)
print("NAT STATS-SV")
print(scipy.stats.pearsonr(new_sv, per_sv))

new_df1 = pd.DataFrame()
new_df1['bins'] = binssv
new_df1['diff'] = new_sv
new_df1['perc'] = per_sv


print(scipy.stats.pearsonr(new_df1.groupby(['bins']).mean()['diff'].tolist(), [1,2,3,4,5]))


print("--------------")
print("US STATS-DA")
new_da, per_da, binsda = get_valid(mean_da['differences'].tolist(), percent_da)
print(scipy.stats.pearsonr(new_da, per_da))


new_df2 = pd.DataFrame()
new_df2['bins'] = binsda
new_df2['diff'] = new_da
new_df2['perc'] = per_da


print(scipy.stats.pearsonr(new_df2.groupby(['bins']).mean()['diff'].tolist(), [1,2,3,4,5]))

print("--------------")
new_ru, per_ru, binsru = get_valid(mean_ru['differences'].tolist(), percent_ru)
print("US STATS-RU")
print(scipy.stats.pearsonr(new_ru, per_ru))


new_df3 = pd.DataFrame()
new_df3['bins'] = binsru
new_df3['diff'] = new_ru
new_df3['perc'] = per_ru


print(scipy.stats.pearsonr(new_df3.groupby(['bins']).mean()['diff'].tolist(), [1,2,3,4,5]))

print("--------------")
new_zh, per_zh, binszh = get_valid(mean_zh['differences'].tolist(), stats_zn)
print("NAT STATS-ZH")
print(scipy.stats.pearsonr(new_zh, per_zh))


mean_zh['bins'] = binszh

print(scipy.stats.pearsonr(mean_zh.groupby(['bins']).mean()['differences'].tolist(), [1,2,3,4,5]))
