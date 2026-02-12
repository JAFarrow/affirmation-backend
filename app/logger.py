import logging
import sys

def setup_logging(app):
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    if app.logger.handlers:
        app.logger.handlers = []

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.logger.info("Logging initialized")
