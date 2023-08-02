import sys
import Chatbot1
import Chatbot2


# line = None
# history = []
# while True:
#     if not line:
#         line = input("Line:")
#     if line in ['quit', 'q', 'exit']:
#         sys.exit()
#     print(Bot1Draft.reply(line, history))
#     print(history)
#     line = None


def script(name, line):
    with open("Script.txt", "a") as f:
        f.write(f"{name}: {line}\n")
    print(f"{name}: {line}")


def main():
    line = "say something"
    history = []
    with open("Script.txt", "w") as f:
        f.write("Script\n\n")
    for script_length in range(10):
        line = Chatbot1.reply(line,history)
        script("Bot1", line)
        line = Chatbot2.reply(line,history)
        script("Bot2", line)


if __name__ == "__main__":
    main()