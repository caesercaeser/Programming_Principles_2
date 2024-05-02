import psycopg2
conn = psycopg2.connect(
	host = "127.0.0.1",
   user = "postgres",
   password = "123456",
   dbname = "snakedata"

)

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE Snakedata(
   user_login VARCHAR(255) NOT NULL,
   last_score INT,
   last_level INT,
   last_FPS INT,
   snake_len INT,
   wall_len INT,
   snake_x INT,
   snake_y INT,
   record INT
);'''


cursor.execute(sql)
print("Database has been created successfully !!");
conn.close()