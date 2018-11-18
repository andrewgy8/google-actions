# Apprentice
[![Build Status](https://travis-ci.com/andrewgy8/apprentice.svg?branch=master)](https://travis-ci.com/andrewgy8/apprentice)
[![PyPI version](https://badge.fury.io/py/apprentice.svg)](https://badge.fury.io/py/apprentice)

Apprentice is a library for deploying and developing actions via Dialogflow and Google Cloud Functions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Apprentice.

```bash
pip install apprentice
```

## Quickstart

A Google Action project will consist of two things:
1. A Dialogflow defined action
1. An endpoint that your Dialogflow Action can talk to.

To generate a Hello World application, you can run:

```bash
$ apprentice init
```

This will create a file structure:

```bash
hello_world_agent/
    main.py
    requirements.txt
```

`main.py` is the file that `gcloud` looks for to upload the function.
It is important that the name, `main.py`, remains in order to use `gcloud` cli.

## Testing

To make local development quicker, you can run a local server with 
```bash
$ apprentice run
```

## Deployment

### Note
[`gcloud` cli](https://cloud.google.com/sdk/docs/quickstarts) must be installed and authorized for the following command 
to work. If you wish to not have `gcloud` cli installed, you can copy the file contents via the gcloud 
function dashboard.   

```bash
$ apprentice -f hello_world -s hello_world_agent -e hello_world
```

This will generate the command to execute a `gcloud function deploy` via the cli.  

## Example Project

```python
import random

import requests

from apprentice import format_response, generate_intent_response


def cool_fact_generator(*args, **kwargs):
    data = _fact_response()
    formatted_data = generate_intent_response(data)
    return format_response(formatted_data)


def _fact_response():
    res = requests.get('https://history.muffinlabs.com/date')
    data = res.json().get('data')

    fact = random.choice(data['Events'])
    year = fact['year']
    text = fact['text']
    phrase = f'Today, in the year {year} {text}'
    return phrase
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU 3.0](https://choosealicense.com/licenses/gpl-3.0/)
