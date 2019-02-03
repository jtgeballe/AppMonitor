"""AppValidator type and supporting functionality"""
from AppMonitor.validatorlib.timer import RepeatTimer
from AppMonitor.validatorlib.uri import UriValidator
from AppMonitor.validatorlib.output import Email
from AppMonitor.validatorlib import intervalutil


class AppValidator:

    def __init__(self, uri, lock, interval=intervalutil.sec_to_next_third_thursday_of_month):
        self.__uri = uri
        self.__interval = interval
        self.__lock = lock

    def start(self):
        RepeatTimer(self.__interval, self._request_uri).start()

    def _request_uri(self):
        uri_validator = UriValidator(self.__uri)
        uri_validator.send_request()
        j = uri_validator.to_json()

        if not uri_validator.is_valid():
            Email(j, self.__lock).send()

        print(uri_validator)
