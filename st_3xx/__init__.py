# /***************************************
# * date         : 20231201
# * author       : parkjungwon (1)
# * code number  : s_--1
# ***************************************/
# /***************************************
# * note
# * 1XX: Redirection( 리다이렉션 )
# * 완전한 처리를 위해서 추가 동작이 필요한 경우입니다.
# * 주로 서버의 주소 또는 요청한 URI의 웹 문서가 이동되었으니 그 주소로 다시 시도하라는 의미입니다.
# ***************************************/

from . import codes

class ErrorCodes:
    def __init__(self):
        self._code_300_status = codes.CODE_300_STATUS
        self._code_300_1 = codes.CODE_300_1
        self._code_301_status = codes.CODE_301_STATUS
        self._code_301_1 = codes.CODE_301_1
        self._code_302_status = codes.CODE_302_STATUS
        self._code_302_1 = codes.CODE_302_1
        self._code_303_status = codes.CODE_303_STATUS
        self._code_303_1 = codes.CODE_303_1
        self._code_304_status = codes.CODE_304_STATUS
        self._code_304_1 = codes.CODE_304_1
        self._code_305_status = codes.CODE_305_STATUS
        self._code_305_1 = codes.CODE_305_1
        self._code_307_status = codes.CODE_307_STATUS
        self._code_307_1 = codes.CODE_307_1

    @property
    def CODE_300_STATUS(self):
        """300 상태 코드를 반환합니다.
        """
        return self._code_300_status

    @property
    def CODE_300_1(self):
        """Returns : 'multiple choices'

        선택 항목이 여러개 있다.
        지정한 URI에 대해서 콘텐츠 협상을 수행한 결과 서버에서 콘텐츠를 결정하지 못하고
        클라이언트에게 복수 개의 링크를 응답할 때 사용합니다.
        """
        return self._code_300_1

    @property
    def CODE_301_STATUS(self):
        """301 상태 코드를 반환합니다.
        """
        return self._code_301_status

    @property
    def CODE_301_1(self):
        """Returns : 'moved permanently'

        지정한 리소스가 새로운 URI로 이동하였다.
        이동할 곳의 새로운 URI는 응답 헤더 Location에 기록합니다.
        """
        return self._code_301_1

    @property
    def CODE_302_STATUS(self):
        """302 상태 코드를 반환합니다.
        """
        return self._code_302_status

    @property
    def CODE_302_1(self):
        """Returns : 'found'

        요청한 리소스를 다른 URI에서 찾았다.
        요청한 URI가 없으므로 클라이언트 메소드를 그대로 유지한 채
        응답 헤더 Location에 표시된 다른 URI로 요청을 재송신할 필요가 있습니다.
        302의 의미를 정확하게 개선해서 307을 정의하였으므로 이 응답 코드의 사용은 권장하지 않습니다.
        """
        return self._code_302_1

    @property
    def CODE_303_STATUS(self):
        """303 상태 코드를 반환합니다.
        """
        return self._code_303_status

    @property
    def CODE_303_1(self):
        """Returns : 'see other'

        다른 위치로 요청하라.
        요청에 대한 처리 결과를 응답 헤더 Location에 표시된 URI에서 GET으로 취득할 수 있습니다.
        브라우저의 폼 요청을 POST로 처리하고 그 결과 화면으로 리다이렉트시킬 때 자주 사용하는 응답 코드입니다.
        """
        return self._code_303_1

    @property
    def CODE_304_STATUS(self):
        """304 상태 코드를 반환합니다.
        """
        return self._code_304_status

    @property
    def CODE_304_1(self):
        """Returns : 'not modified'

        마지막 요청 이후 요청한 페이지는 수정되지 않았다.
        If-Modified-Since와 같은 조건부 GET 요청일 때 지정한 리소스가 갱신되지 않았음을 알려 줍니다.
        이 응답 코드에는 바디가 없습니다.
        """
        return self._code_304_1

    @property
    def CODE_305_STATUS(self):
        """305 상태 코드를 반환합니다.
        """
        return self._code_305_status

    @property
    def CODE_305_1(self):
        """Returns : 'use proxy'

        지정한 리소스에 액세스하려면 프록시를 통해야 한다.
        응답 헤더 Location에 프록시의 URI를 기록합니다.
        """
        return self._code_305_1

    @property
    def CODE_307_STATUS(self):
        """307 상태 코드를 반환합니다.
        """
        return self._code_307_status

    @property
    def CODE_307_1(self):
        """Returns : 'temporary redirect'

        임시로 리다이렉션 요청이 필요하다.
        요청한 URI가 없으므로 클라이언트 메소드를 그대로 유지한 채 응답 헤더 Location에 표시된
        다른 URI로 요청을 재송신할 필요가 있습니다. 클라이언트는 향후 요청 시 원래 위치를 계속 사용해야 합니다.
        302의 의미를 정확하게 재정의해서 HTTP/1.1의 307 응답으로 추가되었습니다.
        """
        return self._code_307_1
