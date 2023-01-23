import ipaddress
import re

def find_conflicts(list1, list2):
  conflicts = []
  for prefix1 in list1:
    for prefix2 in list2:
      if prefix1.split('.')[0] == '0' or prefix2.split('.')[0] == '0':
        print("An invalid IP address was entered.")
        return
      try:
        if ipaddress.IPv4Network(prefix1).overlaps(ipaddress.IPv4Network(prefix2)):
          conflicts.append(prefix1)
          conflicts.append(prefix2)
      except ValueError:
        print("An invalid IP address was entered.")
        return
  return conflicts

print("Enter the first list of IP addresses by pasting multiple lines of text containing the addresses, in the format 'w.x.y.z/m'. Enter 'end' on a line by itself when finished:")
list1 = []
while True:
  line = input()
  if line == 'end':
    break
  match = re.search(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2})', line)
  if match:
    list1.append(match.group(1))

print("Enter the second list of IP addresses by pasting multiple lines of text containing the addresses, in the format 'w.x.y.z/m'. Enter 'end' on a line by itself when finished:")
list2 = []
while True:
  line = input()
  if line == 'end':
    break
  match = re.search(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2})', line)
  if match:
    list2.append(match.group(1))

conflicts = find_conflicts(list1, list2)

if conflicts:
  print("Conflicts found:")
  print(conflicts)
else:
  print("No conflicts found.")
