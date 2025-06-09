from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recettes')
def recettes():
    recettes_list = [
        {"titre": "Crêpes sucrées", "description": "Délicieuses crêpes françaises."},
        {"titre": "Tajine au poulet", "description": "Un classique marocain."},
        {"titre": "Riz sauté aux légumes", "description": "Facile et rapide."}
    ]
    return render_template("recettes.html", recettes=recettes_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
