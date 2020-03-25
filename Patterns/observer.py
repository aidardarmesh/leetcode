from random import randrange


class Subject:
    """
    Subject int-ce sets methods to manage subscribers
    """
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


class Observer:
    """
    Observer int-ce sets method update used by Subject
    """
    def update(self, subject):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._state = 0
        self._observers = []
    
    def get_state(self):
        return self._state

    def attach(self, observer):
        print("Observer has been attached")
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        print("Notifying observers")
        for observer in self._observers:
            observer.update(self)
        
    def do_business_logic(self):
        print("Changing state of subject")
        self._state = randrange(0, 10)

        print(f"State has been changed to {self._state}")
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject):
        if subject.get_state() > 3:
            print("ConcreteObserverA: reacted to event")

class ConcreteObserverB(Observer):
    def update(self, subject):
        if subject.get_state() >= 0 and subject.get_state() <= 3:
            print("ConcreteObserverA: reacted to event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.do_business_logic()
    subject.do_business_logic()

    subject.detach(observer_a)

    subject.do_business_logic()
