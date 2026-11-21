def get_user_dashboard(username):
    dashboard = {
        "username": username,
        "status": "Active",
        "role": "DevOps Engineer"
    }
    return dashboard


if __name__ == "__main__":
    user_dashboard = get_user_dashboard("Rekha")
    print(user_dashboard)
    print("-------------------")
