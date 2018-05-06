#-*- coding:utf-8 –*-

import synonyms
import MySQLdb

class WordDisambiguation:
    userAndKeyword = {}
    def __init__(self):
        self.userAndKeyword.clear()
        self.readPersonFromDB()

    def addKey(self, key, value):
        if self.userAndKeyword.has_key(key) == False:
            self.userAndKeyword[key] = []
        else:
            self.userAndKeyword[key].append(value)

    def getVal(self, key):
        return self.userAndKeyword[key]

    def compareWord(self, wordA, wordB):
        result = synonyms.compare(wordA, wordB, seg=False)
        return result

    def comparePerson(self, name, wordA):
        if self.userAndKeyword.has_key(name) == False:
            return 0
        count = 0
        for i in wordA:
             t = self.userAndKeyword[name]
             for s in t:
                if self.compareWord(i, s) > 0.5 :
                    count += 1
                    break
        count /= len(wordA)
        return count

    def readPersonFromDB(self):
        db = MySQLdb.connect("localhost", "root", "haochengqian262", "name")
        cursor = db.cursor()
        cursor.execute("select * from keyword2")
        rows = cursor.fetchall()
        for row in rows:
            value = row[2].replace(' ', '')
            value = value.split('||')
            name = row[0].replace(' ', '')
            name = name.split('||')
            for wordA in name:
                for wordB in value:
                    self.addKey(wordA, wordB)





