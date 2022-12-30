from generator.flag_generator import FlagGenerator

def main(outfile='results.txt'):
    fg = FlagGenerator(flag_prefix='flag', banner_size=10)
    results_file = open(outfile, 'w')

    # Generate 1,000 flags
    for i in range(1_000):
        gen_flag = fg.generate()
        # Generate the actual flag; See 'Example Flag' above for an example.
        results_file.write(gen_flag)
        results_file.write('\n\n')

    # Finish writing out the results.
    results_file.flush()
    results_file.close()

if __name__ == "__main__":
    main()
