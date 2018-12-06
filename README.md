# Apprentice
[![Build Status](https://travis-ci.com/andrewgy8/apprentice.svg?branch=master)](https://travis-ci.com/andrewgy8/apprentice)
[![PyPI version](https://badge.fury.io/py/apprentice.svg)](https://badge.fury.io/py/apprentice)

Apprentice is a library for deploying and developing actions via Dialogflow and Google Cloud Functions.

## Installation

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

## Getting Started

```python
from apprentice import Apprentice

apr = Apprentice(__name__)


@apr.action()
def hello_world(*args, **kwargs):
    reply = 'Hello world!'
    return apr.response(reply)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU 3.0](https://choosealicense.com/licenses/gpl-3.0/)
