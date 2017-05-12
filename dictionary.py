import random
import sys
import os

super_villains = {'fiddler' : 'isaac bowin',
'captain ice' : 'cool man',
'captain america' : 'nice guy turn hulk'}

print(super_villains['fiddler'])

del super_villains['fiddler']

print(super_villains)

super_villains['new char'] = 'manicPraise'

print(super_villains)

super_villains['captain america'] = 'shwan blon'

print(super_villains)

print(super_villains.get("new char"))

print(super_villains.keys())
print(super_villains.values())
