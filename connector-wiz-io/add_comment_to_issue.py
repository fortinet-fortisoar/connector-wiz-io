import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import api_query_call
import requests, json
logger = get_logger(LOGGER_NAME)


def add_comment_to_issue(config, params):
    query = """
    mutation CreateIssueComment($input: CreateIssueNoteInput!) {
      createIssueNote(input: $input) {
        issueNote {
          createdAt
          id
          text
          user {
            id
            email
          }
        }
      }
    }
    """
    variables = {
	  "input": {
	    "issueId": params.get("issueID"),
	    "text": params.get("comment")
	  }
	}
    try:
      response = api_query_call(config, query=query, variables=variables)
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)