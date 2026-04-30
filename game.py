import random


class SlotMachine:
    def __init__(self, rows, cols, symbol_count, symbol_value):
        self.rows = rows
        self.cols = cols
        self.symbol_count = symbol_count
        self.symbol_value = symbol_value

    def spin(self):
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(self.cols):
            column = random.sample(all_symbols, self.rows)
            columns.append(column)

        return columns

    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []

        for line in range(lines):
            symbol = columns[0][line]

            for column in columns:
                if column[line] != symbol:
                    break
            else:
                winnings += self.symbol_value[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i != len(columns) - 1 else "")
        print()