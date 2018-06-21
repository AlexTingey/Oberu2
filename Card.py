class Card(object):

    timesSeen = 0

    def __init__(self, header, body, footer, difficulty):
        self.header = header
        self.body = body
        self.footer = footer
        self.difficulty = difficulty

    def seen(self):
        self.timesSeen += 1

    def __repr__(self):
        return "Header: %s Center: %s Footer: %s difficulty: %s" % (self.header, self.body, self.footer, self.difficulty)

    def __lt__(self, other):
        return (self.difficulty < other.difficulty) and (self.timesSeen < other.timesSeen)
