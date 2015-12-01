import os

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks, returnValue, Deferred


class ExampleSession(ApplicationSession):
    def __init__(self, config=None):
        ApplicationSession.__init__(self, config=config)

        args = config.extra
        self.domain = args['domain']
        self.token = args['token']

    def onChallenge(self, details):
        if details.method == "token":
            return unicode(self.token)
        else:
            return u''

    def onConnect(self):
        self.join(unicode(self.domain), [u"token"], unicode(self.domain))

    @inlineCallbacks
    def onJoin(self, details):
        yield self.register(self.hello, self.domain + "/hello#details")

    def hello(self, details):
        caller = details.get("caller", "anonymous")
        return "Hello, {}".format(caller)


if __name__ == "__main__":
    ws_url = os.environ['WS_URL']

    config = dict()
    config['domain'] = os.environ['DOMAIN']
    config['token'] = os.environ['EXIS_TOKEN']

    runner = ApplicationRunner(url=unicode(ws_url),
            realm=unicode(config['domain']), extra=config)
    runner.run(ExampleSession)
