from flask import Response

from apprentice import Apprentice


class TestIntentResponse:

    def test_returns_object_when_given_text(self):
        apr = Apprentice(__name__)
        text = 'Hello world'
        json_response = apr.query_result(text, expect_user_response=True)

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
        apr = Apprentice(__name__)
        text = 'Hello world'
        json_response = apr.query_result(text, expect_user_response=False)

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

    def test_returns_flask_response_object(self):
        apr = Apprentice(__name__)
        data = {'msg': 'hello world'}
        with apr.test_request_context():
            res = apr.generate_response(data)

        assert isinstance(res, Response)
        assert res.json == data
        assert res.headers['Content-Type'] == 'application/json'
