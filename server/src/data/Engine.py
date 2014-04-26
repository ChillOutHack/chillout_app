import sqlite3


connection = sqlite3.connect('database.db')
#
#class Engine(object):
#
#    def __init__(self):
#        self.connection = sqlite3.connect('database.db')
#
#c = conn.cursor()
#c.execute("INSERT INTO events VALUES (0, 99.2, 1092941468, 95.4, 3.8)")
#conn.commit()
#
#c.execute("SELECT * FROM events")
#print c.fetchone()
#
#conn.close()