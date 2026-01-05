class Example:
    """
    REFERENCE GUIDE: Java-to-Python OOP
    
    JAVA EQUIVALENT:
    - public:    variable_name
    - protected: _variable_name (Convention)
    - private:   __variable_name (Name Mangling)
    """

    def __init__(self, value):
        """
        CONSTRUCTOR: Equivalent to public Example(int value)
        In Python, attributes are created inside __init__ using 'self'.
        """
        # PUBLIC: Can be read/modified from outside.
        self.public_value = value

        # PROTECTED: Signal to developers "Internal use, but subclasses can touch".
        # Unlike Java, the interpreter won't block access, but it's bad practice to touch.
        self._protected_value = value * 2

        # PRIVATE: Triggers 'Name Mangling'.
        # Python renames this internally to _Example__private_value to prevent conflicts.
        self.__private_value = value * 3

    def show_values(self):
        """
        INSTANCE METHOD: Equivalent to public void showValues()
        'self' is the equivalent of 'this' in Java.
        """
        print(f"Public: {self.public_value}")
        print(f"Protected: {self._protected_value}")
        print(f"Private: {self.__private_value}")

    # ============================================================
    # PROPERTY DECORATORS (The Pythonic Getters/Setters)
    # ============================================================

    @property
    def private_value(self):
        """
        GETTER: Equivalent to public int getPrivateValue()
        Access this like a field: print(obj.private_value)
        """
        return self.__private_value

    @private_value.setter
    def private_value(self, value):
        """
        SETTER: Equivalent to public void setPrivateValue(int value)
        Triggered by: obj.private_value = 10
        """
        if value < 0:
            # Equivalent to 'throw new ValueError(...)'
            raise ValueError("Value cannot be negative")
        self.__private_value = value

    # ============================================================
    # STATIC METHOD
    # ============================================================

    @staticmethod
    def info():
        """
        STATIC METHOD: Equivalent to public static void info()
        Does not take 'self' because it doesn't belong to a specific object instance.
        """
        print("This is a static utility method.")

# --- QUICK REFERENCE FOR USAGE ---
# obj = Example(10)          # Instantiate (No 'new' keyword)
# obj.private_value = 20     # Calls @setter
# print(obj.private_value)   # Calls @property getter