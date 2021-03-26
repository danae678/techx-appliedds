# You are given a dictionary containing the names and ages of a group of people, a list of names of people to remove from that dictionary, and a dictionary of people and ages to add to the first dictionary. Your task is to:

#     1. Calculate the average age of the group at the start.
#     2. Remove the entries from the group dictionary that are in the to_remove list.
#     3. Insert the entries from the to_add dictionary into the group dictionary.
#     4. Calculate the average age of the group after modifying group.
#     5. Return the difference in average age from start to end rounded to two decimal places.

# Don't forget to modify the original group!
group = {
    "Jackie": 24,
    "Jermaine": 18,
    "Marlon": 17,
    "Michael": 14,
    "Tito": 21,
}

to_remove = ["Jermaine"]

to_add = {
    "Randy": 22
}

def find_age_difference(group, to_remove, to_add):
    """Calculates the average age of a group after making changes.

    Args:
        group: Dictionary containing names and ages.
        to_remove: List containing people to remove.
        to_add: Dictionary containing names and ages to add.

    Returns:
        Floating point difference in average age of the group after changes.
    """
    try:
    # Calculate the average age of the group
        average = sum(group.values())/len(group.values())
    except:
        average = 0
  
  # Insert the entries from the to_add dictionary into the group dictionary.
    for key, value in to_add.items():
        group[key] = value
    
  # Remove the entries from the group dictionary that are in the to_remove list.
    for r in to_remove:
        try:
            del group[r]
        except:
            continue
    
    try:
    # Calculate the average age of the group after modifying group.
        new_average = sum(group.values())/len(group.values())
    except:
        new_average = 0
  
    # Return the difference in average age from start to end rounded to two decimal places.
    return round(new_average - average, 2)

print(find_age_difference(group, to_remove, to_add)) #0.8