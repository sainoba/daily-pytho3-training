#user.py

from .library import Base

# Make sure that if self.bar doesn't exist a NotImplementedError
# exception is thrown.
# you can't modify baz()
# you can't modify library.py for this


class Derived(Base):
    def baz(self):
        return "baz" + self.bar()
