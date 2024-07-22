import json
import os
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen
from setting import auth0_domain, api_audience

AUTH0_DOMAIN = auth0_domain
ALGORITHMS = ['RS256']
API_AUDIENCE = api_audience


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'status': False,
            'code': 'not_authorization'
        }, 401)
    partsToken = auth.split(' ')
    if len(partsToken) == 1:
        raise AuthError({
            'status': False,
            'code': 'token_not_found',
        }, 401)
    elif partsToken[0] != 'Bearer':
        raise AuthError({
            'status': False,
            'code': 'invalid_token',
        }, 401)

    return partsToken[1]


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise ({
            'status': False,
            'code': 'invalid_permissions'
        }, 400)
    if permission not in payload['permissions']:
        raise AuthError({
            'status': False,
            'code': 'unauthorized'
        }, 403)
    return True


def verify_decode_jwt(token):
    jsonUrl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwksJson = json.loads(jsonUrl.read())
    unverifiedHeader = jwt.get_unverified_header(token)
    rsaKey = {}
    if 'kid' not in unverifiedHeader:
        raise AuthError({
            'status': False,
            'code': 'invalid_token'
        }, 401)
    for key in jwksJson['keys']:
        if key['kid'] == unverifiedHeader['kid']:
            rsaKey = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e'],
            }
    if rsaKey:
        try:
            return jwt.decode(token, rsaKey, algorithms=ALGORITHMS,
                              audience=API_AUDIENCE, issuer=f'https://{AUTH0_DOMAIN}/')
        except jwt.ExpiredSignatureError as e:
            print(e)
            raise AuthError({
                'status': False,
                'code': 'token_expired'
            }, 401)
        except jwt.JWTClaimError as e:
            print(e)
            raise AuthError({
                'status': False,
                'code': 'invalid_claim'
            }, 401)
        except Exception as e:
            print(e)
            raise AuthError({
                'status': False,
                'code': 'invalid_token'
            }, 401)
    raise AuthError({
        'status': False,
        'code': 'invalid_token'
    })


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator
