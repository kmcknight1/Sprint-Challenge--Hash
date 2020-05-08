#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {}
    route = [None] * length

    #add tickets to ht
    for t in tickets:
        ht[t.source] = t.destination

    #start at current city where source is None
    current_city = ht["NONE"]
    #loop through, starting at current_city
    #add the destinations to the route array
    #next city is the ht[current_city]
    i = 0
    while current_city != "NONE":
        route[i] = current_city
        current_city = ht[current_city]
        i += 1
    #make the last one None
    route[i] = "NONE"
    
    return route