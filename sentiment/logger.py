import logging
import os

# coming back to this for memory usage stuff, may also do this is pandas for key components

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )
# test
logging.debug('messages')
logging.warning('warnings')

f = open(LOG_FILENAME, 'rt')
try:
    body = f.read()
finally:
    f.close()

# TODO: add logging for whole project here
