class BaseResponse:

    def __init__(self):
        self.base_data = {
            'payload': {
                'google': {
                    'expect_user_response': False,
                    'is_ssml': True,
                    'permissions_request': None,
                    "richResponse": {
                        "items": []
                    }
                }
            },
            'source': 'webhook'
        }

    def build(self):
        raise NotImplementedError


class TextResponse(BaseResponse):

    def __init__(self, text, expect_reply, display_text=None):
        super().__init__()
        self.text = text
        self.expect_reply = expect_reply
        self.display_text = display_text if display_text else text

    def build(self):
        message = {
            "simpleResponse": {
                "textToSpeech": self.text,
                "displayText": self.display_text
            }
        }
        self.base_data['payload']['google']['richResponse']['items'].append(message)
        self.base_data['payload']['google']['expect_user_response'] = self.expect_reply
        return self.base_data


class CardResponse(BaseResponse):

    def __init__(self, text, title, subtitle, image_uri, button, expect_reply):
        super().__init__()
        self.text = text
        self.expect_reply = expect_reply
        self.title = title
        self.subtitle = subtitle
        self.image_uri = image_uri
        self.button = button

    def build(self):
        self.base_data['payload']['google']['expect_user_response'] = self.expect_reply
        return self.base_data
