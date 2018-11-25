from flask import Response

from apprentice import format
from apprentice.helpers import action_ctx_test


class TestIntentResponse:

    def test_returns_object_when_given_text(self):
        text = 'Hello world'
        json_response = format.intent_response(text, expect_user_response=True)

        assert json_response == {
            'contextOut': [],
            'data': {
                'google': {
                    'expect_user_response': True,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'displayText': None,
            'messages': [{
                'speech': 'Hello world',
                'type': 0
            }],
            'source': 'webhook',
            'speech': 'Hello world'
        }

    def test_returns_expect_user_response_when_set_to_false(self):
        text = 'Hello world'
        json_response = format.intent_response(text,
                                               expect_user_response=False)

        assert json_response == {
            'contextOut': [],
            'data': {
                'google': {
                    'expect_user_response': False,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'displayText': None,
            'messages': [{
                'speech': 'Hello world',
                'type': 0
            }],
            'source': 'webhook',
            'speech': 'Hello world'
        }


class TestFormatResponse:

    @action_ctx_test
    def test_returns_flask_response_object(self):
        data = {'msg': 'hello world'}
        res = format.response(data)

        assert isinstance(res, Response)
        assert res.json == data
        assert res.headers['Content-Type'] == 'application/json'
