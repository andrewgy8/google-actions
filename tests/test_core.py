from flask import Response

from apprentice import format
from apprentice.helpers import action_ctx_test


class TestIntentResponse:

    def test_returns_object_when_given_text(self):
        text = 'Hello world'
        json_response = format.query_result(text, expect_user_response=True)

        assert json_response == {
            'outputContexts': [],
            'payload': {
                'google': {
                    'expect_user_response': True,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'fulfillmentMessages': [
                {
                    "platform": "ACTIONS_ON_GOOGLE",
                    "text": {
                        "text": [
                            'Hello world'
                        ]
                    }
                }
            ],
            'source': 'webhook',
            'fulfillmentText': 'Hello world'
        }

    def test_returns_expect_user_response_when_set_to_false(self):
        text = 'Hello world'
        json_response = format.query_result(text,
                                            expect_user_response=False)

        assert json_response == {
            'outputContexts': [],
            'payload': {
                'google': {
                    'expect_user_response': False,
                    'is_ssml': True,
                    'permissions_request': None
                },
            },
            'fulfillmentMessages': [
                {
                    "platform": "ACTIONS_ON_GOOGLE",
                    "text": {
                        "text": [
                            'Hello world'
                        ]
                    }
                }
            ],
            'source': 'webhook',
            'fulfillmentText': 'Hello world'
        }


class TestFormatResponse:

    @action_ctx_test
    def test_returns_flask_response_object(self):
        data = {'msg': 'hello world'}
        res = format.response(data)

        assert isinstance(res, Response)
        assert res.json == data
        assert res.headers['Content-Type'] == 'application/json'
