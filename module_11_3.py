import sys
import inspect
def introspection_info(obj):
    s = dir(obj)
    y = []
    p = []
    o = type(obj)
    for i in s:
        if i[0] == "_":
            y.append(i)
        else:
            p.append(i)
    u = f'{type(obj)}'
    a = {'type': u[8:len(u)-2], 'attributes': p , 'methods': y, 'module': __name__, 'versia': sys.version, 'versia.info': sys.version_info}
    return a

number_info = introspection_info(42)
print(number_info)