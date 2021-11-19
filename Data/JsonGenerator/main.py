import random

import names
import urllib.request

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"

class JSON:
    def __init__(self):
        self.fileName = "books.json"
        self.length = 10000
        self.index = "books"
        self.mainName = "author"
        self.wordList = "theme"
        self.nameList = "characters"
        self.intName = "year"
        self.mainWord = "title"

        response = urllib.request.urlopen(word_url)
        long_txt = response.read().decode()
        self.words = long_txt.splitlines()


    def createJSON(self):
        file = open(self.fileName, "a")

        for i in range(self.length):
            random_genre1 = self.words[random.randint(0, len(self.words))-1]
            random_genre2 = self.words[random.randint(0, len(self.words))-1]
            random_tile = self.words[random.randint(0, len(self.words))-1] + " " + self.words[random.randint(0, len(self.words))-1]
            random_year = random.randint(1700, 2022)

            file.write('{ "index" : { "_index": "' + self.index + '", "_id" : "' + str(i) + '" } }\n')

            file.write('{"' + self.mainName + '": "' + names.get_full_name() + '", ')
            file.write('"' + self.wordList + '": ["' + random_genre1 + '", "' + random_genre2 + '"], ')
            file.write('"' + self.intName + '": ' + str(random_year) + ', ')
            file.write('"' + self.nameList + '": ["' + names.get_full_name() + '", "' + names.get_full_name() + '", "' + names.get_full_name() + '"], ')
            file.write('"' + self.mainWord + '": "' + random_tile + '"}\n')


if __name__ == '__main__':
    j = JSON()
    j.createJSON()


