import ipaddress

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

print("Enter the first list of IP address prefixes:")
list1 = []
while True:
  ip = input()
  if ip == "end":
    break
  list1.append(ip)

print("Enter the second list of IP address prefixes:")
list2 = []
while True:
  ip = input()
  if ip == "end":
    break
  list2.append(ip)

conflicts = find_conflicts(list1, list2)

if conflicts:
  print("Conflicts found:")
  print(conflicts)
elif conflicts == None:
  pass
else:
  print("No conflicts found.")
