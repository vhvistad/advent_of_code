import time

def shuffle(deck):
    first, second = deck[:len(deck)//2], deck[len(deck)//2 + len(deck)%2:]
    shuffled = []
    for i in range(len(deck)):
        if i % 2 == 0:
            shuffled.append(first.pop(0))
        else:
            shuffled.append(second.pop(0))
    return shuffled

def shuffles_needed(original_deck):
    times_shuffled = 0
    shuffled_deck = []

    while shuffled_deck != original_deck:
        if times_shuffled == 0:
            shuffled_deck = original_deck

        shuffled_deck = shuffle(shuffled_deck)
        times_shuffled += 1

    return times_shuffled

def make_deck(size):
    deck = []

    for i in range(1, size+1):
        deck.append(i)
    
    return deck

if __name__ == "__main__":
    #deck = make_deck(52)
    start_time = time.time()

    size = 0
    shuffles = 0
    while shuffles != 13:
        size += 2
        deck = make_deck(size)
        shuffles = shuffles_needed(deck)
        print(f'Deck-size = {size}')

    print(f'Result: {size} cards.')
    print("--- Finished in %s seconds ---" % (time.time() - start_time))