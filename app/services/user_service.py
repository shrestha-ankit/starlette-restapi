ALL_USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def get_all_users_handler():
    return ALL_USERS


def get_user_handler(user_id: int):
    for user in ALL_USERS:
        if user.get("id") == user_id:
            return user
    return
        

def create_user_handler(name: str, email: str):
    new_user = {
        "id": len(ALL_USERS) + 1, 
        "name": name, 
        "email": email
        }
    ALL_USERS.append(new_user)
    return new_user


def update_user_handler(user_id: int, data: dict):
    name = data.get("name")
    email = data.get("email")
    for user in ALL_USERS:
        if user.get("id") == user_id:
            if name:
                user["name"] = name
            
            if email:
                user["email"] = email
            
            return user
    return
        
def delete_user_handler(user_id: int):    
    for index, user in enumerate(ALL_USERS):
        if user.get("id") == user_id:
            ALL_USERS.pop(index)
            return user
    
    return
    
    
    
    
    
    
    
   
    
    
    