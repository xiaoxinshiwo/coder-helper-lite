# -- coding:UTF-8 --
# Author:章永新
from functools import wraps

from cacheout import LRUCache

cache = LRUCache()


def cacheable(region, ttl=None):
    """
    对方法的返回值增加缓存
    Args:
        region: 命名空间，一般为类名，或者方法名，需要唯一
        ttl: 缓存失效时间，单位秒

    Returns:
        如果缓存生效则直接返回缓存内容，如果没有缓存则执行目标方法后设置缓存
    """

    def cached(user_function):
        @wraps(user_function)
        def decorated(*args, **kwargs):
            prefix = region + ':' + user_function.__name__
            key = make_key(prefix, args)
            cache_obj = cache.get(key)
            if cache_obj:
                return cache_obj
            else:
                result = user_function(*args, **kwargs)
                if result:
                    cache.set(key, result, ttl)
                return result

        return decorated

    return cached


def make_key(prefix, *args):
    _key = prefix + ':'
    if not args:
        return _key
    else:
        for index, arg in enumerate(list(args)):
            if len(arg) > 0:
                _key = _key + str(arg[len(arg) - 1])
        return _key
