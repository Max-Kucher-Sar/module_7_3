class WordsFinder:
    def __init__(self, *file):
        self.file_names = list(file)


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            all_words[file_name] = []
            with open(file_name, 'r', encoding='utf-8') as name:
                for string in name:
                    string = string.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for punct in punctuation:
                        string = string.replace(punct, '')

                    all_words[file_name].extend(string.split())
        return all_words

    def find(self, word):
        word = word.lower()
        find_result = {}
        for name, words in self.get_all_words().items():
            position = words.index(word)
            find_result[name] = position + 1
        return find_result

    def count(self, word):
        word = word.lower()
        count_result = {}
        count_num = 0
        for name, words in self.get_all_words().items():
            for count_word in words:
                if word == count_word:
                    count_num += 1
            count_result[name] = count_num

        return count_result






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего