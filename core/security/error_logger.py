import logging

logger = logging.getLogger("GAIA_ErrorLogger")
handler = logging.FileHandler("logs/errors.log")
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)
