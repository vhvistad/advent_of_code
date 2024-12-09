import math
import copy

class Display:
    def __init__(self, adress):
        self.adress = adress
        self.digit = 0
        self.segments = {
            "A": True,
            "B": True,
            "C": True,
            "D": True,
            "E": True,
            "F": True,
            "G": False,
        }
        self.nums = {
            '0': '1111110',
            '1': '0110000',
            '2': '1101101',
            '3': '1111001',
            '4': '0110011',
            '5': '1011011',
            '6': '1011111',
            '7': '1110000',
            '8': '1111111',
            '9': '1111011'
        }

    def increment(self):
        if self.digit == 9:
            self.digit = 0
        else:
            self.digit += 1
        for i, segment in enumerate(self.segments.keys()):
            self.segments[segment] = bool(int(self.nums[str(self.digit)][i]))

    def __eq__(self, other):
        for k, v in self.segments.items():
            if v != other.segments[k]:
                return False
        return True

    def __str__(self):
        return str(self.segments)
            

class Collection:
    def __init__(self):
        self.number = 0
        self.displays = {}
        self.alt_displays = {}
        for char in 'IHGFEDCBA':
            self.displays[char] = Display(char)
            self.alt_displays[char] = Display(char)
        self.switches = [
            ['AC', 'IB'],
            ['BD', 'EG'],
            ['GF', 'DE'],
            ['BA', 'BB'],
        ]

    def increment(self, step):
        self.number += step
        exponent = math.log10(self.number)

        if exponent % 1 == 0:
            print(self.number)
            exponent = int(exponent)
            for char in 'IHGFEDCBA'[-(exponent+1):]:
                self.displays[char].increment()
        else:
            self.displays['A'].increment()
        
        
        for a, b in self.switches:
            self.switch_segments(a, b)
        
    def switch_segments(self, a, b):
        self.alt_displays = copy.deepcopy(self.displays)
        test = copy.deepcopy(self.displays)
        display_a = a[0]
        segment_a = a[1]
        display_b = b[0]
        segment_b = b[1]
        test1 = test[display_a].segments[segment_a]
        test2 = test[display_b].segments[segment_b]
        self.alt_displays[display_b].segments[segment_b] = test1
        self.alt_displays[display_a].segments[segment_a] = test2
        # print(f'self.alt_displays[{display_b}].segments[{segment_b}] = {self.alt_displays[display_b].segments[segment_b]}\nself.alt_displays[{display_a}].segments[{segment_a}] = {self.alt_displays[display_a].segments[segment_a]}')

        # for char, display in self.alt_displays.items():
        #     print(f'{char} (self.displays):     {str(display)}')
        #     print(f'{char} (self.alt_displays): {str(self.alt_displays[char])}\n')

    def displays_equal(self):
        for k in 'IHGFEDCBA':
            v = self.displays[k]

        # for k, v in self.displays.items():
            if v != self.alt_displays[k]:
                position = 'ABCDEFGHI'.index(k)
                return False, position
        
        return True, 0


if __name__ == '__main__':
    collection = Collection()
    result = 0

    percent = 0.0

    # n = 10
    n = 1_000_000_000
    i = 0
    step = 1
    while i < n:
    # for i in range(n):
        collection.increment(step)

        equal, position = collection.displays_equal()
        if equal:
            result += 1
            i += 1
            step = 1
        else:
            print(f'Not equal, skipping i from {i} to {i+pow(10, position)}')
            step += pow(10, position)
            i += step

        if i % 1_000_000 == 0 and i != 0:
            percent += 0.1
            formatted = "{:.1f}".format(percent)
            print(f'Progress: {formatted}%')
        # if i % 1000 == 0:
        #     print(f'i = {i}')

    print(f'Result = {result}')

    