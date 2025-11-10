import logging
import logging.config
import yaml

# Load logging configuration from YAML file
with open("logging_config.yaml", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create a logger
logger = logging.getLogger("my_app")

# Example log messages
logger.debug("This is a DEBUG message - useful for development.")
logger.info("This is an INFO message - something normal happened.")
logger.warning("This is a WARNING message - something unexpected happened.")
logger.error("This is an ERROR message - something failed.")
logger.critical("This is a CRITICAL message - major failure!")
