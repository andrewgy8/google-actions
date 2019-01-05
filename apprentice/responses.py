class _BaseResponse:

    def __init__(self, speech, expect_reply, display_text=None):
        self.speech = speech
        self.display_text = display_text if display_text else speech
        self.expect_reply = expect_reply
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
        message = {
            "simpleResponse": {
                "textToSpeech": self.speech,
                "displayText": self.display_text
            }
        }
        payload = self.base_data['payload']['google']
        payload['richResponse']['items'].append(message)
        payload['expect_user_response'] = self.expect_reply
        return self.base_data


class SimpleResponse(_BaseResponse):
    """ Simple text response.
    Simple response with both text to speech and display settings.
    """
    pass


class BasicCardResponse(_BaseResponse):

    def __init__(self,
                 speech,
                 title,
                 image_url,
                 image_accessibility_text,
                 button,
                 expect_reply):
        super().__init__(speech, expect_reply)
        self.title = title
        self.image_uri = image_url
        self.image_accessibility_text = image_accessibility_text
        self.button = button

    def build(self):
        super().build()
        message = {
            "basicCard": {
                "buttons": [self.button],
                "image": {
                    "url": self.image_uri,
                    "accessibilityText": self.image_accessibility_text
                },
                "title": self.title
            }
        }
        payload = self.base_data['payload']['google']
        payload['richResponse']['items'].append(message)
        return self.base_data
