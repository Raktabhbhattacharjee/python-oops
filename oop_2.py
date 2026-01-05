class Example:
    """
    ===================== ACCESS MODIFIER NOTES =====================

    ❌ Python has NO real access modifiers like Java.
       There is no: public / private / protected keyword.

    ✅ Python uses NAMING CONVENTIONS instead.

    Convention meanings:
    --------------------------------------------------
    name        -> PUBLIC (use freely)
    _name       -> PROTECTED (internal use, don't touch from outside)
    __name      -> PRIVATE-ish (name mangling, still accessible)
    --------------------------------------------------

    IMPORTANT:
    Python trusts the programmer ("consenting adults").
    These are NOT enforced by the compiler/interpreter.
    """

    def __init__(self, value):
        # PUBLIC variable
        # Can be accessed from anywhere
        self.public_value = value

        # PROTECTED variable (CONVENTION ONLY)
        # Means: internal use, subclasses allowed
        self._protected_value = value * 2

        # "PRIVATE" variable (NAME MANGLING)
        # Python changes __private_value -> _Example__private_value
        self.__private_value = value * 3

    # ================= INSTANCE METHOD =================
    def show_values(self):
        """
        Normal instance method.
        Uses self (object data).
        """
        print("Public:", self.public_value)
        print("Protected:", self._protected_value)
        print("Private:", self.__private_value)

    # ================= GETTER (PYTHONIC) =================
    @property
    def private_value(self):
        """
        Getter for private variable.
        Access like a variable, not a method.
        """
        return self.__private_value

    # ================= SETTER (PYTHONIC) =================
    @private_value.setter
    def private_value(self, value):
        """
        Setter with validation logic.
        Used only when logic is needed.
        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__private_value = value

    # ================= STATIC METHOD =================
    @staticmethod
    def info():
        """
        Static method:
        - No self
        - Belongs to class
        - Utility / helper logic
        """
        print("This is a static method")
