
from Card import Card
import os
import heapq


class FileParser(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def create_deck(self):
        ret = []
        with open(self.filepath, mode="r", encoding="UTF-16") as file:
            text = file.readlines()

        for line in text:
            split_text = line.split()

            header = split_text[0]
            body = split_text[1]
            footer = split_text[2]

            """Put in try block just in case the user accidentally submits a String difficulty"""
            try:
                difficulty = float(split_text[3])
            except ValueError:
                print("Error: card " + header + " expected float for difficulty but received unexpected type")

            new_card = Card(header, body, footer, difficulty)
            ret.append(new_card)

        heapq.heapify(ret)
        return ret

    def add_card(self, header, body, footer, difficulty, write_mode):
        with open(self.filepath, write_mode, encoding="UTF-16") as file_writer:
            file_writer.write("%s %s %s %s \n" % (header, body, footer, difficulty))

    def write_new_deck(self, deck):
        #delete previous file so as to add new file

        try:
            os.remove(self.filepath)

        except OSError:
            print("Error: " + self.filepath + " does not exist")

        for card in deck:
            self.add_card(card.header, card.body, card.footer, card.difficulty, write_mode="a")

    def append_deck(self, deck):

        for card in deck:
            self.add_card(card.header, card.body, card.footer, card.difficulty, write_mode="a")
