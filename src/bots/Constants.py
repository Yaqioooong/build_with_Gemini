from enum import Enum
class Constants(Enum):
    def __str__(self):
        return str(self.value)
    HTTP_PROXY = 'http://127.0.0.1:6969'
    HTTPS_PROXY = 'https://127.0.0.1:6969'
