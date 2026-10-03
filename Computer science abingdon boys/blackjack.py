#♣♦♥♠
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']: return 10
        if self.rank == 'A': return 11
        return int(self.rank)

    def __str__(self):
        RED = "\033[31m"
        CYAN = "\033[36m"
        RESET = "\033[0m"
        color = RED if self.suit in ['♥', '♦'] else CYAN
        return f"{color}{self.suit}{self.rank}{RESET}"

class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self, bet):
        self.cards = []
        self.bet = bet
        self.is_split = False

    def add_card(self, card):
        if card: self.cards.append(card)

    def calculate_value(self):
        val = sum(card.get_value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while val > 21 and aces:
            val -= 10
            aces -= 1
        return val

    def can_split(self):
        return len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank

    def is_blackjack(self):
        return len(self.cards) == 2 and self.calculate_value() == 21 and not self.is_split

    def __str__(self):
        return f"[{', '.join(str(x) for x in self.cards)}] (Total: {self.calculate_value()})"

class Money:
    def __init__(self, balance=100):
        self.balance = balance

    def adjust(self, amount):
        self.balance += amount

class Analytics:
    @staticmethod
    def get_hit_safety(hand, deck):
        if not deck.cards: return 0
        curr = hand.calculate_value()
        safe = sum(1 for c in deck.cards if curr + (c.get_value() if c.rank != 'A' else 1) <= 21)
        return (safe / len(deck.cards)) * 100

    @staticmethod
    def get_win_probability(player_hand, dealer_upcard, deck):
        p_val = player_hand.calculate_value()
        if p_val > 21: return 0.0, 0.0
        outcomes = []
        for hidden in deck.cards[:20]:
            d_val = dealer_upcard.get_value() + hidden.get_value()
            if d_val >= 17: d_val = 7
            outcomes.append(d_val)
        wins = sum(1 for d in outcomes if d > 21 or p_val > d)
        ties = sum(1 for d in outcomes if p_val == d)
        return (wins/len(outcomes))*100, (ties/len(outcomes))*100

def play_hand(hand, deck, bankroll, dealer_upcard):
    while hand.calculate_value() < 21:
        win_p, tie_p = Analytics.get_win_probability(hand, dealer_upcard, deck)
        safety = Analytics.get_hit_safety(hand, deck)
        print(f"\nHand: {hand}")
        print(f"Safety: {safety:.1f}% | Win: {win_p:.1f}%")
        
        opts = "([h]it, [s]tand"
        if len(hand.cards) == 2:
            opts += ", [d]ouble"
            if hand.can_split() and bankroll.balance >= hand.bet: opts += ", [p]split"
        opts += ")"
        
        choice = input(f"Action {opts}: ").strip().lower()
        if choice == 'h':
            hand.add_card(deck.deal_card())
            if hand.calculate_value() > 21:
                print(f"Busted: {hand}")
                break
        elif choice == 's':
            break
        elif choice == 'd' and len(hand.cards) == 2:
            if bankroll.balance >= hand.bet:
                bankroll.adjust(-hand.bet)
                hand.bet *= 2
                hand.add_card(deck.deal_card())
                print(f"Doubled: {hand}")
            break
        elif choice == 'p' and hand.can_split():
            return "split"
    return "done"

def game_round(bankroll):
    print(f"\n--- Balance: ${bankroll.balance} ---")
    try:
        bet_input = input("Bet (default 10): ").strip()
        bet = int(bet_input) if bet_input else 10
    except ValueError:
        bet = 10

    if bet > bankroll.balance:
        print("Not enough money!")
        return

    bankroll.adjust(-bet)
    deck = Deck()
    player_hands = [Hand(bet)]
    dealer_hand = Hand(0)

    for _ in range(2):
        player_hands[0].add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    print(f"Dealer shows: {dealer_hand.cards[0]}")

    if dealer_hand.is_blackjack():
        print(f"Dealer Blackjack: {dealer_hand}")
        if player_hands[0].is_blackjack():
            bankroll.adjust(bet)
            print("Push: Returned ${bet}")
        else:
            print("Dealer wins with Blackjack.")
        return

    i = 0
    while i < len(player_hands):
        curr = player_hands[i]
        if not curr.is_blackjack():
            res = play_hand(curr, deck, bankroll, dealer_hand.cards[0])
            if res == "split":
                card = curr.cards.pop()
                bankroll.adjust(-bet)
                h2 = Hand(bet)
                h2.is_split = True
                curr.is_split = True
                curr.add_card(deck.deal_card())
                h2.add_card(card)
                h2.add_card(deck.deal_card())
                player_hands.insert(i + 1, h2)
                continue
        i += 1

    if any(h.calculate_value() <= 21 for h in player_hands):
        print("\n--- Dealer's Turn ---")
        while dealer_hand.calculate_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        print(f"Dealer finished: {dealer_hand}")

        d_val = dealer_hand.calculate_value()
        for h in player_hands:
            p_val = h.calculate_value()
            if p_val <= 21:
                if h.is_blackjack():
                    win_amt = h.bet * 2.5
                    bankroll.adjust(win_amt)
                    print(f"Blackjack Win! +${win_amt}")
                elif d_val > 21 or p_val > d_val:
                    win_amt = h.bet * 2
                    bankroll.adjust(win_amt)
                    print(f"Hand wins! +${win_amt}")
                elif p_val == d_val:
                    bankroll.adjust(h.bet)
                    print(f"Push: Returned ${h.bet}")
                else:
                    print(f"Hand loses. -${h.bet}")
    else:
        print("\nAll player hands busted.")

wallet = Money(100)
while wallet.balance > 0:
    game_round(wallet)
    if wallet.balance <= 0:
        print("Game Over! You're out of money.")
        break
    if input("\nPlay again? (y/n): ").lower().strip() != 'y': break