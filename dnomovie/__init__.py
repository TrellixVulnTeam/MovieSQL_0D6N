from __future__ import absolute_import


#This will make sure the app is always imported when
#Django starts so that shared_taks will use this app
from celery import app as celery_app

import pymysql
pymysql.install_as_MySQLdb()

