# -----------------------------------------------------------------------------
# IMPORTS

# standard lib
import datetime
import traceback

# internal lib
from common import config

# external lib




# -----------------------------------------------------------------------------
# FUNCTIONS
def log(text, print_it=True):
    if not config.config['FILE_LOGGER'].parent.exists():
       config.config['FILE_LOGGER'].parent.makedirs()

    message = '{} - {}'.format(datetime.datetime.now(), text)
    with open(config.config['FILE_LOGGER'], 'a') as f:
        f.write(message + '\n')

    if print_it:
        print( message)



def log_exception(user, project, print_it=True):
    text = traceback.format_exc()

    if not config.config['FILE_ERROR'].parent.exists():
        config.config['FILE_ERROR'].parent.makedirs()

    user_project_message = '{} - {}/{}'.format(datetime.datetime.now(), user, project)
    message = '{} - {}'.format(datetime.datetime.now(), text)
    with open(config.config['FILE_ERROR'], 'a') as f:
        f.write(user_project_message + '\n')
        f.write(message + '\n')

    if print_it:
        print( user_project_message)
        print( message)