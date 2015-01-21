Setup AWS
=========

In order to setup AWS, ssh into openshift app, and run:

```
$ rhc env set AWS_ACCESS_KEY_ID=<access key>
$ rhc env set AWS_SECRET_ACCESS_KEY=<secret key>
$ rhc env set AWS_STORAGE_BUCKET_NAME=<bucket name>
```