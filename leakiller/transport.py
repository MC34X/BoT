# -*- coding: utf-8 -*-from io import BytesIO
from io import BytesIO
from six.moves import urllib, http_client
import os, socket, sys, warnings, base64, time, json, asyncio, six

from thrift.transport.TTransport import TTransportBase
try:
    from thrift.protocol import fastbinary
except ImportError:
    fastbinary = None
class TPersistentHttpClient(TTransportBase):
    def __init__(self, uri_or_host, port=None, path=None):
        if port is not None:
            warnings.warn(
                "gunakan THttpClient di sini('http://host:port/path') syntax",
                DeprecationWarning,
                stacklevel=2)
            self.host = uri_or_host
            self.port = port
            assert path
            self.path = path
            self.scheme = 'http'
        else:
            parsed = urllib.parse.urlparse(uri_or_host)
            self.scheme = parsed.scheme
            assert self.scheme in ('http', 'https')
            if self.scheme == 'http':
                self.port = parsed.port or http_client.HTTP_PORT
            elif self.scheme == 'https':
                self.port = parsed.port or http_client.HTTPS_PORT
            self.host = parsed.hostname
            self.path = parsed.path
            if parsed.query:
                self.path += '?%s' % parsed.query
        proxy = None
        self.realhost = self.realport = self.proxy_auth = None
        self.__wbuf = BytesIO()
        self.__http = None
        self.__http_response = None
        self.__timeout = None
        self.__custom_headers = None
        self.__time = time.time()
        self.__loop = 0
    @staticmethod
    def basic_proxy_auth_header(proxy):
        if proxy is None or not proxy.username:
            return None
        ap = "%s:%s" % (urllib.parse.unquote(proxy.username),
                        urllib.parse.unquote(proxy.password))
        cr = base64.b64encode(ap).strip()
        return "Basic " + cr
    def using_proxy(self):
        return self.realhost is not None
    def open(self):
        if self.scheme == 'http':
            self.__http = http_client.HTTPConnection(self.host, self.port)
        elif self.scheme == 'https':
            self.__http = http_client.HTTPSConnection(self.host, self.port)
    def close(self):
        self.__http.close()
        self.__http = None
        self.__http_response = None
    def isOpen(self):
        return self.__http is not None
    def setTimeout(self, ms):
        if not hasattr(socket, 'getdefaulttimeout'):
            raise NotImplementedError
        if ms is None:
            self.__timeout = None
        else:
            self.__timeout = ms / 1000.0
    def setCustomHeaders(self, headers):
        self.__custom_headers = headers
    def read(self, sz):
        return self.__http_response.read(sz)
    def write(self, buf):
        self.__wbuf.write(buf)
    def __withTimeout(f):
        def _f(*args, **kwargs):
            orig_timeout = socket.getdefaulttimeout()
            socket.setdefaulttimeout(args[0].__timeout)
            try:
                result = f(*args, **kwargs)
            finally:
                socket.setdefaulttimeout(orig_timeout)
            return result
        return _f
    def flush(self):
        if self.__loop <= 2:
            if self.isOpen(): self.close()
            self.open(); self.__loop += 1
        elif time.time() - self.__time > 90:
            self.close(); self.open(); self.__time = time.time()
        data = self.__wbuf.getvalue()
        self.__wbuf = BytesIO()
        self.__http.putrequest('POST', self.path)
        self.__http.putheader('Host', self.host)
        self.__http.putheader('Content-Type', 'application/x-thrift')
        self.__http.putheader('Content-Length', str(len(data)))
        if self.__custom_headers:
            for key, val in six.iteritems(self.__custom_headers):
                self.__http.putheader(key, val)
        self.__http.endheaders()
        self.__http.send(data)
        self.__http_response = self.__http.getresponse()
        self.code = self.__http_response.status
        self.message = self.__http_response.reason
        self.headers = self.__http_response.msg