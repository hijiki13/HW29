from abc import ABC, abstractmethod

class AbstractTagFactory(ABC):

    @abstractmethod
    def create_pair_tag (self):
        pass

    @abstractmethod
    def create_unpair_tag(self):
        pass

class ConcreteTagFactory(AbstractTagFactory):
    def create_pair_tag(self, name):
        return PairTag(name)

    def create_unpair_tag(self, name):
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
    if el[1]:
        tag = factory.create_pair_tag(el[0])
    else:
        tag = factory.create_unpair_tag(el[0])

    print(tag.show_tag())
    print(type(tag))
    print()