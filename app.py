from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recettes')
def recettes():
    recettes_data = [
        {
            "titre": "Spaghetti Carbonara",
            "description": "Un classique italien avec des œufs, du fromage et des lardons."
        },
        {
            "titre": "Tajine de poulet",
            "description": "Un plat marocain parfumé aux épices et citron confit."
        },
        {
            "titre": "Crêpes sucrées",
            "description": "Délicieuses crêpes maison à savourer avec du Nutella ou du sucre."
        }
    ]
    return render_template('recettes.html', recettes=recettes_data)

if __name__ == '__main__':
    app.run(debug=True)
