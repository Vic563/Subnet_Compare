import ipaddress

def find_conflicts(list1, list2):
  conflicts = []
  for prefix1 in list1:
    for prefix2 in list2:
      if prefix1.split('.')[0] == '0' or prefix2.split('.')[0] == '0':
        print("An invalid IP address was entered.")
        return []
      try:
        if ipaddress.IPv4Network(prefix1).overlaps(ipaddress.IPv4Network(prefix2)):
          conflicts.append((prefix1, prefix2))
      except ValueError:
        print("An invalid IP address was entered.")
        return []
      except ipaddress.AddressValueError:
        print("Invalid IP address entered.")
        return []
  return conflicts

print("Enter the first list of IP addresses, one per line. Enter 'end' when finished:")
list1 = []
while True:
  ip_address = input()
  if ip_address == 'end':
    break
  list1.append(ip_address)

print("Enter the second list of IP addresses, one per line. Enter 'end' when finished:")
list2 = []
while True:
  ip_address = input()
  if ip_address == 'end':
    break
  list2.append(ip_address)

if len(list1) == 0 or len(list2) == 0:
  print("No valid IP addresses were entered.")
else:
  invalid_ip_entered = False
  for prefix in list1 + list2:
    if prefix.split('.')[0] == '0':
      print("An invalid IP address was entered.")
      invalid_ip_entered = True
    try:
      ipaddress.IPv4Network(prefix)
    except ValueError:
      print("An invalid IP address was entered.")
      invalid_ip_entered = True
      break
    except ipaddress.AddressValueError:
      print("Invalid IP address entered.")
      invalid_ip_entered = True
      break

  if not invalid_ip_entered:
    conflicts = find_conflicts(list1, list2)
    if conflicts:
      print("Conflicts found:")
      for conflict in conflicts:
        print(f"{conflict[0]} conflicts with {conflict[1]}")
    else:
      print("No conflicts found.")
