import pytest
import responses

from example.main import _fact_response, apr


@pytest.fixture(autouse=True)
def api_response(historical_fact_response):
    return responses.add(
        responses.GET,
        'https://history.muffinlabs.com/date',
        json=historical_fact_response,
        status=200)


class TestCoolFactGenerator:

    def test_returns_response_with_json_when_called(self, birth_post_data):
        with apr.test_client() as c:
            res = c.post('/', json=birth_post_data)

        assert res.json == {
            'payload': {
                'google': {
                    'expect_user_response': True,
                    'is_ssml': True,
                    'permissions_request': None,
                    'richResponse': {
                        'items': [
                            {
                                'simpleResponse': {
                                    'textToSpeech':
                                        'Today in the year 308, At '
                                        'Carnuntum, Emperor emeritus '
                                        'Diocletian confers with Galerius, '
                                        'Augustus of the East, and '
                                        'Maximianus, the recently returned '
                                        'former Augustus of the West, in '
                                        'an attempt to end the civil wars '
                                        'of the Tetrarchy.',
                                    'displayText':
                                        'Today in the year 308, At '
                                        'Carnuntum, Emperor emeritus '
                                        'Diocletian confers with Galerius, '
                                        'Augustus of the East, and '
                                        'Maximianus, the recently returned '
                                        'former Augustus of the West, in '
                                        'an attempt to end the civil wars '
                                        'of the Tetrarchy.'

                                }
                            }
                        ]
                    }
                }
            },
            'source': 'webhook'
        }

    def test_returns_content_type_json_when_called(self, birth_post_data):
        with apr.test_client() as c:
            res = c.post('/', json=birth_post_data)

        assert res.headers['Content-Type'] == 'application/json'


class TestFactResponse:

    def test_returns_structured_json_object(self):
        res = _fact_response('history')

        assert res == 'Today in the year 308, At Carnuntum, Emperor ' \
                      'emeritus Diocletian confers with Galerius, Augustus ' \
                      'of the East, and Maximianus, the recently returned ' \
                      'former Augustus of the West, in an attempt to end ' \
                      'the civil wars of the Tetrarchy.'
