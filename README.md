# rainbow-hash-cracker
A Python script to crack SHA256-hashed 4-digit numeric passwords using a rainbow table approach. It generates a dictionary of all 4-digit numbers hashed with SHA256, then matches against input hashes to find the original passwords.

This project is a Python script that tries to recover 4-digit numeric passwords hashed with SHA256. It works by creating a “rainbow table” , basically a dictionary of all 4-digit numbers and their SHA256 hashes.

Then, it reads a CSV file containing usernames and their hashed passwords and checks if any of those hashes match the ones in the table. If it finds a match, it figures out the original 4-digit password and saves the result in a new CSV output file.

This method only works for simple 4-digit numeric passwords and only for SHA256 hashes. It’s a basic but useful tool for learning how rainbow tables work in password cracking.
