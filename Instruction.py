class Instruction(object):
    def __init__(self, rotation, distance, iterations=1):
        self.rotation = rotation
        self.distance = distance
        self.iterations = iterations

    # used in the ListBox to make instructions user-readable
    def __str__(self):
        plurality = ""
        if self.iterations > 1:
            plurality = 's'

        return "Rotate: {} deg; Move; {} px {} time{}".format(self.rotation, self.distance, self.iterations, plurality)
