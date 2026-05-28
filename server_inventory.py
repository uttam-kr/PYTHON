import csv
servers = []
with open('servers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        servers.append(row)

# 2. Display all servers
print("All Servers:")
for server in servers:
    print(f"{server['hostname']} ({server['ip']}) - {server['status']} - {server['role']}")

# 3. Filter by status
status_filter = input("\nEnter status to filter by (e.g., active/inactive): ").strip().lower()
filtered_servers = [s for s in servers if s['status'].lower() == status_filter]

print(f"\nServers with status '{status_filter}':")
for server in filtered_servers:
    print(f"{server['hostname']} ({server['ip']}) - {server['role']}")

# 4. Export filtered results
output_file = f"{status_filter}_servers.csv"
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['hostname', 'ip', 'status', 'role']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for server in filtered_servers:
        writer.writerow(server)

print(f"\nFiltered servers saved to {output_file}")