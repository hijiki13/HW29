from abc import ABC, abstractmethod

class AbstractTagFactory(ABC):
    @abstractmethod
    def create_tag(self):
        pass

class ConcreteTagFactory(AbstractTagFactory):
    def create_tag(self, name, paired):
        if paired:
            return PairTag(name)
        else:
            return NotPairTag(name)

class AbstractTag(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def show_tag(self):
        pass

class PairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    def show_tag(self):
        return f'<{self.name}> </{self.name}>'

class NotPairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    def show_tag(self):
        return f'<{self.name}>'

to_create = [('div', True), ('input', False), ('table', True), ('img', False), ('br', False), ('ul', True)]
factory = ConcreteTagFactory()

for el in to_create:
    tag = factory.create_tag(el[0], el[1])

    print(tag.show_tag())
    print(type(tag))
    print()