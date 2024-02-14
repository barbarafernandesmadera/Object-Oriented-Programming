import random

def deal_cards():
  deck = ['J', 'Q', 'K', 'A'] + [str(i) for i in range(2,11)]
  suits = ['♠', '♥', '♦', '♣']
  cards = [f'{rank}{suit}' for rank in deck for suit in suits]
  #[f'{rank}{suit} for rank in deck for suit in suits]
  random.shuffle(cards)
  return cards[:5]

def print_cards(cards):
  print("Suas cartas:")
  print(" ".join(cards))

def get_bet(credits):
  while True:
    bet = int(input("Place your bet (i to {}): ".format(credits)))
    if 1 <= bet <= credits:
      return bet
    print("Aposta inválida. Por favor, tente novamente")

def swap_cards(cards):
  while True:
    indices = input("Selecione as cartar para troca(exemplo 1,2,3): ").split()
    if all(index.isdigit() for index in indices) and len(indices) <= 5:
      indices = [int(index) - 1 for index in indices]
      return [cards[i] if i in indices else card for i, card in enumerate(cards)]
    print("Entrada inválida. Por favor tente novamente.")

def get_hand_value(cards):
  ranks = [card[:-1] for card in cards]
  suits = [card[-1] for card in cards]
  rank_counts = {rank: ranks.count(rank) for rank in ranks}
  suit_counts = {suit: suits.count(suit) for suit in suits}
  sorted_ranks = sorted(ranks, key=lambda x: ranks.index(x))

  if len(set(suits)) == 1 and all(int(sorted_ranks[i]) + 1 == int(sorted_ranks[i+1]) for i in range(4)):
    return "Straight Flush", 100
  if len(set(suits)) == 1 and sorted_ranks == ['10', 'J', 'Q', 'K', 'A']:
    return "Royal Straight Flush", 200
  if len(set(rank_counts.values())) == 2 and 3 in rank_counts.values():
    return "Full hand", 20
  if 4 in rank_counts.values():
    return "Quadra", 50
  if len(set(suits)) == 1:
    return "Flush", 10
  if all(int(sorted_ranks[i]) + 1 == int(sorted_ranks[i + 1]) for i in range(4)):
    return "Straight", 5
  if len(set(rank_counts.values())) == 3 and 2 in rank_counts.values():
    return "Two pairs", 2
  if len(set(rank_counts.values())) == 3 and 4 in rank_counts.values():
    return "Trinca", 2

  return "Sem combinação", 0

def play_game():
  credits = 200

  while credits > 0:
    print("Credits:", credits)
    bet = get_bet(credits)
    cards = deal_cards()
    print_cards(cards)

    swap = input("Trocar alguma carta? (S/N): ")
    if swap.lower() == 'S':
      cards = swap_cards(cards)
      print_cards(cards)

    combination, payout = get_hand_value(cards)
    credits += payout * bet

    print("Combinação:", combination)
    print("Pagamento:", payout * bet)
    print("Credits: ", credits)

  print("Fim de jogo")

play_game()
