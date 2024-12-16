import re

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    content = re.sub(r"[,.=!?;:]", '', content)
                    content = content.replace(' - ', ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        for file_name, words in self.get_all_words().items():
            try:
                positions[file_name] = words.index(word) + 1
            except ValueError:
                positions[file_name] = None
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word)
        return counts

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('text'))
    print(finder2.count('text'))
