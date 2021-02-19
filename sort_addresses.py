import csv

FILENAMES = [
    "1.00.txt",
    "1.03.txt",
    "1.05B.txt",
    "1.09D.txt",
    "1.10.txt",
    "1.12A.txt",
    "1.13C.txt",
    "1.13D.txt",
    "LoD 1.14C.txt",
    "LoD 1.14D.txt",
]

for filename in FILENAMES:
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        lines = list(reader)

    header = lines[0]
    lines = lines[1:]

    lines.sort(key=lambda line: (line[0], line[1]))

    with open(filename, mode='w', newline="") as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(header)
        writer.writerows(lines)
