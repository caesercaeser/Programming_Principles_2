import psycopg2
from create_table import conn
    
config = psycopg2.connect(**conn)
current = config.cursor()

create_table = '''
    create table snake(
        username VARCHAR(255),
        score INT
    );
''' 

current.execute(create_table)

current.close()
config.commit()
config.close()