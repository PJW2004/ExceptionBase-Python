# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : s_--1
# ***************************************/
# /***************************************
# * note
# * 5XX: Success( 서버 에러 )
# * 서버 사정으로 메시지 처리에 문제가 발생한 경우입니다.
# * 서버의 부하, DB 처리 과정 오류, 서버에서 익셉션이 발생하는 경우를 의미합니다.
# ***************************************/

from . import codes

class ErrorCodes:
    def __init__(self):
        self._code_500_status = codes.CODE_500_STATUS
        self._code_500_1 = codes.CODE_500_1
        self._code_501_status = codes.CODE_501_STATUS
        self._code_501_1 = codes.CODE_501_1
        self._code_502_status = codes.CODE_502_STATUS
        self._code_502_1 = codes.CODE_502_1
        self._code_503_status = codes.CODE_503_STATUS
        self._code_503_1 = codes.CODE_503_1
        self._code_504_status = codes.CODE_504_STATUS
        self._code_504_1 = codes.CODE_504_1
        self._code_505_status = codes.CODE_505_STATUS
        self._code_505_1 = codes.CODE_505_1
        self._code_507_status = codes.CODE_507_STATUS
        self._code_507_1 = codes.CODE_507_1

    @property
    def CODE_500_STATUS(self):
        """500 상태 코드를 반환합니다.
        """
        return self._code_500_status

    @property
    def CODE_500_1(self):
        """Returns : 'internal server error'

        서버에 에러가 발생하였다.
        클라이언트가 모르는 5xx 계열의 응답 코드가 반환된 경우에도 클라이언트는
        500과 동일하게 처리하도록 규정하고 있습니다.
        """
        return self._code_500_1

    @property
    def CODE_501_STATUS(self):
        """501 상태 코드를 반환합니다.
        """
        return self._code_501_status

    @property
    def CODE_501_1(self):
        """Returns : 'not implemented'

        요청한 URI의 메소드에 대해 서버가 구현하고 있지 않다.
        """
        return self._code_501_1

    @property
    def CODE_502_STATUS(self):
        """502 상태 코드를 반환합니다.
        """
        return self._code_502_status

    @property
    def CODE_502_1(self):
        """Returns : 'bad gateway'

        게이트웨이 또는 프록시 역할을 하는 서버가 그 뒷단의 서버로부터 잘못된 응답을 받았다.
        """
        return self._code_502_1

    @property
    def CODE_503_STATUS(self):
        """503 상태 코드를 반환합니다.
        """
        return self._code_503_status

    @property
    def CODE_503_1(self):
        """Returns : 'service unavailable'

        현재 서버에서 서비스를 제공할 수 없다.
        보통은 서버의 과부하나 서비스 점검 등 일시적인 상태입니다.
        """
        return self._code_503_1

    @property
    def CODE_504_STATUS(self):
        """504 상태 코드를 반환합니다.
        """
        return self._code_504_status

    @property
    def CODE_504_1(self):
        """Returns : 'gateway timeout'

        게이트웨이 또는 프록시 역할을 하는 서버가 그 뒷단의
        서버로부터 응답을 기다리다 타임아웃이 발생하였다.
        """
        return self._code_504_1

    @property
    def CODE_505_STATUS(self):
        """505 상태 코드를 반환합니다.
        """
        return self._code_505_status

    @property
    def CODE_505_1(self):
        """Returns : 'HTTP version not supported'

        클라이언트가 요청에 사용한 HTTP 버전을 서버가 지원하지 않는다.
        """
        return self._code_505_1

    @property
    def CODE_507_STATUS(self):
        """507 상태 코드를 반환합니다.
        """
        return self._code_507_status

    @property
    def CODE_507_1(self):
        """Returns : 'insufficient storage'

        (WebDAV) 서버에 저장 공간 부족으로 처리에 실패하였다.
        """
        return self._code_507_1
