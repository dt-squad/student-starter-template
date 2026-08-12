# List: dogs = [<data>]
# Dictionary: {key:value, key:value}
# Tuple: dogs = (<immutable data>)
# Loop: for dog in dogs: <code is repeated on each dog instance until there are no instances left>



dogs = [
    {"breed" : "Portugeese Water Dog", "age": 12},
    {"breed" : "Staffy", "age": 2},
    {"breed" : "Cockapoo", "age": 5},
    {"breed" : "Poodle", "age": 8},
    {"breed" : "Great Dane", "age": 14},
]

def return_age(dogs):
    total_age = 0
    for dog in dogs:
        age = dog["age"]
        dog["Colour"] = "Brown"
        total_age += age

    return total_age

return_age(dogs)

# Same outcome with a tuple (which makes the data immutable)
total_age = 0
dogs = (
    {"breed": "Portugeese Water Dog", "age": 12},
    {"breed": "Staffy", "age": 2},
    {"breed": "Cockapoo", "age": 5},
    {"breed": "Poodle", "age": 8},
    {"breed": "Great Dane", "age": 14},
)

for dog in dogs:
    age = dog["age"]
    total_age += age

print(total_age)

# Or a tuple of tuples
total_age = 0
dogs = (
    ("Portugeese Water Dog", 12),
    ("Staffy", 2),
    ("Cockapoo", 5),
    ("Poodle", 8),
    ("Great Dane", 14),
)

total_age = 0
for dog in dogs:
    age = dog[1]
    total_age += age

print(total_age)