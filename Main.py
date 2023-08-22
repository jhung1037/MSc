import sys
from Chatbot import ChatBot
from datetime import datetime

# log into script
def script(name, line):
    with open("Script.txt", "a") as f:
        f.write(f"{name}: {line}\n")

# extract line only for the normal format of a script
def extract(text):
    first_quote = text.index('"')
    last_quote = text.rindex('"')
    extracted_text = text[first_quote + 1 : last_quote]
    return extracted_text

# reassure objective be passed into the prompt
John_obj = "Let's play an acting game. In this game, you are John. Your ultimate goal is to kiss Alma." # without showing your affection."
Alma_obj = "Let's play an acting game. In this game, you are Alma. Your ultimate goal is to show John how you care about him." # without revealing too much."

def main():
    # initialisation
    John = ChatBot("John")
    Alma = ChatBot("Alma")
    line = ""
    chat_history = "Previous Conversation:"

    # create script file
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("Script.txt", "w") as f:
        f.write(f"{time}\n\n")

    # conversation loop
    for script_length in range(5): # set script_length here
        line = John.reply(John_obj, "Alma", chat_history, line)
        script("John", extract(line))
        chat_history = chat_history + "\nJohn: " + line
        line = Alma.reply(Alma_obj, "John", chat_history, line)
        script("Alma", extract(line))
        chat_history = chat_history + "\nAlma: " + line

if __name__ == "__main__":
    main()