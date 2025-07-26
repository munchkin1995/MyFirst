from optparse import Values

import psycopg2
import pandas as pd

# Define connection parameters
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test",
    user="postgres",
    password="Root"
)


query = "select * from person"

df = pd.read_sql(query, conn)

# df['country'] = 'india'
print((df["count"][0]))


# Close the connection
# cursor.close()
conn.close()
