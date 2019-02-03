"""
The URIValidator type checks that the response code of a url falls between 200 and 299.
"""
import urllib.request
from datetime import datetime
from http import HTTPStatus

http_code_format = "{0:0>3}"
datetime_format = "%Y-%m-%d %I:%M:%S %p"


class UriValidator:
    def __init__(self, uri):
        self.__uri = uri
        self.__code = None
        self.__datetime = None

    def __str__(self):
        if not self._has_sent_request():
            return "Request to %s was not made." % self.__uri

        code_str = http_code_format.format(self.__code)
        date_str = self.__datetime.strftime(datetime_format)

        return "DateTime: %s Code: %s URI: %s" % (date_str, code_str, self.__uri)

    def send_request(self):
        request = urllib.request.Request(self.__uri)
        try:
            self.__datetime = datetime.now()
            r = urllib.request.urlopen(request)
            self.__code = r.code
        except urllib.error.HTTPError as e:
            self.__code = e.code

    def is_valid(self):
        if not self._has_sent_request():
            return False

        return HTTPStatus.MULTIPLE_CHOICES > self.__code >= HTTPStatus.OK

    def to_json(self):
        if not self._has_sent_request():
            return {'uri': self.__uri}

        code_str = http_code_format.format(self.__code)
        date_str = self.__datetime.strftime(datetime_format)

        return {'datetime': date_str, 'uri': self.__uri, 'code': code_str}

    def _has_sent_request(self):
        return self.__code is not None and self.__code is not None
