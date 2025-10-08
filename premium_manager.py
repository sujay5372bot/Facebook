import json
import os

PREMIUM_FILE = "premium_keys.json"
PREMIUM_USERS_FILE = "premium_users.json"

# Load premium keys
def load_keys():
    with open(PREMIUM_FILE, "r") as f:
        return json.load(f)

# Save updated keys
def save_keys(data):
    with open(PREMIUM_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Check & activate premium key
def activate_key(user_id, key):
    data = load_keys()

    if key in data["valid_keys"]:
        data["valid_keys"].remove(key)
        data["used_keys"].append(key)
        save_keys(data)
        add_premium_user(user_id)
        return True
    else:
        return False

# Save premium user IDs
def add_premium_user(user_id):
    if os.path.exists(PREMIUM_USERS_FILE):
        with open(PREMIUM_USERS_FILE, "r") as f:
            users = json.load(f)
    else:
        users = []

    if user_id not in users:
        users.append(user_id)

    with open(PREMIUM_USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Check if user is premium
def is_premium(user_id):
    if os.path.exists(PREMIUM_USERS_FILE):
        with open(PREMIUM_USERS_FILE, "r") as f:
            users = json.load(f)
            return user_id in users
    return False
