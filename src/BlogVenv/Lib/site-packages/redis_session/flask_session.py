#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from redis_session.session import Session, newSessionId
from flask import request, after_this_request
from functools import wraps
from werkzeug.contrib.securecookie import SecureCookie
from itsdangerous import URLSafeTimedSerializer
from flask.json.tag import TaggedJSONSerializer



sessionOptions = {}

def setupSession(options):
    global sessionOptions
    sessionOptions['session_cookie_id'] = options.get('SESSION_COOKIE_ID') or 'session-id'
    sessionOptions['session_redis'] = options.get('SESSION_REDIS')
    sessionOptions['session_redis_prefix'] = options.get('SESSION_REDIS_PREFIX')
    sessionOptions['session_expire'] = options.get('SESSION_EXPIRE')
    sessionOptions['session_cookie_http_only'] = options.get('SESSION_COOKIE_HTTP_ONLY') is not False
    sessionOptions['session_cookie_secure'] = options.get('SESSION_COOKIE_SECURE') is not False
    sessionOptions['session_cookie_domain'] = options.get('SESSION_COOKIE_DOMAIN')
    sessionOptions['session_cookie_path'] = options.get('SESSION_COOKIE_PATH') or '/'
    sessionOptions['session_secret_key'] = options.get('SECRET_KEY')

    if sessionOptions['session_secret_key'] is None:
        raise Exception('Please specify secret_key for flask app for security!')

def setup_session(app):
    global sessionOptions
    setupSession(app.config)
    app.config['SESSION_COOKIE_SECURE'] = sessionOptions['session_cookie_secure']
    digest_method = hashlib.sha1
    key_derivation = "hmac"

    # Seems flask cookies are not natively handled well, we borrowed some codes from: http://pythonexample.com/code/flask-cookie-httponly/
    serializer = URLSafeTimedSerializer(
        sessionOptions['session_secret_key'],
        salt=sessionOptions['session_secret_key'],
        serializer=TaggedJSONSerializer(),
        signer_kwargs=dict(key_derivation=key_derivation, digest_method=digest_method)
    )

    def encodeCookie(_sessionId):
        scookie = SecureCookie({sessionOptions['session_cookie_id']: _sessionId}, sessionOptions['session_secret_key'])
        return serializer.dumps(scookie)

    def decodeCookie(_sessionId):
        try:
            return serializer.loads(_sessionId).get(sessionOptions['session_cookie_id'])
        except:
            pass

    @app.before_request
    def _attach():
        request.session = None
        sessionId = decodeCookie(request.cookies.get(sessionOptions['session_cookie_id']))
        if sessionId is None or sessionId == '':
            sessionId = newSessionId()

            @after_this_request
            def post_set_cookie(response):
                # TODO: Add http only switch here after some testing
                response.set_cookie(sessionOptions['session_cookie_id'], encodeCookie(sessionId), secure=sessionOptions['session_cookie_secure'], domain=sessionOptions['session_cookie_domain'], path=sessionOptions['session_cookie_path'])
                return response

        request.session = Session(sessionId, **sessionOptions)


