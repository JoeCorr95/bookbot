def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    num_of_words = count_words(text)
    # print(f"{num_of_words} words found in the document")
    num_letters = count_letters(text)
    # print(f"{num_letters}")
    report = genereate_report(text)
    for item in report:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)   
    
def count_letters(text):
    count = {}
    for char in text:
        char = char.lower()
        if char.isalpha() is False:
            continue
        if char not in count:
            count[char] = 1
        else: 
            count[char] += 1
    return count

def sort_on(d):
    return d["num"]

def genereate_report(text):
    num_letters = count_letters(text)
    # list_for_report = list(num_letters.items())
    # sorted_list = sorted(list_for_report, key=char)
    
    sorted_list = []
    for ch in num_letters:
            sorted_list.append({"char": ch, "num": num_letters[ch]})
            sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()