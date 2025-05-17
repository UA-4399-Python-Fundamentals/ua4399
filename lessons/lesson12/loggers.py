import logging
from pathlib import Path
path  = Path(__file__).parent
logging.basicConfig(
    level=logging.DEBUG,
    filename=f'{path}/app.log',
    filemode='w',
    format='%(asctime)s - %(thread)d - %(name)s - %(levelname)s - %(filename)s - %(funcName)s- %(message)s'
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

def my_funk():
    logging.debug('This is a debug message from f')
    logging.info('This is an info message from f')
    logging.warning('This is a warning message from f')
    logging.error('This is an error message from f')
    logging.critical('This is a critical message from f')

my_funk()
