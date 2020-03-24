from typing import Any

class Builder:
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """
    def produce_part_a(self) -> None:
        pass

    def produce_part_b(self) -> None:
        pass

    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._product = Product1()
    
    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")
    
    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.
    """
    def __init__(self) -> None:
        self._parts = []
    
    def add(self, part: Any) -> None:
        self._parts.append(part)
    
    def list_parts(self) -> None:
        print(', '.join(self._parts))


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration, therefore optional.
    """
    def __init__(self) -> None:
        self._builder = None
    
    def set_builder(self, builder: Builder) -> None:
        self._builder = builder
    
    def get_builder(self) -> Builder:
        return self._builder
    
    def build_mvp(self) -> None:
        self._builder.produce_part_a()
    
    def build_full(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()


if __name__ == "__main__":
    director = Director()
    director.set_builder(ConcreteBuilder1())

    print("Standard product:")
    director.build_mvp()
    director.get_builder()._product.list_parts()
    director.get_builder().reset()

    print("Extended product:")
    director.build_full()
    director.get_builder()._product.list_parts()
    director.get_builder().reset()

    print("Custom product:")
    builder = director.get_builder()
    builder.produce_part_a()
    builder.produce_part_b()
    builder._product.list_parts()
