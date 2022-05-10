import os
import psycopg2 
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS telephones;')
cur.execute('''CREATE TABLE telephones (id serial PRIMARY KEY,
                                 stamp text NOT NULL,
                                 model text NOT NULL,
                                 diagonal text NOT NULL,
                                 camera text NOT NULL,
                                 memory TEXT NOT NULL);
                                 ''')

cur.execute('''INSERT INTO telephones (stamp, model, diagonal, camera, memory )
            VALUES ('Apple', '12', '13 inches', '15 mp', '512 gigabytes')''')
            
cur.execute('''INSERT INTO telephones (stamp, model, diagonal, camera, memory )
            VALUES ('Apple', '13', '14 inches', '15 mp', '256 gigabytes')''')

cur.execute('''INSERT INTO telephones (stamp, model, diagonal, camera, memory )
            VALUES ('Apple', '11', '12 inches', '13 mp', '128 gigabytes')''')

conn.commit()
cur.close()
conn.close()
#DB_USERNAME = postgres
#DB_PASSWORD = 1234
