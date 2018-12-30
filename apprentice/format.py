import json

from flask import Flask, make_response

from .responses import TextResponse, CardResponse


class Apprentice(Flask):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(__name__, *args, **kwargs)

    def generate_text_response(self, reply):
        response_object = self.query_result(reply)
        return self.generate_response(response_object)

    def generate_card_response(self, reply):
        response = CardResponse(
            text="foo", title=reply, subtitle='bar', image_uri='',
            button=None, expect_reply=True)
        response_object = response.build()
        return self.generate_response(response_object)

    def generate_response(self, data):
        resp = json.dumps(data, indent=4)
        resp = make_response(resp)
        resp.headers['Content-Type'] = 'application/json'
        return resp

    def query_result(self, text, expect_user_response=True):
        response = TextResponse(text, expect_user_response)
        return response.build()

