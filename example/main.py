import random

import requests

from apprentice import Apprentice, SimpleResponse

apr = Apprentice(__name__)

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


@apr.route('/', methods=['POST'])
def cool_fact_generator(*args, **kwargs):
    reply = _fact_response('name')
    obj = SimpleResponse(speech=reply, expect_reply=True)
    return apr.response_from_object(obj)


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
        return f'Today in the year {year}, {text} was born.'  # noqa
    else:
        return f'Today in the year {year}, {text}'
