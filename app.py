from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/pokemon/<query>")
def search(query):

    url = "https://pokeapi.co/api/v2/pokemon-form/" + query + "/"
    r = requests.get(url).json()

    if query.isdigit():
        return 'The pokemon with id ' + str(query) + ' is ' + r['name']
    else:
        return str(query) + ' has id ' +  str(r['id'])


if __name__ == '__main__':
    app.run()
