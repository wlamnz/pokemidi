# Pokemidi

Script used to generate a midi file by reading disassembled pokemon red music code.

Requires python 2.

Usage: pokemidi.py [-l LOOPS] [-t TEMPO] FILENAME

Example: pokemidi.py -l 2 -t 120 music/pallettown.asm
The above command will generate the midi file (output.mid) containing the pallet town music. The tempo set will be 120 and the music will loop two times.
