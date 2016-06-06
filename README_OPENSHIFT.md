Setup Openshift
==============

In order to setup Openshift, run these from terminal, possibly with "--app [app name]" at the end:

```
$ rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=site/site_settings/wsgi.py
```

in addition to any other environment variables in `.env`

Also, to reset up domain hosting (if need be), use

```
$ rhc alias add [app name] [sub-domain].[domain]
```

To back up the MySQL database, use

```
mysqldump -h $OPENSHIFT_MYSQL_DB_HOST -P $OPENSHIFT_MYSQL_DB_PORT -u $OPENSHIFT_MYSQL_DB_USERNAME --password="$OPENSHIFT_MYSQL_DB_PASSWORD" --all-databases  > ~/app-deployments/backup.sql
```
