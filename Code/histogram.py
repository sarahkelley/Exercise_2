import sys
import psycopg2
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

lower = sys.argv[1]
upper = sys.argv[2]

cur.execute("SELECT * FROM tweetwordcount WHERE COUNT BETWEEN %s and %s", (int(lower[:-1]), int(upper)))

word = []
count = []
for record in cur:
		word.append(record[0])
		count.append(record[1])
for_graph = pd.DataFrame()
for_graph['word'] = word
for_graph['count'] = count


y_pos = np.arange(len(for_graph['word']))
plt.bar(y_pos, for_graph['count'])
plt.title("Word Frequencies")
list_of_words= for_graph['word']
plt.xticks(y_pos,list_of_words)
plt.xlabel("Words")
plt.ylabel("Count")
plt.savefig('wordhistogram.png')
plt.show()

conn.commit()