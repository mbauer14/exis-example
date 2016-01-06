import os

import riffle


class ExampleSession(riffle.Domain):
    def onJoin(self):
        self.register("hello#details", self.hello)

    def hello(self, details):
        caller = details.get("caller", "anonymous")
        print("Received hello from: {}".format(caller))
        return "Hello, {}".format(caller)


if __name__ == "__main__":
    riffle.SetFabric(os.environ['WS_URL'])
    domain = os.environ['DOMAIN']
    ExampleSession(domain).join()
