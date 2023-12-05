"""Print out all the melons in our inventory."""


from melons import all_melons

def print_melons(all_melons):
    """Print each melon with corresponding attribute information."""

#  all_melons.items() returns a view of the dictionary's items as a list of tuples. 
# Each tuple consists of a key-value pair, where melon_name is assigned to the KEY, 
# and attributes is assigned the value. In this case, the values contain the attributes for that melon.
# After 'for'...the variable that is used will become the KEY of that dictionary, in this case it's melon_name
    for melon_name, attributes in all_melons.items(): 
        print(melon_name.upper())

# This for loop iterates through the items of the attributes dictionary, 
# which contains the attributes for a specific melon.
# attributes.items(): returns a view of the dictionary's items as a list of tuples. 
# Each tuple consists of a key-value pair, where the key is an attribute name, 
# and the value is the corresponding attribute value.
# In the key:value pair format, attribute would be key. Value would be value
# The print statement prints each attribute and its corresponding value in a formatted string.
# This then removes the curly brackets.
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')


print_melons(all_melons)

