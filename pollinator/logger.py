import logging

logger = logging.getLogger("pollinator")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler("pollinator.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
