import pandas as pd
from scipy import stats as st
import seaborn as sns
from numpy.random import RandomState
import streamlit as stream
import matplotlib.pyplot as plt

state = RandomState(42)

stream.title("Задание 1. Статистика")

data_upload = stream.file_uploader(label='Загрузить данные')

if data_upload is not None:
    data = pd.read_csv(data_upload, encoding='cp1251')
else:
    data = pd.read_csv('Статистика.csv', encoding='cp1251')
data
work_days = stream.slider('work_days', min_value=0, max_value=7, value=2)
age = stream.slider('age', min_value=25, max_value=60, value=35)

data['is_greater_than'] = data['Количество больничных дней'] > work_days
data = data.astype({'is_greater_than': 'int32'})

m = []
w = []
workers_older = []
workers_younger = []

for i in range(5000):
    m.append(data[data['Пол'] =='М'].sample(frac=1, replace=True, random_state=state)['is_greater_than'].mean())
    w.append(data[data['Пол'] =='Ж'].sample(frac=1, replace=True, random_state=state)['is_greater_than'].mean())
    workers_older.append(data[data['Возраст'] >= age].sample(frac=1, replace=True, random_state=state)['is_greater_than'].mean())
    workers_younger.append(data[data['Возраст'] < age].sample(frac=1, replace=True, random_state=state)['is_greater_than'].mean())

m = pd.Series(m)
w = pd.Series(w)
    
workers_older = pd.Series(workers_older)
workers_younger = pd.Series(workers_younger)
    
stream.title("Графики распределений")
    
stream.markdown('График распределения мужчин и женщин:')
fig = plt.figure(figsize=(10, 4))
ax = plt.axes(xlim=(0, 1), ylim=(0, 1250))
plt.title('Распределение вероятностей мужчин и женщин, которые пропустили дней: ' + str(work_days))
plt.xlabel("Вероятность пропуска")
plt.ylabel("Количество")
m.hist(color='green', alpha = 0.5, bins=20)
w.hist(color='blue', alpha = 0.5, bins=20)
ax.legend(['Мужчины', 'Женщины'])
stream.pyplot(fig)
    
stream.markdown('График распределения людей, старше и младше ' + str(age) + ' лет:')
fig = plt.figure(figsize=(10, 4))
ax = plt.axes(xlim=(0, 1), ylim=(0, 1250))
plt.title('Распределение вероятностей людей, старше и младше ' + str(age) + ' лет, которые пропустили дней: ' + str(work_days))
plt.xlabel("Вероятность пропуска")
plt.ylabel("Количество")
workers_older.hist(color='green', alpha = 0.5, bins=20)
workers_younger.hist(color='blue', alpha = 0.5, bins=20)
ax.legend(['Люди, достигшие ' + str(age) + ' лет', 'Люди, младше ' + str(age) + ' лет'])
stream.pyplot(fig)
    
stream.title("Проверка гипотез")
alpha = stream.slider('alpha (уровень значимости)', min_value=.01, max_value=.1, value=.05)
stream.markdown('**1-ая проверка гипотез:**')
stream.markdown('**H_0:** Количество больничных дней мужчин более ' + str(work_days) + ' дней = количество больничных дней женщин более ' + str(work_days) + ' дней')
stream.markdown('**H_a:** Количество больничных дней мужчин более ' + str(work_days) + ' дней > количество больничных дней женщин более ' + str(work_days) + ' дней')

results = st.ttest_ind(m, w, equal_var=False, alternative='greater')
stream.write('**t-критерий Стьюдента**:', results.statistic)
stream.write('**p-value** (Вероятность того, что мы отклоним нулевую гипотезу, когда она верна):', results.pvalue) 
if results.pvalue < alpha:
    stream.write('**ОТВЕРГАЕМ** нулевую гипотезу. Следовательно, принимаем альтернативную гипотезу.')
    stream.markdown('**Вывод:** Мужчины **ПРОПУСКАЮТ** в течение года более ' + str(work_days) + ' дней по болезни значимо чаще женщин')
else:
    stream.write('**НЕ ПОЛУЧИЛОСЬ ОТВЕРГНУТЬ** нулевую гипотезу')
    stream.markdown('**Вывод:** Мужчины **НЕ ПРОПУСКАЮТ** в течение года более ' + str(work_days) + ' дней по болезни значимо чаще женщин')
        
    
stream.markdown('**2-я проверка гипотез:**')
stream.markdown('**H_0:** Количество больничных дней более ' + str(work_days) + ' дней работников старше ' + str(age) + ' лет = количество больничных дней более ' + str(work_days) + ' дней работников моложе ' + str(age) + ' лет')
stream.markdown('**H_a:** Количество больничных дней более ' + str(work_days) + ' дней работников старше ' + str(age) + ' лет > количество больничных дней более ' + str(work_days) + ' дней работников моложе ' + str(age) + ' лет')
    
results = st.ttest_ind(workers_older, workers_younger, equal_var=False, alternative='greater')
stream.write('**t-критерий Стьюдента**:', results.statistic)
stream.write('**p-value** (Вероятность того, что мы отклоним нулевую гипотезу, когда она верна):', results.pvalue) 
if results.pvalue < alpha:
    stream.write('**ОТВЕРГАЕМ** нулевую гипотезу. Следовательно, принимаем альтернативную гипотезу.')
    stream.markdown('**Вывод:** Работники старше ' + str(age) + ' лет **ПРОПУСКАЮТ** в течение года более ' + str(work_days) + ' рабочих дней по болезни значимо чаще своих более молодых коллег.')
else:
    stream.write('**НЕ ПОЛУЧИЛОСЬ ОТВЕРГНУТЬ** нулевую гипотезу')
    stream.markdown('**Вывод:** Работники старше ' + str(age) + ' лет **НЕ ПРОПУСКАЮТ** в течение года более ' + str(work_days) + ' рабочих дней по болезни значимо чаще своих более молодых коллег.')
