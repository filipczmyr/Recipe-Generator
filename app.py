from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
from ai import Ai

OPENAI_API_KEY = "YOUR_API_KEY"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)

class ingredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(100))

@app.route('/', methods=['POST', 'GET'])
def index():
    recepie = ""
    data = ingredients.query.all()
    if request.method == 'POST':
        selected_items = request.form.getlist('selected_items')
        recepie = Ai("Tell  me a recepie using these ingredients: " + str(selected_items), OPENAI_API_KEY)
    return render_template('index.html', data=data, recepie=recepie)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
