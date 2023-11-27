import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

#insert your data
connection = mysql.connector.connect (
    host = '',
    user = '',
    password = '',
    database = 'chicagocrime'
)

#insert the query that you will use
query = '''
SELECT *
FROM chicago_crimes_2008_to_2011
    '''

df = pd.read_sql_query(query, connection)

#graphic config
plt.figure(figsize=(10,6))

df.plot(kind='bar', x='tipo', y='cantidad', rot=45)

plt.xlabel('Crime type')
plt.ylabel('Crime quantity')
plt.title('Crime quantity between the years 2008 and 2009')

#this is to display the exact number of each value over each bar in case of be neccesary
for index, value in enumerate(df['cantidad']):
    plt.annotate(str(value), xy=(index, value), ha='center', va='bottom')

plt.show()

