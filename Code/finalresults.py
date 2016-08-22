import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("SELECT * FROM tweetwordcount")

#checks if the sys.argv is 1 which means no entry or 2 which means a word was provided
if len(sys.argv)==1:
	list_of_words = []
	for record in cur:
		list_of_words.append(record)
	clean = sorted(list_of_words)
	for item in clean:
		print item
else:
	word_to_find = sys.argv[1]
	for record in cur:
		if word_to_find in record:
			print "There are", record[1], "occurences of the word", record[0]




conn.commit()
