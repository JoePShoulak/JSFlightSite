from ariadne import QueryType

query = QueryType()

from db.client import get_client
from db.exceptions import DataError
def resolve_get_client(_, info, id: int) -> dict:
    try:
        return { '__typename': 'Client', **get_client(id) }
    except DataError as e:
        return { '__typename': e.__class__.__name__, 'message': str(e) }

query.set_field('getClient', resolve_get_client)
