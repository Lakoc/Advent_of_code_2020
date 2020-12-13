import sys


def find_first():
    mod = sys.maxsize
    bus_id = 0
    for i, bus in enumerate(buses):
        bus = int(bus)
        department = bus - (minutes % bus)
        if department < mod:
            mod = department
            bus_id = bus
    print(bus_id * mod)


with open('input') as file:
    lines = file.readlines()
    minutes = int(lines[0].rstrip())
    buses = lines[1].rstrip().split(',')
    while 'x' in buses:
        buses.remove('x')
    find_first()
