from collections import defaultdict
from flask import Flask, request, abort
import random

app = Flask(__name__)

snippets = defaultdict(list)

@app.route('/snippet/<lang>', methods=['GET', 'POST'])
def snippet(lang):
    global snippets

    if request.method == 'POST':
        snippets[lang.strip().lower()].append(request.get_json())

        return "added snippet"
    else:
        if len(snippets[lang]) > 0:
            return random.choice(snippets[lang])
        else:
            abort(400)

past_data = defaultdict(list)

@app.route('/pastdata/<snippetid>', methods=['GET', 'POST'])
def set_past_data(snippetid):
    global past_data

    if request.method == 'POST':
        past_data[snippetid.strip().lower()].append(request.get_json())

        return "added user data"
    else:
        if len(past_data[snippetid]) > 0:
            return random.choice(past_data[snippetid])
        else:
            abort(400)

if __name__ == "__main__":
    app.run(port=5123, debug=True)