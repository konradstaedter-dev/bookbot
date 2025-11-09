def get_book_text(filepath):
    with open(filepath) as datei:
        inhalt = datei.read()
    print(inhalt)

def main():
    get_book_text("books/frankenstein.txt")

main()