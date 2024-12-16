from flask import Flask, render_template, request, jsonify
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

    # Afficher les valeurs de la colonne SIT.ACTUELLE dans le terminal
    for suivi in suivis:
        print(suivi['SIT.ACTUELLE'])  # Cela affichera la valeur de la colonne SIT.ACTUELLE pour chaque ligne

    conn.close()

    return render_template("index.html", suivis=suivis)


@app.route("/search")
def search():
    query = request.args.get('query', '')  # Récupère la requête de recherche
    conn = sqlite3.connect("suivi_curative(BD).db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Recherche dans la base de données (ajustez la colonne à votre besoin)
    cursor.execute("SELECT * FROM suivi_curative WHERE CAST(MATRICULE AS TEXT) LIKE ?", ('%' + query + '%',))
    suivis = cursor.fetchall()

    conn.close()
    # Retourner les résultats au format JSON
    return jsonify([dict(suivi) for suivi in suivis])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
