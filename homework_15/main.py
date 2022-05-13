from Flask import flask, jsonify
import sqlite3

def main():
    app = Flask(__name__)
    app.congig['JSON_AS_ASII'] = False
    app.config['DEBUG'] = True

    def db_connect(query):
    connection = sqlite3.connect('animal.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

    @app.route('animals/<int:itemid>')
    def requet_by_animal_index(itemid):
        query = f"""SELECT
        animal_index,
        name,
        outcome_year
        FROM animals_redesigned
        WHERE animal_index = {itemid}
        """
        db_connect(query)
        return jsonify(db_connect(query))

    app.run(debug=True)

if __name__ = '__man__':
    main()

