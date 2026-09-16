class Sundial:
    def __init__(self):
        self.index = 50
        self.zero_hits = 0

    def _advance(self, steps):
        direction = 1 if steps > 0 else -1
        for _ in range(abs(steps)):
            self.index = (self.index + direction) % 100
            if self.index == 0:
                self.zero_hits += 1

    def command(self, cmd):
        cmd = cmd.strip()
        if not cmd:
            return
        direction = cmd[0].upper()
        amount = int(cmd[1:])
        if direction == "L":
            self._advance(-amount)
        elif direction == "R":
            self._advance(amount)
        else:
            raise ValueError(f"Invalid command: {cmd}")

def process_file(filename):
    s = Sundial()
    with open(filename, "r") as f:
        for line in f:
            s.command(line)
    return s.zero_hits
test = process_file("adventofcode.txt")
print(test)