
from constants import sp_obj

try:
    print(sp_obj.getData('HELLO_WORLD'))
except ValueError as v:
    print(v)

print(sp_obj.getData('GEN_ZIP'), ' ', end=' ')
print(type(sp_obj.getData('GEN_ZIP')))
print(sp_obj.getData('READ_ZIP'), ' ', end=' ')
print(type(sp_obj.getData('READ_ZIP')))