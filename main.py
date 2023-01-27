import classes
import os
import json

'''
This is a game where the user must guess a number from 1 - 100. The closer the user is to the number, the more points the user earns.

Point values are stored alongside a username in an SQL database of Dict data type variables. This is called after the user logs into the game at the start of the program.
'''

def select_user(username):
  if not os.path.exists("users.json"):
    file_content = {
      username: {
        "username": username,
        "score": 0
      }
    }

    json_file = open("users.json", "w")
    json_file.write(json.dumps(file_content, indent=2))
    json_file.close()

  users_file = open("users.json")
  users_dict = json.loads(users_file.read())
  users_file.close()

  if not username in users_dict.keys():
    users_dict[username] = {
      "username": username,
      "score": 0
    }

    users_file = open("users.json", "w")
    users_file.write(json.dumps(users_dict, indent=2))
    users_file.close()

  user_data = users_dict.get(username)
  player = classes.User(user_data["username"], user_data["score"])

  return player

def score_changer(player: object):
  users_file = open("users.json")
  users_dict = json.loads(users_file.read())
  users_file.close()

  users_dict[player.name] = {
    "username": player.name,
    "score": player.score
  }

  users_file = open("users.json", "w")
  users_file.write(json.dumps(users_dict, indent=2))
  users_file.close()

def main(username):
  player = select_user(username)

  while True:
    print("\n--------------------\n")
    print(player)

    score_change = input("\nScore change: ")
    try:
      player.score += int(score_change)
    except ValueError:
      print("\n\nEnter a valid whole number.")

    score_changer(player)

main(input("Username: "))