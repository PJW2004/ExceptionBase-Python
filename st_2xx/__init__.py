# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : s_--1
# ***************************************/
# /***************************************
# * note
# * 2XX: Success( 성공 )
# * 클라이언트의 요청이 서버에서 성공적으로 처리되었다는 의미입니다.
# ***************************************/

from . import codes

class ErrorCodes:
    def __init__(self):
        self._code_200_status = codes.CODE_200_STATUS
        self._code_200_1 = codes.CODE_200_1
        self._code_201_status = codes.CODE_201_STATUS
        self._code_201_1 = codes.CODE_201_1
        self._code_202_status = codes.CODE_202_STATUS
        self._code_202_1 = codes.CODE_202_1
        self._code_203_status = codes.CODE_203_STATUS
        self._code_203_1 = codes.CODE_203_1
        self._code_204_status = codes.CODE_204_STATUS
        self._code_204_1 = codes.CODE_204_1
        self._code_205_status = codes.CODE_205_STATUS
        self._code_205_1 = codes.CODE_205_1
        self._code_206_status = codes.CODE_206_STATUS
        self._code_206_1 = codes.CODE_206_1
        self._code_207_status = codes.CODE_207_STATUS
        self._code_207_1 = codes.CODE_207_1

    @property
    def CODE_200_STATUS(self):
        """200 상태 코드를 반환합니다.
        """
        return self._code_200_status

    @property
    def CODE_200_1(self):
        """Returns 'ok'

        이는 서버가 요청을 성공적으로 처리 함을 알립니다.
        """
        return self._code_200_1

    @property
    def CODE_201_STATUS(self):
        """201 상태 코드를 반환합니다.
        """
        return self._code_201_status

    @property
    def CODE_201_1(self):
        """Returns : 'created'

        요청이 처리되어서 새로운 리소스가 생성
        응답 헤더 Location 에 새로운 리소스의 절대 URI 를 기록합니다.
        """
        return self._code_201_1

    @property
    def CODE_202_STATUS(self):
        """202 상태 코드를 반환합니다.
        """
        return self._code_202_status

    @property
    def CODE_202_1(self):
        """Returns : 'Accepted'

        요청은 접수하였지만, 처리가 완료되지 않음
        응답 헤더의 Location, Retry-After를 참고하여 클라이언트는 다시 요청을 보냅니다.
        """
        return self._code_202_1

    @property
    def CODE_203_STATUS(self):
        """203 상태 코드를 반환합니다.
        """
        return self._code_203_status

    @property
    def CODE_203_1(self):
        """Returns : 'non-Authoritative information'

        신뢰할 수 없는 정보
        응답 헤더가 오리지널 서버로부터 제공된 것이 아니다.
        프록시 서버가 응답 헤더에 주석을 덧붙인 경우가 하나의 예입니다.
        """
        return self._code_203_1

    @property
    def CODE_204_STATUS(self):
        """204 상태 코드를 반환합니다.
        """
        return self._code_204_status

    @property
    def CODE_204_1(self):
        """Returns : 'no content'

        처리를 성공하였지만, 클라이언트에게 돌려줄 콘텐츠가 없다.
        응답에는 헤더만 있고 바디는 없습니다.
        DELETE 요청에 대한 응답에 많이 사용됩니다.
        """
        return self._code_204_1

    @property
    def CODE_205_STATUS(self):
        """205 상태 코드를 반환합니다.
        """
        return self._code_205_status

    @property
    def CODE_205_1(self):
        """Returns : 'reset content'

        처리를 성공하였고 브라우저의 화면을 리셋하라.
        예를 들어 브라우저가 입력 폼을 보여 주고 있을 때 이 응답 코드를 받으면
        브라우저는 모든 입력 항목을 리셋하고 재 입력할 수 있는 상태가 됩니다.
        """
        return self._code_205_1

    @property
    def CODE_206_STATUS(self):
        """206 상태 코드를 반환합니다.
        """
        return self._code_206_status

    @property
    def CODE_206_1(self):
        """Returns : 'partial content'

        콘텐츠의 일부만을 보낸다.
        응답 헤더의 Content-Range에 응답 콘텐츠의 범위를 기록합니다.
        예를 들어 1,500 바이트의 리소스 중에서 처음의 500바이트만을 보낼 때 사용할 수 있습니다.
        """
        return self._code_206_1

    @property
    def CODE_207_STATUS(self):
        """207 상태 코드를 반환합니다.
        """
        return self._code_207_status

    @property
    def CODE_207_1(self):
        """Returns : 'multi-status'

        (WebDAV) 처리 결과의 스테이터스가 여러개 이다.
        207 응답은 성공을 뜻하지만,
        각각의 처리 결과가 성공인지는 바디를 봐야 알 수 있습니다.
        """
        return self._code_207_1
