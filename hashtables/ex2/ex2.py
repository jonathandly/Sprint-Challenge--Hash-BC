#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        if ticket.source == "NONE":
            route[0] = ticket.destination
        

    current = route[0]
    index = 1

    while route[-1] is None:
        route[index] = hash_table_retrieve(hashtable, current)
        current = route[index]
        index += 1

    return route[0:-1]
