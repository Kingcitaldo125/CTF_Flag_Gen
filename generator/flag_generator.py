from random import randrange

class FlagGenerator:
    def __init__(self, flag_prefix, banner_size) -> None:
        self.flag_prefix = flag_prefix
        self.banner_size = banner_size
        # 133t 5p34k
        ls = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(0,10)] + ['@', '_']
        self.printable_chars = ''.join(ls)

    def generate(self):
        lpc_len = len(self.printable_chars)
        midlist = [self.printable_chars[randrange(0, lpc_len)] for i in range(self.banner_size)]
        return self.flag_prefix + "{" + ''.join(midlist) + "}"

if __name__ == "__main__":
    fg = FlagGenerator(flag_prefix='flag', banner_size=4)

    for i in fg.generate():
        print(f'Flag: {i}')
