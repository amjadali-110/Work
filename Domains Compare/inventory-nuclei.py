# Read domains from inventory.txt
with open('inventory.txt', 'r') as file:
    inventory_domains = set(file.read().splitlines())

# Read domains from nuclei.txt
with open('nuclei.txt', 'r') as file:
    nuclei_domains = set(file.read().splitlines())

# Find domains in inventory.txt but not in nuclei.txt
inventory_not_in_nuclei = inventory_domains - nuclei_domains

# Find domains in nuclei.txt but not in inventory.txt
nuclei_not_in_inventory = nuclei_domains - inventory_domains

# Print the results
print("Domains in inventory.txt but not in nuclei.txt:")
for domain in inventory_not_in_nuclei:
    print(domain)

print("\nDomains in nuclei.txt but not in inventory.txt:")
for domain in nuclei_not_in_inventory:
    print(domain)
