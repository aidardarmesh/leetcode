class Context:

    def __init__(self, strategy):
        self._strategy = strategy
    
    def do_business_logic(self):
        return self._strategy.update([1,4,2,3,5])


class Strategy:

    def update(self):
        pass


class ConcreteStrategyA(Strategy):

    def update(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):

    def update(self, data):
        return list(reversed(sorted(data)))


if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    print(context.do_business_logic())
    context._strategy = ConcreteStrategyB()
    print(context.do_business_logic())
