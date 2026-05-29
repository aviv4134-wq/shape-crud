import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
file_handler = logging.FileHandler('logs.txt',encoding='utf-8')
file_streamer = logging.StreamHandler()

file_handler.setFormatter(formatter)
file_streamer.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(file_streamer)

