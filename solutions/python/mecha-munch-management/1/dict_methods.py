"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    pass


def read_notes(notes):
    new_dict = dict.fromkeys(notes, 1)
    return new_dict
        
    new_dict = dict(notes)
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    pass


def update_recipes(ideas, recipe_updates):
    rec_update = dict(recipe_updates)
    return ideas | rec_update
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    pass


def sort_entries(cart):
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    pass


def send_to_store(cart, aisle_mapping):
    result = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            result[item] = [quantity] + aisle_mapping[item]
    sorte = sorted(result.items(), reverse = True)
    return dict(sorte)
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    pass


def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        if item in store_inventory:
            store_inventory[item][0] -= fulfillment_cart[item][0]
            if store_inventory[item][0] == 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    pass
