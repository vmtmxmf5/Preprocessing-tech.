### 타이타닉 예제 살펴보기

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('gadfly')

titanic = sns.load_dataset('titanic')
t = titanic.copy()
```

함수 전처리
```sage
t['survived'].sum()
t['age'].median()
t.groupby('pclass')['fare'].median()
```

**동일**한 전처리
```sage
t['pclass'].groupby(t['pclass']).count()
t.groupby('pclass')['pclass'].count()
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
```sage
t_sort = t.sort_values(by=['age'], ascending=False)
```

#### query 특정 level 값들만 선택
```sage
t.query("alive=='yes'").groupby('pclass').count()
t.query("alive=='yes'")['alive']
```
