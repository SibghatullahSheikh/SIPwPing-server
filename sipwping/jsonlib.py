# coding=utf8

# Copyright (C) 2011 Saúl Ibarra Corretgé <saghul@gmail.com>
#

try:
    import cjson as jsonlib
    jsonlib.dumps = jsonlib.encode
    jsonlib.loads = jsonlib.decode
except ImportError:
    try:
        from django.utils import simplejson as jsonlib
    except ImportError:
        try:
            import simplejson as jsonlib
        except ImportError:
            import json as jsonlib

