class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance:
            raise Exception("This is Singleton!")

        Singleton.__instance = self

    @staticmethod
    def get_instance():
        if not Singleton.__instance:
            Singleton()
        
        return Singleton.__instance

s = Singleton()
print(s)
print(Singleton.get_instance() == s)
s = Singleton()
print("Exception didn't raise")
