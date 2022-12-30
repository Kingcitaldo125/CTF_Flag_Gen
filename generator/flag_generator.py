from itertools import combinations as comb

class FlagGenerator:
    def __init__(self, flag_prefix, banner_size) -> None:
        self.flag_prefix = flag_prefix
        self.banner_size = banner_size
        # 133t 5p34k
        ls = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(0,10)] + ['@', '_']
        self.printable_chars = ''.join(ls)

    def generate(self):
        for item in comb(self.printable_chars, self.banner_size):
            yield self.flag_prefix + "{" + ''.join(item) + "}"

if __name__ == "__main__":
    fg = FlagGenerator('flag', 4)
    for i in fg.generate():
        print(f'Flag: {i}')
