import subprocess
with open('airdrop.txt', 'r+') as f: #r+ does the work of rw
    lines = f.readlines()
    for i, line in enumerate(lines):
        list_files = subprocess.Popen(["spl-token", "transfer", "--allow-unfunded-recipient", "--fund-recipient", "8YPwxJ7geGS8jjtTYzKaYbgkFWBQQHKtfHS4g2nzXcHt", "7",lines[i].strip()], )
        list_files.wait()
    f.seek(0)
    for line in lines:

        f.write(line)
        print(line)