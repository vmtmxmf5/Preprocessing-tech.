### 타이타닉 예제 살펴보기

``` sage
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('gadfly')
```

```sage
titanic = sns.load_dataset('titanic')
t = titanic.copy()
```

함수 전처리
```sage
t['survived'].sum()
t['age'].median()
```

*동일*한 전처리
```sage
t['pclass'].groupby(t['pclass']).count()
t['pclass'].value_counts()
```

### cut 사용법
```sage
k1 = [0, 18, 35, 60, 80]
k2 = ['아기', '청년', '장년', '중년']
t['age_cls'] = pd.cut(t['age'], bins=k1, labels=k2)
t['age_cls'].value_counts()
```

### 열 sort
t_sort = t.sort_values(by=['age'], ascending=False)