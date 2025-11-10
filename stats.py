def count_words(text):
    words = text.split()
    return len(words)

def sort_on(item):
    return item["num"]

def sortierer(character_dict):
    directories_list=[]
    for i in character_dict:
        directories_list.append({"char":i,"num":character_dict[i]})
    key=sort_on(directories_list[1])
    directories_list.sort(reverse=True, key=sort_on)

    for i in range(0, len(directories_list)):
        print(f"{directories_list[i]["char"]}: {directories_list[i]["num"]}")
    return "erledigt"