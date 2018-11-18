import random

import requests
from flask import Flask, request

from apprentice import format_response, generate_intent_response

app = Flask(__name__)

ENTITIES = {
    "name": "History",
    "entries": [
        {
            "value": "history",
            "synonyms": [
                "history",
                "past event",
                "the past",
                "past"
            ]
        }, {
            "value": "birth",
            "synonyms": [
                "birth",
                "births",
                "born"
            ]
        }
    ]
}


@app.route('/', methods=['POST'])
def cool_fact_generator(*args, **kwargs):
    ac = request.json['result']['parameters']
    name = ENTITIES.get('name')
    entity = ac[name]
    phrase = _fact_response(entity)
    formatted_data = generate_intent_response(phrase)
    return format_response(formatted_data)


def _fact_response(entity):
    res = requests.get('https://history.muffinlabs.com/date')
    data = res.json().get('data')
    if entity == 'birth':
        type_of_fact = data['Births']
    else:
        type_of_fact = data['Events']
    fact = random.choice(type_of_fact)
    year = fact['year']
    text = fact['text']
    if entity == 'birth':
        return f'Today in the year {year}, {text} was born.'
    else:
        return f'Today in the year {year}, {text}'
