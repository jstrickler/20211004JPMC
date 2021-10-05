actor = "Chris Hemsworth"

print(len(actor))  #  why not actor.len() or actor.size() or actor.length()?

print(actor.upper())

a1 = actor.upper()
print(a1, actor)

print(actor.upper)
print(actor.upper())

print(actor.count('h'))
print(actor.lower().count('h'))  # method chaining

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print()

print('ems' in actor)
print('mess' in actor)
print()

print(actor.replace('Chris', 'Liam'), '\n')
print(actor.replace('worth', ''), '\n')

print(actor.index('worth'))
print(actor.find('worth'))
print(actor.find('wombat'))
print()

s = "fee:fi:fo:fum"
print(s.split(':'))
s = "fee::fi::fo::fum"
print(s.split('::'))
s = "fee      fi\tfo\n         fum"   # \r \n \t \f ' '
print(s.split())
print()

s = "          All my exes live in Texas          "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = 'xyxxyyxxxyyyAll my exes live in Texasyyyxxxyyxxyxyyyyyyyyyyy'
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

#   remove leading 'abc'
#   'abcababcababcsomething else'
#  use re
import re   # load the re module
s = 'abcabcababcababcsomething somethingabcabc'
s2 = re.sub('^(?:abc)+(.*?)(?:abc)+$', r'\1', s)
print("s2:", s2)

# print(s.replace('abc', ''))



















