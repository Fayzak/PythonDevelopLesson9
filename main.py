import random
cards = [6, 7, 8, 9, 10, "V", "D", "K", "T"]
lears = ["♥", "♦", "♠", "♣"]


class DurakGame:
    def __init__(self, x, y):
        self.player = x
        self.computer = y

    def logic(self):
        h_hand = self.player
        c_hand = self.computer
        c_card = random.choice(c_hand)
        print("Карта компьютера: {}".format(c_card))
        n = int(input("Введите номер карты: "))
        h_card = h_hand[n]
        print("Ваша карта: {}".format(h_card))

        # Приравняем значения буквенных карт к численным
        if c_card[0] == "T":
            c_card = c_card.replace("T", "14")
        elif c_card[0] == "K":
            c_card = c_card.replace("K", "13")
        elif c_card[0] == "D":
            c_card = c_card.replace("D", "12")
        elif c_card[0] == "V":
            c_card = c_card.replace("V", "11")

        if h_card[0] == "T":
            h_card = h_card.replace("T", "14")
        elif h_card[0] == "K":
            h_card = h_card.replace("K", "13")
        elif h_card[0] == "D":
            h_card = h_card.replace("D", "12")
        elif h_card[0] == "V":
            h_card = h_card.replace("V", "11")

        if c_card[-1] == h_card[-1]:
            if int(c_card[:-1]) > int(h_card[:-1]):
                print("Computer wins!")
            elif int(c_card[:-1]) == int(h_card[:-1]):
                print("Одинаковые карты. Ничья")
            else:
                print("Human wins!")
        else:
            print("Разные масти")


if __name__ == "__main__":
    deck = []
    player_hand = {}
    computer_hand = {}

    def gen_deck():
        """
        Формируем колоду
        :return:
        """
        for i in range(9):
            for j in range(4):
                _card = str(cards[i]) + lears[j]
                deck.append(_card)
        return deck

    gen_dec = gen_deck()

    def gen_h_hand():
        """
        Рука игрока
        :return:
        """
        for i in range(6):
            player_hand[i] = random.choice(gen_dec)
            gen_dec.remove(player_hand[i])
        print("Рука игрока: {}".format(player_hand))
        return player_hand

    def gen_c_hand():
        """
        Рука игрока
        :return:
        """
        for i in range(6):
            computer_hand[i] = random.choice(gen_dec)
            gen_dec.remove(computer_hand[i])
        print("Рука Компьютера: {}".format(computer_hand))
        return computer_hand

    # Перердаем классу игровой логики сформированные руки
    h = gen_h_hand()
    c = gen_c_hand()
    g = DurakGame(h, c)
    g.logic()