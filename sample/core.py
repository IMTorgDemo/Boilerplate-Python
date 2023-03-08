# -*- coding: utf-8 -*-
"""The module provides logic for doing interesting things.

This is implmented for the following reasons.

Example:
    The module can be called either from the service, or the commandline::

        >>> bundler.main()   ???this fails, currently
        $ python bundler

Attributes:
    EMAIL (str): attribute provided by .env file for use in interacting with
        the DynamoDb database.
    PASSWORD (str): same as above.
    LOOKUP_NAME (str): filename for the lookup.csv file.

Functions: 
    main (): input obtained from DynamoDb. Results saved to ./data/output.csv 

Todo:
    * blah, blah
      + blah
      + blah
      + blah
      + blah
      + blah
    * blah, blah

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
# -----------------------------------------------------------------------------
# IMPORTS

# system libs
import os

# internal libs
from . import helpers
from .common import config
from .common import log

# external libs
import requests



# auth
from dotenv import load_dotenv
from pathlib import Path 
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


# global var
env_var = {
    # secret
    'EMAIL':os.getenv('EMAIL'),
    'PASSWORD':os.getenv('PASSWORD'),
    # urls
    'FILE_LOAD':config.config['FILE_LOAD']
}


# -----------------------------------------------------------------------------
# FUNCTIONS

def get_hmm():
    """Get a thought."""
    out = 'hmmm... nice username, ' + env_var['EMAIL']
    return out


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
    url = 'https://www.google.com'
    resp = requests.get(url)
    print(resp.status_code)




# -----------------------------------------------------------------------------
# MAIN
def main():
    """Run the script from commandline.
    """
    log.log("******* BEGIN SCRIPT *******")
    hmm()


if __name__ == '__main__':
    main()    