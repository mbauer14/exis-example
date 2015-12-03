import os

from rabcorelib.pyriffle import FabricSession
from twisted.internet.defer import inlineCallbacks, returnValue, Deferred


class ExampleSession(FabricSession):
    @inlineCallbacks
    def onJoin(self, details):
        yield self.register(self.hello, "hello#details")

    def hello(self, details):
        caller = details.get("caller", "anonymous")
        return "Hello, {}".format(caller)


if __name__ == "__main__":
    ws_url = os.environ['WS_URL']
    domain = os.environ['DOMAIN']

    ExampleSession.start(unicode(ws_url), unicode(domain), start_reactor=True)
