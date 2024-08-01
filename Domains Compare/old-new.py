# Read domains from old.txt
with open('old.txt', 'r') as file:
    old_domains = set(file.read().splitlines())

# Read domains from new.txt
with open('new.txt', 'r') as file:
    new_domains = set(file.read().splitlines())

# Find domains in old.txt but not in new.txt
old_not_in_new = old_domains - new_domains

# Find domains in new.txt but not in old.txt
new_not_in_old = new_domains - old_domains

# Print the results
print("Domains in old.txt but not in new.txt:")
for domain in old_not_in_new:
    print(domain)

print("\nDomains in new.txt but not in old.txt:")
for domain in new_not_in_old:
    print(domain)
