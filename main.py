from stats import count_words 

def get_book_text(filepath):
    with open(filepath) as datei:
        text = datei.read()
    return text

def count_characters(text):
    text_lower=text.lower()
    lexika={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for buchstabe in text_lower:
        if buchstabe in lexika:
            lexika[buchstabe]+=1
    return lexika
        


def main():
    text = get_book_text("books/frankenstein.txt")
    wortzahl = count_words(text)
    print(f"Found {wortzahl} total words")
    character_dict = count_characters(text)
    print(character_dict)
    


if __name__ == "__main__":
    main()

    """
    python
def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts 
    """