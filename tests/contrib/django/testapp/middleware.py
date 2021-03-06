class BrokenRequestMiddleware(object):
    def process_request(self, request):
        raise ImportError('request')


class BrokenResponseMiddleware(object):
    def process_response(self, request, response):
        raise ImportError('response')


class BrokenViewMiddleware(object):
    def process_view(self, request, func, args, kwargs):
        raise ImportError('view')


class MetricsNameOverrideMiddleware(object):
    def process_response(self, request, response):
        request._opbeat_transaction_name = 'foobar'
        return response
