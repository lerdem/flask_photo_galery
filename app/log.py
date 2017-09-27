import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(name)-12s | %(levelname)-5s | %(message)s'
)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)

filehandler = logging.FileHandler('logger.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(filehandler)