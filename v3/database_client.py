from typing import final
from sqlalchemy import create_engine

# create_table_sql = """CREATE TABLE Users(
# name TEXT NOT NULL,
# email TEXT PRIMARY KEY,
# company_name TEXT NOT NULL,
# phone_number TEXT NOT NULL,
# api_key TEXT NOT NULL UNIQUE,
# image TEXT
# );

# CREATE TABLE Logs(
# email TEXT,
# result TEXT,
# output TEXT,
# exec_time REAL
# );
# """

engine = create_engine("sqlite://///home/ryan/Documents/Pekla/WebApp/v3/db.db")


# try:
#     conn = engine.connect()
#     conn.execute(create_table_sql)
# except Exception as e:
#     print(e)
# finally:
#     conn.close()
#     engine.dispose()

