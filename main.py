# Через абстрактную фабрику релизовать создание объектов тегов html.
# Парные теги реализуются через фабрику PairTagFactory, непарные через NotPairTagFactory
#------------------------
from abc import ABC, abstractmethod

class AbstractTagFactory(ABC):
    @abstractmethod
    def create_tag(self):
        pass

class PairTagFactory(AbstractTagFactory):
    def create_tag(self, name):
        return PairTag(name)

class NotPairTagFactory(AbstractTagFactory):
    def create_tag(self, name):
        return NotPairTag(name)

class AbstractTag(ABC):
    def __init__(self, name) -> None:
        self._name = name

    # @abstractmethod
    # def show_tag(self):
    #     pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class PairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    # def show_tag(self):
    #     return f'<{self._name}> </{self._name}>'

    def __str__(self) -> str:
        return f'<{self._name}> </{self._name}>'

class NotPairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    # def show_tag(self):
    #     return f'<{self._name}>'

    def __str__(self) -> str:
        return f'<{self._name}>'

to_create = [('div', True), ('input', False), ('table', True), ('img', False), ('br', False), ('ul', True)]
pair_factory = PairTagFactory()
unpair_factory = NotPairTagFactory()

# factory
for el in to_create:
    if el[1]:
        tag = pair_factory.create_tag(el[0])
    else:
        tag = unpair_factory.create_tag(el[0])

    print(tag)
    print(type(tag))
    print()

# just tag
test = PairTag('html')
print(test)
print(type(test))