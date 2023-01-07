from logger import logging

def _log_proxy_pass(req, res):
    logging.info('[ProxyPass] {} > {}'.format(req.file, res.status_code))


def proxy_pass_action(request):
    pass
