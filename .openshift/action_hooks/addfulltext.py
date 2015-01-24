import MySQLdb, os

conn = MySQLdb.connect(
    host=os.environ['OPENSHIFT_MYSQL_DB_HOST'],
    user=os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
    passwd=os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
    db=os.environ['OPENSHIFT_APP_NAME'],
    port=int(os.environ['OPENSHIFT_MYSQL_DB_PORT'])
)
c = conn.cursor()

c.execute('ALTER TABLE database_song ADD FULLTEXT (title)')
c.execute('ALTER TABLE database_song ADD FULLTEXT (artist)')
c.execute('ALTER TABLE database_song ADD FULLTEXT (themes)')
c.execute('ALTER TABLE database_song ADD FULLTEXT (lyrics)')
conn.commit()
conn.close()