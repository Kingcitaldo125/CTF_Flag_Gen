#!/usr/bin/python

from os import system
from itertools import combinations as comb

def main():
    infile = 'asdf.txt'
    key = 'Prestidigitation'
    outfile = 'out.txt'
    hexfile = 'hex.txt'
    command = f"openssl aes128 -nosalt -in {infile} -out {outfile} -pass pass:{key} >/dev/null"

    # Example Flag (total flag len must be a multiple 16)
    # flag{abcdefghij}

    flag_prefix='flag{'
    flag_suffix='}'

    #banner_size = 10
    banner_size = 2

    printable_chars = ''.join([chr(i) for i in range(33,127)])

    results_file = open('results.txt', 'w')

    for gen_flag in comb(printable_chars, banner_size):
        # Generate the actual flag; See 'Example Flag' above for an example.
        gen_flag = flag_prefix + ''.join(gen_flag) + flag_suffix

        # Write out the flag contents to the file OpenSSL will read from
        with open(infile, 'w') as f:
            f.write(gen_flag)
            f.flush()

        # Execute the openssl encryption operation.
        # AES 128 (no salt, no IV, just a plain 128 bit block cypher operation).
        # Key size should be 16 bytes (128 bits).
        system(command)

        # Extract the hex value information from the 
        system(f'hexdump -C {outfile} >{hexfile}')

        # Write out the hexdump information to a single line in our results file.
        # A single line should associate the current flag combination result
        # with the hex information.
        with open(hexfile) as f:
            results_file.write(gen_flag)
            results_file.write('\n')
            results_file.write(f.read())
            results_file.write('\n\n')

        # cleanup
        system(f'rm {infile} {outfile} {hexfile}')

    # Finish writing out the results.
    results_file.flush()
    results_file.close()

if __name__ == "__main__":
    main()
