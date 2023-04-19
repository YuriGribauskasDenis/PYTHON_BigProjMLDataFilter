
from constants import ap_obj

try:
    print(ap_obj.getData('DND_RATIO'))
except ValueError as v:
    print(v)

print(ap_obj.getData('NODEFECT_FLDR'), ' ', end=' ')
print(type(ap_obj.getData('NODEFECT_FLDR')))