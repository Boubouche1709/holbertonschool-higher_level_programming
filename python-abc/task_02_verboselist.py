#!/usr/bin/python3


# Define a class that extends the built-in list
class VerboseList(list):
    # Override the append method
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    # Override the extend method
    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    # Override the remove method
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    # Override the pop method
    def pop(self, index=-1):
        item = self[index]  # Get the item before popping
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
