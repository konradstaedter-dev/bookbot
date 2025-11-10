def count_words(text):
    words = text.split()
    return len(words)

def sort_on(item):
    return item["num"]

def sortierer(character_dict):
    directories_list=[]
    for i in character_dict:
        d={"char":i,"num":character_dict[i]}
        directories_list.append(d)
    key=sort_on(directories_list[1])
    directories_list.sort(reverse=True, key=sort_on)

    for i in range(0, len(directories_list)):
        print(f"{directories_list[i]["char"]}: {directories_list[i]["num"]}")
    x="erledigt"
    return x