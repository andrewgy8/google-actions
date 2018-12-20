# Apprentice
[![Build Status](https://travis-ci.com/andrewgy8/apprentice.svg?branch=master)](https://travis-ci.com/andrewgy8/apprentice)
[![PyPI version](https://badge.fury.io/py/apprentice.svg)](https://badge.fury.io/py/apprentice)

Apprentice is a framework built for developing Google Actions 
via [Dialogflow](https://dialogflow.com) and 
[Google Cloud (serverless) Functions](https://cloud.google.com/functions/).

Includes:
- plug-and-play feel to get going quickly
- basic Dialogflow API 2.0 response handling
- local setup for quick iteration

## Installation

```bash
pip install apprentice
```

## Quickstart

A Google Action project will consist of two things:
1. [Dialogflow Intent](https://dialogflow.com/docs/intents)
1. A webhook to satisfy your users intent

To generate a "Hello World" webhook, run:

```bash
$ apprentice init
```

This will create a file structure:

```bash
src/
    main.py
    requirements.txt
```

Run a local server with 
```bash
$ apprentice run
```

and expose to localhost port via an https tunnel. Then add the url to the fulfillment
webhook in Dialogflow.  

For a more indepth example please see the tutorial I wrote 
[here](https://medium.com/@andrew_32881/hey-google-talk-to-24dfd336acd).

## Deployment

### Note
[`gcloud` cli](https://cloud.google.com/sdk/docs/quickstarts) must be installed and authorized for the following command 
to work. If you wish to not have `gcloud` cli installed, you can copy the file contents via the gcloud 
function dashboard.   

```bash
$ apprentice -f hello_world -s hello_world_agent -e hello_world
```

This will generate the command to execute a `gcloud function deploy` via the cli.  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU 3.0](https://choosealicense.com/licenses/gpl-3.0/)
