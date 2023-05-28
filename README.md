# MTech
## Задание 1. (Статистика). Постановка задачи

Руководство компании обратило внимание на то, что сотрудники старше 35 лет болеют чаще, чем более молодые сотрудники. Кроме этого, среди мужчин количество пропусков рабочих дней в связи с больничным выше, чем среди женщин. В связи с этой ситуацией, руководство организации планирует ввести дополнительные медицинские осмотры среди групп риска. 
Вам необходимо проверить следующие гипотезы:
1)	Мужчины пропускают в течение года более 2 рабочих дней (work_days) по болезни значимо чаще женщин.
2)	Работники старше 35 лет (age) пропускают в течение года более 2 рабочих дней (work_days) по болезни значимо чаще своих более молодых коллег.
Все необходимые данные содержатся в файле «Статистика».

Решение необходимо предоставить: 
1)	В виде jupyter notebook (с аккуратно оформленным кодом, графиками и описанной логикой решения). 
2)	В виде дашборда на Streamlit с простым функционалом: 
 - a.	должна быть возможность загрузить csv, в формате аналогично файлу «Статистика»
 - b.	должна быть возможность задать параметры age и work_days
 - c.	указан результат проверки гипотез
 - d.	указана логика получения результата (должны быть отрисованы графики распределений, указаны критерии проверки (стат. тесты, статистики, уровень значимости т.п.) 

## Пояснения
1) Дашборд поднят на сервере streamlit: https://theborokko-mtech-mvideo-streamlit-sbox3k.streamlit.app/
2) Примеры значений при которых отвергаются нулевые гипотезы (принимаются гипотезы, которые даны в постановке задачи):
 - a. work_days = 6 - мужчины пропускают по болезни значимо чаще женщин
 - b. age = 36 - работники, достигшие это возраста, пропускают 2 рабочих дня значимо чаще чем более молодые коллеги 
