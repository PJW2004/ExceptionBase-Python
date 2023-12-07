from . import st_1xx
from . import st_2xx
from . import st_3xx
from . import st_4xx
from . import st_5xx

class CODE_100_1(Exception):
    def __init__(self, obj: str = ""):
        self.msg: str = f"{st_1xx.ErrorCodes.CODE_100_1} : {obj}"
        super().__init__(self.msg)
