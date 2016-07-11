from celery.task import periodic_task
from datetime import timedelta
from api import all_hotels
from djcelery import celery

@periodic_task(run_every = timedelta(seconds = 20))
def test():
	all_hotels()
	print "all_hotels work!"

@periodic_task(run_every = timedelta(seconds = 30))
def test2():
	print "is works! seconds = 30"

@celery.task
def add(x, y):
	a = x + y
	print 'result {0}'.format(a)	

		    

