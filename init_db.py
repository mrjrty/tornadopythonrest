#!/usr/bin/env python
# coding:utf-8

from motorengine import connect
from tornado import gen, ioloop
import config
from data.collections import School


@gen.coroutine
def create_schools():
    schools = [
        {'name': u'junio', 'verifier': u''},
        {'name': u'juninho', 'verifier': u''},
        {'name': u'junao', 'verifier': u''},
    ]

    # School.objects.delete()
    for school in schools:
        yield School(**school).save()


@gen.coroutine
def init_db():
    yield create_schools()

    io_loop.stop()


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.instance()
    connect(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, io_loop=io_loop,
            username=config.DB_USER, password=config.DB_PWD)

    io_loop.add_timeout(1, init_db)
    io_loop.start()

