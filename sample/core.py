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
import helpers
from common import config

# external libs
import requests



# auth



# global var
env_var = {
    # secret
    'EMAIL':os.getenv('EMAIL'),
    'PASSWORD':os.getenv('PASSWORD'),
    # urls
    'FILE_LOAD':config.config["FILE_LOAD"]
}


# -----------------------------------------------------------------------------
# FUNCTIONS

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())




# -----------------------------------------------------------------------------
# MAIN
def main():
    """Run the script from commandline.
    """
    get_hmm()
    hmm()


if __name__ == '__main__':
    main()    