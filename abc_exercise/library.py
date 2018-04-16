#library.py

# Make sure classes that inherit from `Base` require to 
# implement `self.baz`. Hint: Use abc
# -

from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def baz(self):
        pass

    def bar(self):
        return "bar"
