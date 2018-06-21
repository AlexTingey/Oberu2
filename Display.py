import tkinter as tk
from tkinter import filedialog
from FileParser import FileParser
from Deck import Deck

def main():
    display_main_screen()


def display_main_screen():
    root = tk.Tk()
    root.title("Oberu")
    root.geometry("1000x750")

    #Create the two frames for the text and buttons to be placed onto
    center_frame = tk.Frame(root, width= 500, height=375, pady=250)
    button_frame = tk.Frame(root, width=600, height= 100)


    title = tk.Label(center_frame, text="Oberu", font=("Helvetica", 45))
    title.pack()

    button1 = tk.Button(button_frame, text="Open Deck", font=("Helvetica", 12), command= display_deck_selector, padx=50)
    button2 = tk.Button(button_frame, text="Create Deck", font=("Helvetica", 12), command= display_deck_creator, padx=50)
    button1.pack(side="left")
    button2.pack(side="right")


    center_frame.pack()
    button_frame.pack()
    root.mainloop()

def display_deck_selector():
    file = tk.filedialog.askopenfilename()
    file_reader = FileParser(str(file))
    cards = file_reader.create_deck()
    deck = Deck(cards)

    display_deck(deck, file_reader)

def display_deck_creator():
    file = tk.filedialog.askopenfilename()
    file_reader = FileParser(str(file))

    root = tk.Tk()
    root.title("Oberu")
    root.geometry("1000x750")

    entry_frame = tk.Frame(root, width=500, height=400, pady =100)
    button_frame = tk.Frame(root, width=500, height=400)

    header_label = tk.Label(entry_frame, text="Card Header")
    header_entry = tk.Entry(entry_frame)

    body_label = tk.Label(entry_frame, text="Card Body")
    body_entry = tk.Entry(entry_frame)

    footer_label = tk.Label(entry_frame, text="Card Footer")
    footer_entry = tk.Entry(entry_frame)

    create_card_button = tk.Button(button_frame, text="Create Card", command=lambda: add_card(file_reader, header_entry.get(), body_entry.get(), footer_entry.get()))
    exit_entry_button = tk.Button(button_frame, text="Exit", command=lambda: root.destroy())

    header_label.pack()
    header_entry.pack()
    body_label.pack()
    body_entry.pack()
    footer_label.pack()
    footer_entry.pack()

    create_card_button.pack(side="left")
    exit_entry_button.pack()

    entry_frame.pack()
    button_frame.pack()

    root.mainloop()

def add_card(fileReader, header, body, footer):
    fileReader.add_card(header, body, footer, 1.0, "a")


def display_deck(deck, file):
    root = tk.Tk()
    root.title("Oberu")
    root.geometry("1000x750")

    center_frame = tk.Frame(root, width=500, height=400, pady=250)
    button_frame = tk.Frame(root, width=500, height=100)

    """Create initial labels, update every time button is pressed for every card in the deck"""
    card = deck.get_next_card()
    header_label = tk.Label(center_frame, text=card.header, font=("Helvetica", 24), pady= 20)
    body_label = tk.Label(center_frame, text=card.body, font=("Helvetica", 48), pady= 20)
    footer_label = tk.Label(center_frame, text=card.footer, font=("Helvetica", 24))

    header_label.pack()
    body_label.pack()
    footer_label.pack()

    difficult_button = tk.Button(button_frame, text="Difficult", font=("Helvetica", 12), command= lambda: change_card_display(root, header_label, body_label, footer_label, deck, "difficult", file))
    easy_button = tk.Button(button_frame, text="Easy", font=("Helvetica", 12), command= lambda: change_card_display(root, header_label, body_label, footer_label, deck, "easy", file))
    moderate_button = tk.Button(button_frame, text="Moderate", font=("Helvetica", 12), command= lambda: change_card_display(root, header_label, body_label, footer_label, deck, "moderate", file))

    difficult_button.pack(side= "right")
    moderate_button.pack(side="right")
    easy_button.pack(side="right")

    center_frame.pack()
    button_frame.pack()

    root.mainloop()


def change_card_display(root, header_label, body_label, footer_label, deck, difficulty, file_reader):
    card = deck.get_next_card()

    if card is None:
        header_label.config(text="")
        body_label.config(text="End of deck reached")
        footer_label.config(text="")
        root.destroy()
        write_deck_after_completion(deck, file_reader)

    else:
        header_label.config(text=card.header)
        body_label.config(text=card.body)
        footer_label.config(text=card.footer)

        if difficulty == "difficult":
            card.difficulty /= 3.0
        elif difficulty == "easy":
            card.difficulty *= 3.0


def write_deck_after_completion(deck, file_reader):
    print(deck.fileDeck)
    file_reader.write_new_deck(deck.fileDeck)

if __name__ == "__main__":
    main()
