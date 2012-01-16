from twisted.application.service import ServiceMaker

TwistedSupervisor = ServiceMaker(
    "Twisted supervisor clone",
    "twisted.supervisor.tap",
    "Twisted supervisor clone",
    "supervisor")

