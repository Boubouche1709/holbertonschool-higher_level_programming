#!/usr/bin/python3


# Define the CountedIterator class
class CountedIterator:
    def __init__(self, iterable):
        # Initialize the internal iterator from the iterable
        self.iterator = iter(iterable)
        # Initialize the counter to track how many items have been fetched
        self.count = 0

    def __iter__(self):
        # Return self to make this object an iterator
        return self

    def __next__(self):
        # Fetch the next item from the internal iterator
        item = next(self.iterator)  # May raise StopIteration
        # Increment the counter
        self.count += 1
        return item

    def get_count(self):
        # Return the number of items that have been iterated
        return self.count
