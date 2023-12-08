"""
CP1404/CP5632 Practical
rogramming Language client code.

Estimate: 8 minutes
Actual:   5 minutes

"""


from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]


if __name__ == "__main__":
    main()
