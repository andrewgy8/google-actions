import pytest

from apprentice.responses import (
    BasicCardResponse,
    SimpleResponse,
    _BaseResponse
)


class TestBaseResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = _BaseResponse(text, expect_reply=expect_response)

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


class TestTextResponse:

    @pytest.mark.parametrize('expect_response', [
        True,
        False
    ])
    def test_returns_basic_text_response_when_expect_response_specified(
            self, expect_response):
        text = 'Hello world'
        res = SimpleResponse(text, expect_reply=expect_response)

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
        title = 'This is the card title'
        image_url = 'https://www.some-image-uri.com'
        image_accessibility_text = 'Image description text'
        button = {
            "title": "Click Me!",
            "openUrlAction": {
                'url': "https://www.button-direction-uri.com"}
        }

        res = BasicCardResponse(speech=text,
                                title=title,
                                image_url=image_url,
                                image_accessibility_text=image_accessibility_text,  # noqa
                                button=button,
                                expect_reply=expect_response)
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
                            },
                            {
                                "basicCard": {
                                    "buttons": [
                                        {
                                            "title": "Click Me!",
                                            "openUrlAction": {
                                                'url': "https://www.button-direction-uri.com"  # noqa
                                            }
                                        }
                                    ],
                                    "image": {
                                        "url": "https://www.some-image-uri.com",  # noqa
                                        "accessibilityText": "Image description text"  # noqa
                                    },
                                    "title": "This is the card title"
                                }
                            }
                        ]
                    }
                }
            },
            'source': 'webhook'
        }
