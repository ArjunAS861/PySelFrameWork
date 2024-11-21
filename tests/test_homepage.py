from utilities.SetupClass import SetupClass
import logging
import os

logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler(os.getcwd() + "\\reports\\" + __name__ + "_report.log")
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
class TestForm(SetupClass):
    def test_form_submission(self, data_provider):
        logger.info(data_provider["name"])
        logger.info(data_provider["address"])


