from hashlib import sha256
import csv


def hash_password_hack(input_file_name, output_file_name):
    # Generate rainbow table for 4-digit numbers
    hp = {}
    for i in range(1000, 10000):  # 10000 to include 9999
        hashed = sha256(str(i).encode()).hexdigest()
        hp[hashed] = i

    new_hp = {}
    with open(input_file_name, 'r' ) as fin:
        reader = csv.reader(fin)
        for row in reader:
            if len(row) < 2:
                continue
            name = row[0].strip()
            hash_value = row[1].strip()
            if hash_value in hp:
                new_hp[name] = hp[hash_value]
                print(f"Found match: {name} -> {hp[hash_value]}")

    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)
        for name, val in new_hp.items():
            writer.writerow([name, val])



if __name__ == "__main__":
    hash_password_hack(r"D:\Zahra\github\rainbow hash\input.csv", "D:\\Zahra\\github\\rainbow hash\\output.csv")