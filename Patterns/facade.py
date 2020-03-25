class Facade:
    """
    Provides simple int-ce to complex logic of several systems
    """
    def __init__(self, subsystem_1, subsystem_2):
        self._subsystem_1 = subsystem_1
        self._subsystem_2 = subsystem_2

    def operation(self):
        res = []
        res.append("Facade initializes subsystems:")
        res.append(self._subsystem_1.boot())
        res.append(self._subsystem_2.boot())
        res.append("Facade orders subsystems to perform actions:")
        res.append(self._subsystem_1.go())
        res.append(self._subsystem_2.fire())

        return "\n".join(res)


class Subsystem_1:
    def boot(self):
        return "Subsystem_1: Ready!"
    
    def go(self):
        return "Subsystem_1: Go!"


class Subsystem_2:
    def boot(self):
        return "Subsystem_2: Ready!"
    
    def fire(self):
        return "Subsystem_2: Fire!"


def client_code(facade):
    print(facade.operation())


if __name__ == '__main__':
    facade = Facade(Subsystem_1(), Subsystem_2())
    client_code(facade)
