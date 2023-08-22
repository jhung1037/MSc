import tiktoken

tokenizer = tiktoken.get_encoding('cl100k_base')

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(text)
    return len(tokens)

def main():
    with open("Settings/John.txt", "r") as f:
        a = f.read()

    print(tiktoken_len(a))

if __name__ == "__main__":
    main()