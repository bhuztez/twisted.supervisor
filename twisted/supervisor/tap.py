from twisted.python import usage
from twisted.application import strports

from twisted.supervisor import service


class Options(usage.Options):
    pass


def makeService(config):
    # see http://twistedmatrix.com/documents/current/core/howto/application.html
    # for MultiService

    # root = resource.Resource()
    # top = Top()
    # top.putSubHandler('supervisor', Supervisor())
    # root.putChild('RPC2', top)
    # return strports.service("9001", server.Site(root))
    
    return service.Supervisor({})

