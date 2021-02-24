command = input()
users = {}
languages = {}
while command != "exam finished":
    command = command.split("-")
    if "banned" not in command:
        username, language, points = command[0], command[1], int(command[2])
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
        if username in users:
            if users[username] < points:
                users[username] = points
        elif username not in users:
            users[username] = points
    else:
        username = command[0]
        users.pop(username)
    command = input()
users_ord = dict(sorted(users.items(), key = lambda x: (-x[1], x[0])))
languages_ord = dict(sorted(languages.items(), key = lambda x: (-x[1], x[0])))
print("Results:")
for key, value in users_ord.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in languages_ord.items():
    print(f"{key} - {value}")


