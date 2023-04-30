class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self. typing = typing
        self. reflection = reflection
        self. year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return(f"{self.name}, "
               f"{self.reflection} Typing, "
               f"Reflection={self.is_dynamic()}, "
               f"First appeared in {self.year} ")
