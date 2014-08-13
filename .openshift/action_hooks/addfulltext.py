import MySQLdb, os

conn = MySQLdb.connect(host=os.environ['OPENSHIFT_MYSQL_DB_HOST'], user='brandon',
    db=os.environ['OPENSHIFT_APP_NAME'], port=os.environ['OPENSHIFT_MYSQL_DB_PORT'])
c = conn.cursor()

c.execute('ALTER TABLE database_song ADD FULLTEXT(title, artist, themes, lyrics)')

c.close()