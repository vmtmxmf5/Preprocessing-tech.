
import pandas as pd

## 날씨 데이터
wth = pd.read_csv('C:\\dd\\my2.csv', encoding='cp949')
wth.columns = ['code', 'name', 'date', 'C', 'humid', 'rain', 'cloud', 'solar']
wth2 = wth[wth['name'] != '문경'].copy()

## datetime으로 통일
wth2['date'] = wth2['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m'))

## 탑선-광주 분리
wth3 = wth2[wth2['name'] == '광주']

## 영흥-인천 분리
wth4 = wth2[wth2['name'] == '인천']


## 발전량 데이터
df = pd.read_excel('C:\\dd\\한국남동발전_발전실적 (1).xls')
df.columns = ['loc', 'plant', 'date', 'storage', 'EG', 'ther', 'userate', 'generator']
df2 = df[df['generator'] == '태양력'].copy()

## datetime으로 통일
df2['date'] = df2['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m'))
df2 = df2.sort_values('date')

## 예천태양광, 영흥태양광5 삭제
dlt = df2['loc'] != ('예천태양광' and '영흥태양광#5')
df3 = df2[dlt]

# 날씨 추가
## 탑선태양광에 날씨 추가
df4 = df3[df3['loc'] == '탑선태양광']
tmp = pd.merge(df4, wth3, on='date', how='left')

## 영흥태양광에 날씨 추가
df5 = df3[df3['loc'] == '영흥태양광']
tmp1 = pd.merge(df5, wth4, on='date', how='left')

df6 = df3[df3['loc'] == '영흥태양광 #3']
tmp2 = pd.merge(df6, wth4, on='date', how='left')

## 탑선 + 영흥
temp = tmp.append([tmp1, tmp2])
ee = pd.merge(df3, temp, how='left')