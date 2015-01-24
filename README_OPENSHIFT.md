Setup Openshift
==============

In order to setup Openshift, run these from terminal, possibly with "--app [app name]" at the end:

```
# to set up AWS keys
$ rhc env set AWS_ACCESS_KEY_ID=<access key>
$ rhc env set AWS_SECRET_ACCESS_KEY=<secret key>
$ rhc env set AWS_STORAGE_BUCKET_NAME=<bucket name>
$ rhc env set MAILGUN_KEY=<mailgun api key>
$ rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=site/site_settings/wsgi.py
```

Also, to reset up domain hosting (if need be), use

```
$ rhc alias add [app name] [sub-domain].[domain]
```
