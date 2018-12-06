import json

from flask import Flask, make_response


class Apprentice(Flask):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(__name__, *args, **kwargs)

    def generate_text_response(self, reply):
        response_object = self.query_result(reply)
        return self.generate_response(response_object)

    def generate_response(self, data):
        resp = json.dumps(data, indent=4)
        resp = make_response(resp)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    def query_result(self, text, expect_user_response=True):
        return {
            'fulfillmentText': text,
            'fulfillmentMessages': [
                {
                    "platform": "ACTIONS_ON_GOOGLE",
                    "text": {
                        "text": [
                            text
                        ]
                    }
                }
            ],
            'payload': {
                'google': {
                    "expect_user_response": expect_user_response,
                    "is_ssml": True,
                    "permissions_request": None,
                }
            },
            'outputContexts': [],
            'source': 'webhook'
        }
