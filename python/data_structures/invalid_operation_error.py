class InvalidOperationError(Exception):
    def __init__(self, str_message):
        super().__init__(str_message)
