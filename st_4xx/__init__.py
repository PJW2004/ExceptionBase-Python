# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : s_--1
# ***************************************/
# /***************************************
# * note
# * 4XX: Client Error( 클라이언트 에러 )
# * 없는 페이지를 요청하는 등 클라이언트의 요청 메시지 내용이 잘못된 경우를 의미합니다.
# ***************************************/

from . import codes

class ErrorCodes:
    def __init__(self):
        self._code_400_status = codes.CODE_400_STATUS
        self._code_400_1 = codes.CODE_400_1
        self._code_401_status = codes.CODE_401_STATUS
        self._code_401_1 = codes.CODE_401_1
        self._code_402_status = codes.CODE_402_STATUS
        self._code_402_1 = codes.CODE_402_1
        self._code_403_status = codes.CODE_403_STATUS
        self._code_403_1 = codes.CODE_403_1
        self._code_404_status = codes.CODE_404_STATUS
        self._code_404_1 = codes.CODE_404_1
        self._code_405_status = codes.CODE_405_STATUS
        self._code_405_1 = codes.CODE_405_1
        self._code_406_status = codes.CODE_406_STATUS
        self._code_406_1 = codes.CODE_406_1
        self._code_407_status = codes.CODE_407_STATUS
        self._code_407_1 = codes.CODE_407_1
        self._code_408_status = codes.CODE_408_STATUS
        self._code_408_1 = codes.CODE_408_1
        self._code_409_status = codes.CODE_409_STATUS
        self._code_409_1 = codes.CODE_409_1
        self._code_410_status = codes.CODE_410_STATUS
        self._code_410_1 = codes.CODE_410_1
        self._code_411_status = codes.CODE_411_STATUS
        self._code_411_1 = codes.CODE_411_1
        self._code_412_status = codes.CODE_412_STATUS
        self._code_412_1 = codes.CODE_412_1
        self._code_413_status = codes.CODE_413_STATUS
        self._code_413_1 = codes.CODE_413_1
        self._code_414_status = codes.CODE_414_STATUS
        self._code_414_1 = codes.CODE_414_1
        self._code_415_status = codes.CODE_415_STATUS
        self._code_415_1 = codes.CODE_415_1
        self._code_416_status = codes.CODE_416_STATUS
        self._code_416_1 = codes.CODE_416_1
        self._code_417_status = codes.CODE_417_STATUS
        self._code_417_1 = codes.CODE_417_1
        self._code_422_status = codes.CODE_422_STATUS
        self._code_422_1 = codes.CODE_422_1
        self._code_423_status = codes.CODE_423_STATUS
        self._code_423_1 = codes.CODE_423_1
        self._code_424_status = codes.CODE_424_STATUS
        self._code_424_1 = codes.CODE_424_1
        self._code_428_status = codes.CODE_428_STATUS
        self._code_428_1 = codes.CODE_428_1
        self._code_429_status = codes.CODE_429_STATUS
        self._code_429_1 = codes.CODE_429_1
        self._code_431_status = codes.CODE_431_STATUS
        self._code_431_1 = codes.CODE_431_1
        self._code_444_status = codes.CODE_444_STATUS
        self._code_444_1 = codes.CODE_444_1
        self._code_451_status = codes.CODE_451_STATUS
        self._code_451_1 = codes.CODE_451_1

    @property
    def CODE_400_STATUS(self):
        """400 상태 코드를 반환합니다.
        """
        return self._code_400_status

    @property
    def CODE_400_1(self):
        """Returns : 'bad request'

        요청의 구문이 잘못되었다.
        클라이언트가 모르는 4xx 계열 응답 코드가 반환된 경우에도
        클라이언트는 400과 동일하게 처리하도록 규정하고 있습니다.
        """
        return self._code_400_1

    @property
    def CODE_401_STATUS(self):
        """401 상태 코드를 반환합니다.
        """
        return self._code_401_status

    @property
    def CODE_401_1(self):
        """Returns : 'unauthorized'

        지정한 리소스에 대한 액세스 권한이 없다.
        응답 헤더 WWW-Authenticate에 필요한 인증 방식을 지정합니다.
        """
        return self._code_401_1

    @property
    def CODE_402_STATUS(self):
        """402 상태 코드를 반환합니다.
        """
        return self._code_402_status

    @property
    def CODE_402_1(self):
        """Returns : 'payment required'

        지정한 리소스를 액세스하기 위해서는 결제가 필요하다.
        이 응답 코드는 실제로는 사용되지 않습니다.
        """
        return self._code_402_1

    @property
    def CODE_403_STATUS(self):
        """403 상태 코드를 반환합니다.
        """
        return self._code_403_status

    @property
    def CODE_403_1(self):
        """Returns : 'forbidden'

        지정한 리소스에 대한 액세스가 금지되었다.
        401 인증 처리 이외의 사유로 리소스에 대한 액세스가 금지되었음을 의미합니다.
        리소스의 존재 자체를 은폐하고 싶은 경우는 404 응답 코드를 사용할 수 있습니다.
        """
        return self._code_403_1

    @property
    def CODE_404_STATUS(self):
        """404 상태 코드를 반환합니다.
        """
        return self._code_404_status

    @property
    def CODE_404_1(self):
        """Returns : 'not found'

        지정한 리소스를 찾을 수 없다.
        """
        return self._code_404_1

    @property
    def CODE_405_STATUS(self):
        """405 상태 코드를 반환합니다.
        """
        return self._code_405_status

    @property
    def CODE_405_1(self):
        """Returns : 'method not allowed'

        요청한 URI가 지정한 메소드를 지원하지 않는다.
        응답 헤더 Allow에 이 URI가 지원하는 메소드 목록을 기록합니다.
        """
        return self._code_405_1

    @property
    def CODE_406_STATUS(self):
        """406 상태 코드를 반환합니다.
        """
        return self._code_406_status

    @property
    def CODE_406_1(self):
        """Returns : 'not acceptable'

        클라이언트가 Accept-* 헤더에 지정한 항목에 관해 처리할 수 없다.
        응답 바디에는 300 응답처럼 서버가 수용 가능한 다른 선택지 리스트가 기록됩니다.
        """
        return self._code_406_1

    @property
    def CODE_407_STATUS(self):
        """407 상태 코드를 반환합니다.
        """
        return self._code_407_status

    @property
    def CODE_407_1(self):
        """Returns : 'bad request'

        클라이언트는 프록시 서버에 인증이 필요하다.
        프록시 서버의 응답 헤더 Proxy-Authenticate에 필요한 인증 방식을 지정합니다.
        """
        return self._code_407_1

    @property
    def CODE_408_STATUS(self):
        """408 상태 코드를 반환합니다.
        """
        return self._code_408_status

    @property
    def CODE_408_1(self):
        """Returns : 'request timeout'

        요청을 기다리다 서버에서 타임아웃하였다.
        """
        return self._code_408_1

    @property
    def CODE_409_STATUS(self):
        """409 상태 코드를 반환합니다.
        """
        return self._code_409_status

    @property
    def CODE_409_1(self):
        """Returns : 'conflict'

        서버가 요청을 수행하는 중에 충돌이 발생하였다.
        예를 들어 사용자명을 new_name으로 변경하려 하였지만,
        서버에 이미 new_name이라는 사용자가 존재하는 경우입니다.
        응답 헤더 Location에는 충돌이 발생한 리소스의 URI를 기록합니다.
        """
        return self._code_409_1

    @property
    def CODE_410_STATUS(self):
        """410 상태 코드를 반환합니다.
        """
        return self._code_410_status

    @property
    def CODE_410_1(self):
        """Returns : 'Gone'


        지정한 리소스가 이전에는 존재하였지만, 현재는 존재하지 않는다.
        예를 들어 기간이 한정된 프로모션 사이트가 사라진 경우 사용할 수 있는 응답 코드입니다.
        """
        return self._code_410_1

    @property
    def CODE_411_STATUS(self):
        """411 상태 코드를 반환합니다.
        """
        return self._code_411_status

    @property
    def CODE_411_1(self):
        """Returns : 'length required'

        요청 헤더에 Content-Length를 지정해야 한다.
        """
        return self._code_411_1

    @property
    def CODE_412_STATUS(self):
        """412 상태 코드를 반환합니다.
        """
        return self._code_412_status

    @property
    def CODE_412_1(self):
        """Returns : 'precondition failed'

        If-Match와 같은 조건부 요청에서 지정한 사전 조건이 서버와 맞지 않는다.
        """
        return self._code_412_1

    @property
    def CODE_413_STATUS(self):
        """413 상태 코드를 반환합니다.
        """
        return self._code_413_status

    @property
    def CODE_413_1(self):
        """Returns : 'request entity too large'

        요청 메시지가 너무 크다.
        서버는 접속을 끊습니다.
        """
        return self._code_413_1

    @property
    def CODE_414_STATUS(self):
        """414 상태 코드를 반환합니다.
        """
        return self._code_414_status

    @property
    def CODE_414_1(self):
        """Returns : 'request-URI too large'

        요청 URI가 너무 길다.
        """
        return self._code_414_1

    @property
    def CODE_415_STATUS(self):
        """415 상태 코드를 반환합니다.
        """
        return self._code_415_status

    @property
    def CODE_415_1(self):
        """Returns : 'unsupported media type'

        클라이언트가 지정한 미디어 타입을 서버가 지원하지 않는다.
        예를 들어 서버가 지원하는 이미지는 JPG, PNG뿐인데
        클라이언트가 GIF 형식의 이미지를 요청하는 경우입니다.
        """
        return self._code_415_1

    @property
    def CODE_416_STATUS(self):
        """416 상태 코드를 반환합니다.
        """
        return self._code_416_status

    @property
    def CODE_416_1(self):
        """Returns : 'range not satisfiable'

        클라이언트가 지정한 리소스의 범위가 서버의 리소스 사이즈와 맞지 않는다.
        """
        return self._code_416_1

    @property
    def CODE_417_STATUS(self):
        """417 상태 코드를 반환합니다.
        """
        return self._code_417_status

    @property
    def CODE_417_1(self):
        """Returns : 'expectation failed'

        클라이언트가 지정한 Expect 헤더를 서버가 이해할 수 없다.
        """
        return self._code_417_1

    @property
    def CODE_422_STATUS(self):
        """422 상태 코드를 반환합니다.
        """
        return self._code_422_status

    @property
    def CODE_422_1(self):
        """Returns : 'unprocessable entity'

        (WebDAV) 클라이언트가 송신한 XML이 구문은 맞지만, 의미상 오류가 있다.
        """
        return self._code_422_1

    @property
    def CODE_423_STATUS(self):
        """423 상태 코드를 반환합니다.
        """
        return self._code_423_status

    @property
    def CODE_423_1(self):
        """Returns : 'locked'

        (WebDAV) 지정한 리소스는 잠겨있다.
        """
        return self._code_423_1

    @property
    def CODE_424_STATUS(self):
        """424 상태 코드를 반환합니다.
        """
        return self._code_424_status

    @property
    def CODE_424_1(self):
        """Returns : 'failed dependency'

        (WebDAV) 다른 작업의 실패로 인해 본 요청도 실패하였다.
        """
        return self._code_424_1

    @property
    def CODE_426_STATUS(self):
        """426 상태 코드를 반환합니다.
        """
        return self._code_426_status

    @property
    def CODE_426_1(self):
        """Returns : 'upgraded required'

        클라이언트의 프로토콜의 업그레이드가 필요하다.
        응답에 Upgrade 헤더를 보내 필요한 프로토콜을 알려 줍니다.
        """
        return self._code_426_1

    @property
    def CODE_428_STATUS(self):
        """428 상태 코드를 반환합니다.
        """
        return self._code_428_status

    @property
    def CODE_428_1(self):
        """Returns : 'precondition required'

        If-Match와 같은 사전조건을 지정하는 헤더가 필요하다.
        If-Match 헤더가 있지만, 맞지 않는 경우는 412 응답을 보냅니다.
        """
        return self._code_428_1

    @property
    def CODE_429_STATUS(self):
        """429 상태 코드를 반환합니다.
        """
        return self._code_429_status

    @property
    def CODE_429_1(self):
        """Returns : 'too many requests'

        클라이언트가 주어진 시간 동안 너무 많은 요청을 보냈다.
        요청의 속도를 제한할 때 사용합니다.
        응답에 Retry-After 헤더를 보내 얼마나 기다릴지를 알려 줄 수 있습니다.
        """
        return self._code_429_1

    @property
    def CODE_431_STATUS(self):
        """431 상태 코드를 반환합니다.
        """
        return self._code_431_status

    @property
    def CODE_431_1(self):
        """Returns : 'request header fields too large'

        헤더의 길이가 너무 크다.
        헤더의 전체 크기가 크거나 또는 하나의 헤더가 매우 큰 경우입니다.
        보통 Referer URL이 길거나 쿠키 항목이 많은 경우입니다.
        """
        return self._code_431_1

    @property
    def CODE_444_STATUS(self):
        """444 상태 코드를 반환합니다.
        """
        return self._code_444_status

    @property
    def CODE_444_1(self):
        """Returns : 'connection closed without response'

        (NGINX) 응답을 보내지 않고 연결을 종료하였다.
        보통 악의적인 요청에 대해서 사용하며 클라이언트에서는 응답
        을 볼 수 없고 Nginx 로그에는 나타납니다.
        """
        return self._code_444_1

    @property
    def CODE_451_STATUS(self):
        """451 상태 코드를 반환합니다.
        """
        return self._code_451_status

    @property
    def CODE_451_1(self):
        """Returns : 'unavailable for legal reasons'

        법적으로 문제가 있는 리소스를 요청하였다.
        """
        return self._code_451_1
