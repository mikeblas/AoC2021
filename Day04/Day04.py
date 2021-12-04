
with open('input.txt') as my_file:
    input_lines = my_file.readlines()
input_lines = [s.strip() for s in input_lines]
line_count = len(input_lines)

number_list = input_lines[0].split(",")
number_list = [int(x) for x in number_list]

input_lines = input_lines[2:]

print(number_list)
print(input_lines)

class BingoCard:

    def __init__(self, text_lines):
        self.rows = []
        self.marked = []
        self.previously_won = False
        for line in text_lines:
            this_line = line.split()
            this_line = [int(x) for x in this_line]
            self.rows.append(this_line)
            self.marked.append([0 for x in range(5)])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        build = "\n"
        for idy in range(5):
            for idx in range(5):
                build += f"{self.rows[idy][idx]:2}"
                if self.marked[idy][idx] == 1:
                    build += "* "
                else:
                    build += "  "
            build += '\n'

        return build

    def mark(self, number):
        for idy in range(5):
            for idx in range(5):
                if self.rows[idy][idx] == number:
                    self.marked[idy][idx] = 1

    def is_winner(self):
        if self.previously_won:
            return False
        for idy in range(5):
            if 0 not in self.marked[idy]:
                self.previously_won = True
                return True

        for idx in range(5):
            all_marked = True
            for idy in range(5):
                if self.marked[idy][idx] == 0:
                    all_marked = False
                    break
            if all_marked:
                self.previously_won = True
                return True

        return False

    def get_score(self):
        score = 0
        for idy in range(5):
            for idx in range(5):
                if self.marked[idy][idx] == 0:
                    score += self.rows[idy][idx]

        return score


cards = []
i = 0
while i < len(input_lines):
    cards.append(BingoCard(input_lines[i:i+5]))
    i += 6

has_winner = False
last_winning_score = -1
for number in number_list:
    print(f"drew {number}")
    for card in cards:
        card.mark(number)
        if card.is_winner():
            print(f"card won!\n{card}")
            has_winner = True
            score = card.get_score()
            print(f"card score is {score}, product is {score * number}")
            last_winning_score = score * number

# print(cards)

print(f"{last_winning_score=}")

