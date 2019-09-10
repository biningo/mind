#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from redis_session.session import Session, newSessionId
from tornado.options import options, define


define('session-redis', default='redis://localhost:6379', help='session store redis url', type=str)
define('session-redis-prefix', help='redis key prefix', type=str)
define('session-expire', help='session ttl(seconds)', type=int)
define('session-cookie-id', help='cookie key, default: session-id', type=str)
define('session-cookie-secure', default=True, help='if use secure session cookie', type=bool)
define('session-cookie-domain', default='', help='session cookie domain', type=str)
define('session-cookie-path', default='/', help='session cookie path', type=str)
define('session-cookie-http-only', default=True, help='if set session cookie as http only', type=bool)


class SessionHandler(RequestHandler):
    """Build basic request handlers with session handling"""

    @property
    def sessionId(self):
        if not hasattr(self, '_sessionId'):
            cookieKey = options.session_cookie_id or 'session-id'
            httpOnly = options.session_cookie_http_only
            sessionId = self.get_secure_cookie(cookieKey) if options.session_cookie_secure else self.get_cookie(cookieKey)
            if isinstance(sessionId, bytes):
                sessionId = sessionId.decode('utf8')
            if sessionId is None or sessionId == '':
                sessionId = newSessionId()
                domain = options.session_cookie_domain if len(options.session_cookie_domain) > 0 else None
                if options.session_cookie_secure:
                    self.set_secure_cookie(cookieKey, sessionId, httponly=httpOnly, domain=domain, path=options.session_cookie_path)
                else:
                    self.set_cookie(cookieKey, sessionId, httponly=httpOnly, domain=domain, path=options.session_cookie_path)
            self._sessionId = sessionId
        return self._sessionId

    @property
    def session(self):
        if not hasattr(self, '_session'):
            self._session = Session(self.sessionId, session_redis=options.session_redis,
                session_redis_prefix=options.session_redis_prefix,
                session_expire=options.session_expire)

        return self._session

    @session.setter
    def session(self, value):
        self.session.save(value)

    @session.deleter
    def session(self):
        self.session.clear()

