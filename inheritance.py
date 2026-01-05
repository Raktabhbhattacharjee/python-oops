# ============================================================
# NOTE ABOUT PROGRAM ENTRY (READ THIS FIRST)
# ============================================================
"""
JAVA:
- Program starts from: public static void main(String[] args)
- main is:
    * static
    * inside a class
    * called by the JVM
- Objects are created INSIDE main()

PYTHON:
- Program starts from the FILE ITSELF
- No required main method
- No required class
- Code runs top-to-bottom

The line below is NOT a magic method.
It is a RUNTIME CHECK that says:
"Only run this block if this file is executed directly."
"""


# ============================================================
# PARENT CLASS
# ============================================================
class Model:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self._is_trained = False

    def train(self):
        print("Base training logic")
        self._is_trained = True


# ============================================================
# CHILD CLASS (Inheritance)
# ============================================================
class NeuralNetwork(Model):
    def __init__(self, model_name: str, layers: int):
        # super() initializes the parent part of the object
        super().__init__(model_name)
        self.layers = layers

    def train(self):
        # This overrides the parent method
        super().train()
        print(f"Training neural network with {self.layers} layers")


# ============================================================
# PYTHON "MAIN" (BY CONVENTION, NOT REQUIRED)
# ============================================================
def main():
    """
    This function is NOT special to Python.
    We call it 'main' ONLY by convention.

    Think of this as:
    "Where object creation and execution logic lives"
    (similar role to Java's main method)
    """

    # Object creation happens here (like Java main)
    model = NeuralNetwork("AlphaNet", 50)

    # Method calls
    model.train()


# ============================================================
# ENTRY POINT GUARD
# ============================================================
if __name__ == "__main__":
    """
    JAVA:
    - JVM always calls main()

    PYTHON:
    - This condition decides whether main() is called
    - If file is imported → this block is skipped
    - If file is run directly → this block runs
    """

    main()
