class School:
    def __init__(self, fishes):
        self.fishes = fishes

    def spawn(self):
        self.fishes.append(Fish(timer=9))

    def advance(self):
        for fish in self.fishes:
            if fish.timer == 0:
                fish.timer = 6
                self.spawn()
            else:
                fish.timer -= 1

    def display(self):
        fishes = ""
        for fish in self.fishes:
            #fishes.append(str(fish.timer))
            fishes += str(fish.timer)+","
        return fishes[:-1]

class Fish:
    def __init__(self, timer):
        self.timer = timer