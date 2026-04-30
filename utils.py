import os


def save_balance(balance):
    os.makedirs("data", exist_ok=True)
    with open("data/balance.txt", "w") as f:
        f.write(str(balance))


def load_balance():
    try:
        with open("data/balance.txt", "r") as f:
            return int(f.read())
    except:
        return 0


def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print("Too low!")
                continue
            if max_val is not None and value > max_val:
                print("Too high!")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")