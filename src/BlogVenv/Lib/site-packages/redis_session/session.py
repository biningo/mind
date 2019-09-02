#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from uuid import uuid4
from redis_session.model import SessionStore

class RedisResult(object):
    """Redis result parser"""

    def __init__(self, raw):
        self.raw = raw

    @property
    def int(self):
        try:
            return int(self.raw)
        except:
            return 0

    @property
    def bool(self):
        return self.str == 'True'

    @property
    def str(self):
        return '' if self.none else self.raw.decode('utf8')

    @property
    def none(self):
        return self.raw is None

    @property
    def json(self):
        try:
            return json.loads(self.raw)
        except:
            return {}

class Session(object):
    def __init__(self, sessionId, **kwargs):
        super(Session, self).__init__()
        object.__setattr__(self, '_sessionId', sessionId)
        object.__setattr__(self, '_key', SessionStore(kwargs).key)
        self.touch()

    @property
    def key(self):
        return self._key

    @property
    def sessionId(self):
        return self._sessionId
    
    def __getattr__(self, key):
        return RedisResult(self.key.hget(key, sessionId=self.sessionId))

    def __setattr__(self, key, value):
        self.key.hset(key, value, sessionId=self.sessionId)
        self.touch()

    def __delattr__(self, key):
        self.key.hel(key, sessionId=self.sessionId)

    def __hasattr__(self, key):
        self.key.hexists(key, sessionId=self.sessionId)

    def touch(self):
        self.key.expire(sessionId=self.sessionId)

    def load(self):
        return self.key.hgetall(sessionId=self.sessionId)

    def clear(self):
        self.key.delete(sessionId=self.sessionId)

    def save(self, value):
        self.key.hmset(value, sessionId=self.sessionId)
        self.touch()


def newSessionId():
    return '{}{}'.format(uuid4(), uuid4())
