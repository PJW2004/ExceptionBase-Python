# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : -_-1
# ***************************************/
# /***************************************
# * note
# * 오류 처리의 기본 베이스 스크립트
# ***************************************/

from . import st_1xx
from . import st_2xx
from . import st_3xx
from . import st_4xx
from . import st_5xx

__all__ = ["st_1xx", "st_2xx", "st_3xx", "st_4xx", "st_5xx"]
__version__ = "1.0.0"

from fastapi import HTTPException

WEB_EXCEPTION_OBJECT    = HTTPException
SYSTEM_EXCEPTION_OBJECT = Exception

# from . import content

# class Code0(Exception):
#     def __init__(self, obj: str = ""):
#         if not isinstance(obj, str):
#             raise Code4()
#         self.msg: str = f"{content.ERROR_CODE_0} : {obj}"
#         super().__init__(self.msg)

# class Code1(Exception):
#     def __init__(self, obj: str = ""):
#         if not isinstance(obj, str):
#             raise Code4()
#         self.msg: str = f"{content.ERROR_CODE_1} : {obj}"
#         super().__init__(self.msg)

# class Code2(Exception):
#     def __init__(self, obj: str = ""):
#         if not isinstance(obj, str):
#             raise Code4()
#         self.msg: str = f"{content.ERROR_CODE_2} : {obj}"
#         super().__init__(self.msg)

# class Code3(Exception):
#     def __init__(self, obj: str = ""):
#         if not isinstance(obj, str):
#             raise Code4()
#         self.msg: str = f"{content.ERROR_CODE_3} : {obj}"
#         super().__init__(self.msg)

# class Code4(Exception):
#     def __init__(self, obj: type = str):
#         self.msg: str = f"{content.ERROR_CODE_4} : {obj}"
#         super().__init__(self.msg)
