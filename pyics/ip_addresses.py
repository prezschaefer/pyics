import pyics


class IPAddresses(pyics.Collection):

    path = '/floating-ips'

    def bind(self):
        raise NotImplementedError

    def unbind(self):
        raise NotImplementedError

    def request(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError
