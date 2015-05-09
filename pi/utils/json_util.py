'''
Created on May 9, 2015

@author: Aman
'''
import json

def toJson(o, cls=None):
    if isinstance(o, (list, tuple)):
        d = [to_dict(r, cls) for r in o]
    else:
        d = to_dict(o, cls)
    return json.dumps(d, check_circular=True, indent=True, sort_keys=True)

def to_dict(inst, cls=None):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    if not cls:
        cls = inst.__class__
        
    convert['DATETIME'] = convertDatetime

    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        # print c.name, '|'+str(c.type)+'|', str(c.type) in convert
        typ = str(c.type)
        if typ in convert.keys() and v is not None:
            try:
                d[c.name] = convert[typ](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return d

def convertDatetime(v):
    return v.isoformat()
