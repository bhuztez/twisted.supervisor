import shlex
from twisted.internet import reactor, protocol
from twisted.application import service


class SubprocessProtocol(protocol.ProcessProtocol):
    pass


class Supervisor(service.Service):


    def __init__(self, config):
        self.config = config
        self.subprocesses = {}


    def startService(self):
        service.Service.startService(self)
        
        for name in self.config:
            self.startProgram(name)


    def stopService(self):
        service.Service.stopService(self)


    def startProgram(self, name):
        command = shlex.split(self.config[name])
        proto = SubprocessProtocol()
        self.subprocesses[name] = self.subprocesses.get(name, []) + [proto]
        reactor.spawnProcess(proto, command[0], command)

        
    def stopProgram(self, name):
        raise NotImplemented


