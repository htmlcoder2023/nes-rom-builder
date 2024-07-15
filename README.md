# nes-rom-builder

This is a Python program that attempts to build matching game ROMs by brute-forcing every possible ROM combination for mapper 0. There is also a .txt file that can pasted into cmd that provides information about the game's hashes. If you are willing to add a .txt file that contains a game's hashes for this project, open a pull request.

The format for the text file is like this:

Line 1: [Game Name]

Line 2: [CRC32 of Unheadered ROM]

Line 3: [MD5 of Unheadered ROM]

Line 4: [SHA1 of Unheadered ROM]

Line 5: [SHA256 of Unheadered ROM]

Line 6: [CRC32 of Headered File]

Line 7: [MD5 of Headered File]

Line 8: [SHA1 of Headered File]

Line 9: [SHA256 of Headered File]

Lines 10-25: [The decimal equivalent of each byte in the header.]

Line 26: [File size]
