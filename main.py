from stats import count_words,sortierer
import sys

def get_book_text(filepath):
    with open(filepath) as datei:
        text = datei.read()
    return text


    
def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts 
    

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    wortzahl = count_words(text)
    print(f"Found {wortzahl} total words")
    character_dict = count_characters(text)
    
    print(sortierer(character_dict))
    


if __name__ == "__main__":
    main()