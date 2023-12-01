# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : s_--1
# ***************************************/
# /***************************************
# * note
# * 1XX: Information( 정보 제공 )
# * 임시 응답으로 현재 클라이언트의 요청까지는 처리 되었으니 계속 진행하라는 의미 입니다.
# * HTTP 1.1 버전부터 추가 되었습니다.
# ***************************************/

from . import codes

class ErrorCodes:
    def __init__(self):
        self._code_100_status = codes.CODE_100_STATUS
        self._code_100_1 = codes.CODE_100_1
        self._code_101_status = codes.CODE_101_STATUS
        self._code_101_1 = codes.CODE_101_1
        self._code_102_status = codes.CODE_102_STATUS
        self._code_102_1 = codes.CODE_102_1

    @property
    def CODE_100_STATUS(self):
        """100 상태 코드를 반환합니다.
        """
        return self._code_100_status

    @property
    def CODE_100_1(self):
        """Returns : 'continue'

        이는 리소스에 대한 액세스가 금지됨을 나타내는 문자열입니다.
        """
        return self._code_100_1

    @property
    def CODE_101_STATUS(self):
        """101 상태 코드를 반환합니다.
        """
        return self._code_101_status

    @property
    def CODE_101_1(self):
        """Returns : 'switching protocols'

        이는 프로토콜을 HTTP 1.1에서 업그레이드할 때 Upgrade 응답 헤더에 표시합니다.
        """
        return self._code_101_1

    @property
    def CODE_102_STATUS(self):
        """102 상태 코드를 반환합니다.
        """
        return self._code_102_status

    @property
    def CODE_102_1(self):
        """Returns : 'processing'

        이는 서버가 처리하는 데 오랜 시간이 예상되어 클라이언트에서
        타임 아웃이 발생하지 않도록 이 응답 코드를 보냅니다.
        """
        return self._code_102_1
