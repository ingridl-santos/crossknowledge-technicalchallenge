import requests
import redis
import json
from config.config_redis import config_redis

from decorator import decorator

redis = redis.StrictRedis(**config_redis)


@decorator
def cache(function, http='GET', expire=10, *args, **kwargs):
    """ Data will be stored in redis """
    url = args[0]
    key = f'{http}_{url}'
    if not redis.exists(key):
        response = function(*args, **kwargs)
        data = json.dumps(response)
        redis.setex(key, expire, data)
        return response
    else:
        return json.loads(redis.get(key))


@cache
def get(url, parameters=None):
    """ Fetches an URL and returns the response """
    return requests.get(url, params=parameters).json()


@cache(http='POST')
def post(url, parameters=None, data=None):
    """ Post data to an URL and returns the response """
    return requests.post(url, params=parameters, data=data).json()


@cache(http='PUT')
def put(url, parameters=None, data=None):
    """ Put data to an resource and returns the response """
    return requests.put(url, params=parameters, data=data).json()


@cache(http='PACTH')
def patch(url, parameters=None, data=None):
    """ Patches an resource and returns the response """
    return requests.patch(url, params=parameters, data=data).json()


@cache(http='DELETE')
def delete(url, parameters=None, data=None):
    """ Requests the deletion of an resource and returns the response """
    return requests.delete(url, params=parameters, data=data).json()
