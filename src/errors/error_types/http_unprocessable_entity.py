class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str) -> None: # "Conversar" com a classe Exception
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
