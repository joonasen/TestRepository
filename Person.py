class Person:
    def __init__(name,age):
        self._name = name
        self._age = age

    @property
    def name(self, _default = None):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @address.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return f'name: {self._name}\nAge: {self._age}'