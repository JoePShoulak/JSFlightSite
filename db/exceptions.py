class DataError(Exception):
	pass

class ClientDoesNotExistError(DataError):
	def __init__(self, id: int):
		super().__init__(f'Client "{id}" does not exist.')