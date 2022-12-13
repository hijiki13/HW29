# Через абстрактную фабрику релизовать создание объектов тегов html.
# Парные теги реализуются через фабрику PairTagFactory, непарные через NotPairTagFactory

# Где должно быть условие для создавания элемента класса PairTagFactory или NotPairTagFactory? 
# Оно вообще должно быть? Пользователь должен создавать только один объект factory, а тип фабрики выбирается по передаваемым переменным? (True -> Paired; False -> UnPaired)
# __init__ должен быть в моей абстрактной фабрике??? И в ней же условие??
# Или как я выполнила? При создании ты явно указываешь какой тег надо. (Если через примеры с фигурами, это как Rectangle(), Circle(), но у меня парные и не парные теги)
# Как Клиент вообще может взаимодействовать с абстрактными классами, если они ничего не делают?! Или имеется в виду неявное взаимодействие через потомков?
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

    @abstractmethod
    def show_tag(self):
        pass

class PairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    def show_tag(self):
        return f'<{self._name}> </{self._name}>'

class NotPairTag(AbstractTag):
    def __init__(self, name) -> None:
        super().__init__(name)

    def show_tag(self):
        return f'<{self._name}>'

to_create = [('div', True), ('input', False), ('table', True), ('img', False), ('br', False), ('ul', True)]

# factory
for el in to_create:
    if el[1]:
        tag = PairTagFactory().create_tag(el[0])
    else:
        tag = NotPairTagFactory().create_tag(el[0])

    print(tag.show_tag())
    print(type(tag))
    print()

# just tag
test = PairTag('html')
print(test.show_tag())
print(type(test))