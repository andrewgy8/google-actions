import json

from flask import make_response


def response(data):
    resp = json.dumps(data, indent=4)
    resp = make_response(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


def intent_response(text, expect_user_response=True):
    return {
        'speech': text,
        'displayText': None,
        'messages': [
            {
                "type": 0,
                "speech": text
            }
        ],
        'data': {
            'google': {
                "expect_user_response": expect_user_response,
                "is_ssml": True,
                "permissions_request": None,
            }
        },
        'contextOut': [],
        'source': 'webhook'
    }
