from generator.flag_generator import FlagGenerator

def main(outfile='results.txt'):
    # Example Flag (total flag len must be a multiple 16)
    # flag{abcdefghij}

    fg = FlagGenerator(flag_prefix='flag', banner_size=4)
    results_file = open(outfile, 'w')

    for gen_flag in fg.generate():
        # Generate the actual flag; See 'Example Flag' above for an example.
        results_file.write(gen_flag)
        results_file.write('\n\n')

    # Finish writing out the results.
    results_file.flush()
    results_file.close()

if __name__ == "__main__":
    main()
