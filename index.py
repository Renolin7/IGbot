from instabot import Bot
from utils import fetch_reply
import os
bot = Bot()
usname = os.environ['username']
passwrd = os.environ['password']
bot.login(username=usname, password=passwrd)
'''def choice(message):
    get_choice = input(message)
    if get_choice == "y":
        return True
    elif get_choice == "n":
        return False
    else:
        print("Invalid Input")
        return choice(message)'''
def main():
   if bot.api.get_inbox_v2():
     
     data = bot.last_json["inbox"]["threads"]
     for item in data:
        bot.console_print(item["inviter"]["username"], "lightgreen")
        user_id = str(item["inviter"]["pk"])
        last_item = item["last_permanent_item"]
        item_type = last_item["item_type"]
        if item_type == "text":
            print(last_item["text"])
            bot.send_message(fetch_reply(item_type,52521), user_id, thread_id=item["thread_id"])
            continue
        else:
            print(item_type)
if __name__ == '__main__':
   
    try:
        main()
    except KeyboardInterrupt:
        exit()
