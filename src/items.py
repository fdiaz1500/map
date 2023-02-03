class Weapon:
    def __init__(self):
        raise NotImplementedError('Do note create raw Weapon objects.')

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.description = 'A fist-sized rock, suitable for throwing.'
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.description = 'A small dagger with some rust.'
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty Sword'
        self.description = 'A decent sword for starters.'
        self.damage = 20