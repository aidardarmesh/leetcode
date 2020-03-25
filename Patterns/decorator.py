class Component:
    """
    Component int-ce that defines which methods can be decorated
    """
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component
    
    def get_component(self):
        return self._component
    
    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self.get_component().operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self.get_component().operation()})"


def client_code(component):
    print(f"RESULT: {component.operation()}")


if __name__ == '__main__':
    real_component = ConcreteComponent()
    client_code(real_component)

    decorated_a = ConcreteDecoratorA(real_component)
    decorated_b = ConcreteDecoratorB(decorated_a)
    client_code(decorated_b)
