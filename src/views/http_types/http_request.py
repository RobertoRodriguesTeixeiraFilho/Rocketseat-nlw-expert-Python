class HttpRequest:
    def __init__(
            self,
            header: dict = None,
            body: dict = None,
            query_params: dict = None
        ) -> None: # Caso os elementos não forem preenchidos, os não preenchidos serão None
        # Salvando os elementos que irão entrar no metodo construtor
        self.header = header
        self.body = body
        self.query_params = query_params
