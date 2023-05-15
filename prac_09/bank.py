class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []
        self.band = []

    def __str__(self):
        line = ",".join(self.band)
        return f"{self.name} ({line})"

    def add(self, musician):
        self.musicians.append(musician)
        self.band.append(musician.__str__())

    def play(self):
        for musician in self.musicians:
            if not musician.instruments:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing {musician.instruments}")