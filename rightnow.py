import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('gadfly')

## 데이터 준비
df = pd.read_excel('C:\\dd\\main.xlsx')

df2 = df[['EG', 'userate', 'name', 'C', 'humid', 'rain', 'solar', 'latitude', 'longitude', 'storage']].copy()

df2['trim_EG'] = df2['EG'] > 650
df2['trim_EG'] = df2[df2['EG'] > 650]
df2['trim_EG'] = df2['trim_EG'].apply(pd.to_numeric)

## 월 발전시간 = 발전량 / 용량
df2['time_EG'] = df2['EG'].div(df2.storage, axis=0)

df3 = df2[['EG', 'solar', 'trim_EG', 'time_EG','storage']].copy()

df3.dtypes
df3.count()

df3.columns = ['EG', 'Insolation', 'trim_EG', 'time_EG', 'Capacity']
df3['Use_ratio'] = df2['userate']

# 산포도
sns.regplot(x='Insolation', y='EG', data=df3)

df_tmp = df2['EG']
df_tmp.loc[df_tmp > 650] = 'Larger than 650'
df_tmp.loc[df_tmp != 'Larger than 650'] = 'Less than 650'
df3['Group'] = df_tmp

sns.lmplot(x='Insolation', y='EG', data=df3, hue='Group', palette=gg_palette)
plt.ylabel(None)
plt.title('Why is Solar Energy Uncorrelated with the Sum of Insolation?')




## 히트맵
mask = np.zeros_like(df3.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(df3.corr(),
            linewidth=0,
            cmap="YlGnBu",
            annot=True,
            )
plt.title('Correlation between Variables')



df2[df2['storage'] >= 3].count()

sns.barplot()

#################################
co = pd.Series([24, 36, 57, 109, 140, 166, 168, 174, 241, 264, 263, 262])
date = [x for x in range(2009, 2021)]
lst = list(map(str, date))


co.plot(kind='bar', color=gg_palette)
plt.xticks(ticks=np.arange(0,12),labels=['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], rotation=45)
plt.ylabel('# of Generation')
plt.title('The Number of Solar Generation')



#######################
fig, ax = plt.subplots(1, 1, figsize=(7, 7))

mask = np.zeros_like(df3.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(df3.corr(), 
            square=True, 
            mask=mask,
            linewidth=2.5, 
            vmax=0.4, vmin=-0.4, 
            cmap=cmap, 
            cbar=False,
            annot=True,
            ax=ax)

ax.set_yticklabels(ax.get_xticklabels(), fontfamily='serif', rotation = 0, fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), fontfamily='serif', rotation=90, fontsize=11)

ax.spines['top'].set_visible(True)

fig.text(0.97, 1, 'Correlation Heatmap Visualization', fontweight='bold', fontfamily='serif', fontsize=15, ha='right')    
fig.text(0.97, 0.92, 'Dataset : Titanic\nAuthor : Subin An', fontweight='light', fontfamily='serif', fontsize=12, ha='right')    

plt.tight_layout()
plt.show()



## Seasonal graph, Annual EG
df = df.set_index('date')
df['year'] = df.index.year
df['month'] = df.index.month

pivot = pd.pivot_table(df,
                       values = ['EG'],
                       index = ['month'],
                       columns = ['year'])

pivot.plot(color=gg_palette)
plt.xlabel('Month')
plt.xticks(range(1,13))
plt.ylabel('Generated Electricity')
plt.title('Average Solar Energy Production in a Month')
plt.legend(loc='center left', bbox_to_anchor=(0.96, 0.5), fontsize = 10)


pivot2 = pd.pivot_table(df, values=['EG'], index=['month'])
pivot2['month'] = pivot2.index

ax = sns.barplot(x='month', y='EG', data=pivot2,
                 palette=gg_palette)
plt.xlabel('Month')
plt.xticks(range(1, 13))
plt.ylabel('Generated Electricity')
plt.show()

pivot3 = pd.pivot_table(df,
                        values=['EG'],
                        index=['year'])
pivot3['year'] = pivot3.index


%matplotlib auto

sns.barplot(x='EG', y='year', data=pivot3,
            palette=gg_palette, orient='h')
plt.xlabel('Generated Electricity')
plt.ylabel(None)
plt.title('Annual Electricity Generation from Solar Energy in KOEN')


