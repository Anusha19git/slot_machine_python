from game import SlotMachine, print_slots
from player import Player
from config import *
from utils import save_balance, load_balance, get_int_input


def main():
    print("🎰 Welcome to Slot Machine 🎰")

    balance = load_balance()
    player = Player(balance)

    if player.balance == 0:
        deposit = get_int_input("Enter deposit amount: ", 1)
        player.deposit(deposit)

    machine = SlotMachine(ROWS, COLS, SYMBOL_COUNT, SYMBOL_VALUE)

    stats = {"spins": 0, "wins": 0}

    while True:
        print(f"\n💰 Current balance: {player.balance}")
        choice = input("Press Enter to spin (q to quit): ").lower()

        if choice == "q":
            break

        lines = get_int_input("Enter number of lines (1-3): ", 1, MAX_LINES)
        bet = get_int_input(f"Enter bet per line ({MIN_BET}-{MAX_BET}): ", MIN_BET, MAX_BET)

        total_bet = bet * lines

        if not player.can_bet(total_bet):
            print("❌ Not enough balance")
            continue

        print("\n🎰 Spinning...\n")
        slots = machine.spin()
        print_slots(slots)

        winnings, winning_lines = machine.check_winnings(slots, lines, bet)

        net = winnings - total_bet
        player.update_balance(net)

        stats["spins"] += 1
        if winnings > 0:
            stats["wins"] += 1

        print(f"\n💸 You won: {winnings}")
        print(f"🏆 Winning lines: {winning_lines}")

    save_balance(player.balance)

    print("\n📊 Game Stats:")
    print(f"Total Spins: {stats['spins']}")
    print(f"Total Wins: {stats['wins']}")
    print(f"Final Balance: {player.balance}")


if __name__ == "__main__":
    main()