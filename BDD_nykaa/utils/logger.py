import logging
import os


def get_logger():

    base_dir = os.getcwd()
    logs_dir = os.path.join(base_dir, "logs")

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logger = logging.getLogger("nykaa_logger")

    logger.handlers.clear()

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    log_file = os.path.join(logs_dir, "test.log")

    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger