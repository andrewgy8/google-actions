import pytest

from apprentice.format import Response


class TestResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = Response(text, expect_reply=expect_response)

        assert res.build() == {
            'outputContexts': [],
            'payload': {
                'google': {
                    'expect_user_response': expect_response,
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
