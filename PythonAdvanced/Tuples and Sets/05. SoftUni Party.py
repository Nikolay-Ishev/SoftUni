n = int(input())
guest_list = set()
for reservation in range(n):
    guest_list.add(input())
command = input()
while command != "END":
    guest_list.remove(command)
    command = input()
print(len(guest_list))
for guest in sorted(guest_list):
    print(guest)

