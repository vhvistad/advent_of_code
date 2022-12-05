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

def shuffle_13(original_deck):
    shuffled_deck = []

    for i in range(13):
        if i == 0:
            shuffled_deck = original_deck

        shuffled_deck = shuffle(shuffled_deck)

    return shuffled_deck == original_deck


if __name__ == "__main__":
    start_time = time.time()
    deck = [1, 2]
    size = len(deck)
    while True:
        deck = deck + [size + 1, size + 2]
        size += 2
        if shuffle_13(deck):
            break

    print(f'Result: {size} cards.')
    print("--- Finished in %s seconds ---" % (time.time() - start_time))