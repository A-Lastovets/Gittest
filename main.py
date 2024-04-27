def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_name, words_count):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Numbers: {words_count}")

def count_words(text):
    words_count = text.split()
    
    return len(words_count)


def main(input, output):
    text = read_file(input)
    words_count = count_words(text)
    print(words_count)
    write_file(output, words_count)

if __name__ == "__main__":
    main("input_file.txt", "output_file.txt")