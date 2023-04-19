
from constants import np_obj

try:
    print(np_obj.getData('NODEFECT_FLDR'))
except ValueError as v:
    print(v)

print(np_obj.getData('DND_RATIO'), ' ', end=' ')
print(type(np_obj.getData('DND_RATIO')))
print(np_obj.getData('TVT_RATIO'), ' ', end=' ')
print(type(np_obj.getData('TVT_RATIO')))