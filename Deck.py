import heapq

"""Stores a collection of cards, largely a wrapper for the backing heapq"""
class Deck:

    def __init__(self, fileDeck):
        self.fileDeck = fileDeck

    def get_next_card(self):
        try:
            ret = heapq.heappop(self.fileDeck)
        except IndexError:
            print("End of pQueue reached, deck was empty and shall remain empty, there's no tricking me")
            return None
        ret.seen()

        """Multiply by the golden ratio because its cool, causes the card to be replaced in the heap at a lower priority"""
        # golden = (1 + 5 ** 0.5) / 2
        # ret.difficulty = ret.difficulty * golden

        heapq.heappush(self.fileDeck, ret)

        if ret.timesSeen > 5:
            return None

        return ret
