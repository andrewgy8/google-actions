class BaseResponse:

    def __init__(self):
        self.base_data = {
            # 'fulfillmentText': None,
            'fulfillmentMessages': [
                # {
                #     "platform": "ACTIONS_ON_GOOGLE",
                #     "simpleResponses": {
                #         "simpleResponses": [
                #             {"textToSpeech": None}]},
                # }
            ],
            'payload': {
                'google': {
                    'expect_user_response': False,
                    'is_ssml': True,
                    'permissions_request': None,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": "this is a simple response"
                                }
                            },
                            {
                                "basicCard": {
                                    "buttons": [
                                        {
                                            "title": "button text",
                                            "openUriAction": {'uri': "https://www.google.com"}
                                        }
                                    ],
                                    "formattedText": "Some text",
                                    "image": {
                                        "url": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                                        "accessibilityText": "Accessibility text describing the image"
                                    },
                                    "title": "Card Title"
                                }
                            }

                        ]
                    }

                }
            },
            'source': 'webhook'
        }

    def build(self):
        raise NotImplementedError


class TextResponse(BaseResponse):

    def __init__(self, text, expect_reply):
        super().__init__()
        self.text = text
        self.expect_reply = expect_reply

    def build(self):
        message = {
            'platform': 'ACTIONS_ON_GOOGLE',
            'text': {'text': [self.text]}
        }

        self.base_data['fulfillmentMessages'].append(message)
        self.base_data['fulfillmentText'] = self.text
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
        message = {
            # "platform": "ACTIONS_ON_GOOGLE",
            # "quickReplies": {
            #   "title": self.title,
            #   "quickReplies": [self.text]
            # }

            "card": {
                "title": "card title",
                "subtitle": "card text",
                "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                "buttons": [
                    {
                        "text": "button text",
                        "postback": "https://assistant.google.com/"
                    }
                ]
            }


        }
        # self.base_data['fulfillmentMessages'][0]['simpleResponses']['simpleResponses'][0]['textToSpeech'] = self.text
        self.base_data['fulfillmentMessages'].append(message)
        self.base_data['fulfillmentText'] = self.text
        self.base_data['payload']['google']['expect_user_response'] = self.expect_reply
        print(self.base_data)
        return self.base_data



# 'image': {
            #     "imageUri": 'https://upload.wikimedia.org/wikipedia/commons/1/10/Wappen_Uri_matt.svg',
            #     "accessibilityText": 'bull'
            # }