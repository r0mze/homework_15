import sqlite3


connection = sqlite3.connect("netflix.db")
cursor = connection.cursor()
sqlite_query = (""
                "SElECT title, country, release_year, listed_in AS genre, description "
                "from netflix "
                "ORDER BY release_year DESC "
                "LIMIT 1")
cursor.execute(sqlite_query)
result = cursor.fetchall()


if __name__ == '__main__':
    print(result)
    print()
    print(f"title: {result[0][0]}")
    print(f"country: {result[0][1]}")
    print(f"release_year: {result[0][2]}")
    print(f"genre: {result[0][3]}")
    print(f"description: {result[0][4]}")


