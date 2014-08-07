from setuptools import setup

import os

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='worshipdatabase',
      version='1.0',
      description='Database of worship songs',
      author='Brandon Chinn',
      author_email='brandonchinn178@berkeley.edu',
      url='brandonchinn178.github.io',
      install_requires=open('requirements.txt').readlines(),
)

