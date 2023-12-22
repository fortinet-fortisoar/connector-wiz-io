from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from django.utils.module_loading import import_string
from .builtins import *
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests
logger = get_logger(LOGGER_NAME)


class Wiz(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        return supported_operations.get(operation)(config, params)

    def check_health(self, config, *args, **kwargs):
        try:
            response = api_query_call(config, query="query{issues{totalCount}}")
            if response.status_code == requests.codes.ok:
                logger.info("connector is available")
                return True
            logger.info(f"Error {response.status_code} - {response.text}")
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)