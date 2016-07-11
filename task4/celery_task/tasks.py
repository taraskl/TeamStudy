# from __future__ import absolute_import

# from celery import shared_task


# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)
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

# def delay(self, *args, **kwargs):
#         """Star argument version of :meth:`apply_async`.

#         Does not support the extra options enabled by :meth:`apply_async`.

#         :param \*args: positional arguments passed on to the task.
#         :param \*\*kwargs: keyword arguments passed on to the task.

#         :returns :class:`celery.result.AsyncResult`:

#         """
#     return self.apply_async(args, kwargs)			    

