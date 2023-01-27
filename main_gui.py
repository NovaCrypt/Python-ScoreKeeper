import customtkinter
import os
import json
import classes

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")
root.title("Game Login")

def open_game_window(player: object):
  game_window = customtkinter.CTkToplevel()
  game_window.geometry("500x300")
  game_window.title("Game")

  def negative_score_change():
    try:
      player.score -= (int(score_change.get()))
    except ValueError:
      print("Invalid value entry, score change function requires a number.")

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

    score_label.configure(text=f"{player.score}")

  def positive_score_change():
    try:
      player.score += (int(score_change.get()))
    except ValueError:
      print("Invalid value entry, score change function requires a number.")

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

    score_label.configure(text=f"{player.score}")

  game_window.rowconfigure(0,weight=1)
  game_window.columnconfigure(0,weight=1)

  display_frame = customtkinter.CTkFrame(master=game_window)
  display_frame.grid(row=0,column=0,padx=20,pady=(30,0),sticky="nsew")

  username_label = customtkinter.CTkLabel(master=display_frame,text=f"{player.name}'s Score",font=("Acumin Pro Extra Light",28))
  username_label.pack(pady=12,padx=10)

  score_label = customtkinter.CTkLabel(master=display_frame,text=f"{player.score}",font=("Acumin Pro Extra Light",28))
  score_label.pack(pady=12,padx=10)

  control_frame = customtkinter.CTkFrame(master=game_window)
  control_frame.grid_columnconfigure(1,weight=1)
  control_frame.grid(row=1,column=0,pady=30,padx=20,sticky="ew")

  score_change = customtkinter.CTkEntry(master=control_frame,placeholder_text="Value")
  score_change.grid(row=0,column=1,padx=10,pady=12,sticky="nsew")

  minus_button = customtkinter.CTkButton(master=control_frame,text="-",command=negative_score_change,width=40)
  minus_button.grid(row=0,column=0,padx=(10,0),pady=12)

  plus_button = customtkinter.CTkButton(master=control_frame,text="+",command=positive_score_change,width=40)
  plus_button.grid(row=0,column=2,padx=(0,10),pady=12)


def login():
  username = username_entry.get()

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

  open_game_window(player)

login_frame = customtkinter.CTkFrame(master=root)
login_frame.pack(pady=20,padx=60,fill="both",expand=True)

login_label = customtkinter.CTkLabel(master=login_frame,text="Login",font=("Acumin Pro Extra Light",28))
login_label.pack(pady=12,padx=10)

username_entry = customtkinter.CTkEntry(master=login_frame,placeholder_text="Username")
username_entry.pack(pady=12,padx=10)

login_button = customtkinter.CTkButton(master=login_frame,text="Login",command=login)
login_button.pack(pady=12,padx=10)

root.mainloop()