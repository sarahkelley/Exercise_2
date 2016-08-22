from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        self.counts[word] += 1

        try:

            conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

            cur = conn.cursor()

            cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES (%s, %s)",  (word, self.counts[word]))

            conn.commit()

        except:

            conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

            cur = conn.cursor()

            cur.execute("UPDATE Tweetwordcount set count=%s WHERE word=%s",  (self.counts[word], word))

            conn.commit()        
        
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
