import MySQLdb, os

conn = MySQLdb.connect(host=os.environ['OPENSHIFT_MYSQL_DB_HOST'],
    db=os.environ['OPENSHIFT_APP_NAME'], port=int(os.environ['OPENSHIFT_MYSQL_DB_PORT']))
c = conn.cursor()

c.execute('ALTER TABLE database_song ADD FULLTEXT(title, artist, themes, lyrics)')
conn.commit()
c.close()