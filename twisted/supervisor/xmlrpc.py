from twisted.web import xmlrpc, server, resource

import os


class Top(xmlrpc.XMLRPC):
    pass



class Supervisor(xmlrpc.XMLRPC):

    def __init__(self, service):
        xmlrpc.XMLRPC.__init__(self)
        self._service = service


    def xmlrpc_getVersion(self):
        return '3.0'


    def xmlrpc_getSupervisorVersion(self):
        return '3.0'


    def xmlrpc_getAllProcessInfo(self):
        return []


    def xmlrpc_getPID(self):
        return os.getpid()


    def xmlrpc_shutdown(self):
        reactor.callLater(1, reactor.stop)
        return True


    def xmlrpc_restart(self):
        return False



