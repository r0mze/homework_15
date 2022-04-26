from flask import Flask, jsonify
import sqlite3


def main():
    app = Flask(__name__)
    app.config['JSON_AS_ACII'] = False
    app.config['DEBUG'] = True


def db_connect(query):
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def get_actors(name1='Rose McIver', name2='Ben Lamb'):
    query = f"""
        SELECT 
            "cast"
        FROM netflix
        WHERE "cast" LIKE '%{name1}%'
            AND "cast" LIKE '%{name2}%'
        """
    response = db_connect(query)
    actors = []
    for cast in response:
        if cast == name1 or cast == name2:
            continue
        else:
            actors.extend(cast[0].split(', '))
    print(set(actors))

get_actors()
    # response_json.append({
    #     'title': cast[0].split(', ')
    # })
    # return jsonify(response_json)


if __name__ == '__main__':
    main()
