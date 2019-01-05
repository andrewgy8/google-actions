import pytest

from apprentice.responses import BaseResponse, TextResponse


class TestBaseResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = BaseResponse(text, expect_reply=expect_response)

        with pytest.raises(NotImplementedError):
            res.build()


class TestTextResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = TextResponse(text, expect_reply=expect_response)

        assert res.build() == {
            'payload': {
                'google': {
                    'expect_user_response': expect_response,
                    'is_ssml': True,
                    'permissions_request': None,
                    'richResponse': {
                        'items': [
                            {
                                "simpleResponse": {
                                    "textToSpeech": 'Hello world',
                                    "displayText": 'Hello world'

                                }
                            }
                        ]
                    }
                }
            },
            'source': 'webhook'
        }


class TestCardResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = TextResponse(text, expect_reply=expect_response)

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
