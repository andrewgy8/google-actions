class BaseResponse:

    def __init__(self, text, expect_reply):
        self.text = text
        self.expect_reply = expect_reply
        self.base_data = {
            'fulfillmentText': None,
            'fulfillmentMessages': [],
            'payload': {
                'google': {
                    "expect_user_response": False,
                    "is_ssml": True,
                    "permissions_request": None,
                }
            },
            'outputContexts': [],
            'source': 'webhook'
        }

    def build(self):
        raise NotImplementedError


class TextResponse(BaseResponse):

    def __init__(self, text, expect_reply):
        super().__init__(text, expect_reply)

    def build(self):
        message = {
            "platform": "ACTIONS_ON_GOOGLE",
            "text": {
                "text": [
                    self.text
                ]
            }
        }

        self.base_data['fulfillmentMessages'].append(message)
        self.base_data['fulfillmentText'] = self.text
        self.base_data['payload']['google']['expect_user_response'] = self.expect_reply
        return self.base_data
