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
    r = requests.get(url)

    if r.status_code == 200:

        r = r.json()

        if query.isdigit():
            return 'The pokemon with id ' + str(query) + ' is ' + r['name']
        else:
            return str(query) + ' has id ' +  str(r['id'])
    else:
        return 'Please input a valid pokemon name or id'

if __name__ == '__main__':
    app.run()
