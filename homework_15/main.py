import sqlite3

connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
sqlite_query = """
CREATE TABLE IF NOT EXISTS animals_redesigned (
	animal_id integer PRIMARY KEY AUTOINCREMENT,
	name varchar,
	date_of_birth date ,
	age_upon_outcome varchar,
	animal_type_id integer,
	outcome_type_id integer,
	animal_breed_id integer,
	color_1st_id integer,
	color_2d_id integer,
	outcome_subtype_id integer,
	month_id integer,
	year_id integer
)
"""
cursor.execute(sqlite_query)
cursor.fetchall()
connection.close()