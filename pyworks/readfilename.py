import os

# for root, dirs, files in os.walk("."):
#     for filename in files:
#         print(filename)

path = str(os.getcwd()) + "\json"
print(path)

with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            strval = entry.name
            if strval.find("_ipv6networks.json") != -1:
                ipv6jsonfile = 'json/' + strval
                print("1 " + ipv6jsonfile )
            elif strval.find("_networks.json") != -1:
                ipv4jsonfile = 'json/' + strval
                print("2 " + ipv4jsonfile)

print("3 " + ipv4jsonfile)
print("4 " + ipv6jsonfile)