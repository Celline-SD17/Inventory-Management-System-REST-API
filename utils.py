def next_id(inventory):
    if inventory:
        return max(item["id"] for item in inventory) + 1
    else:
        return 1