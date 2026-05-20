lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

def sort_variables():
    mutable = []
    immutable = []

    for name, value in globals().items():
        if name.startswith("__"):
            continue

        if isinstance(value, (list, dict, set)):
            mutable.append(name)
        else:
            immutable.append(name)

    sorted_variables = {
        "mutable": mutable,
        "immutable": immutable,
    }

    return sorted_variables
