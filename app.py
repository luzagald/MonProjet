from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    # Connexion à la base SQLite
    conn = sqlite3.connect("suivi_curative(BD).db")
    conn.row_factory = sqlite3.Row  # Récupération sous forme de dictionnaire
    cursor = conn.cursor()

    # Récupération des données
    cursor.execute("SELECT * FROM suivi_curative")
    suivis = cursor.fetchall()

    conn.close()
    return render_template("index.html", suivis=suivis)

if __name__ == "__main__":
    app.run(debug=True)
