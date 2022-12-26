test = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''


with open('input/day25.sql') as f:
    text = f.read()

numbers = text.splitlines()

snafu = {'0': 0, '1': 1, '2': 2,  '=': -2, '-': -1, }

total = 0

for number in numbers:
    trans = 0
    for i, digit in enumerate(number[::-1]):
        trans += snafu[digit]*(5**i)
    total += trans

print(total)
number = total


snafu_number = [0 for _ in range(int(len(str(number))*2))]
i = len(snafu_number)-1
while number > 0:
    snafu_number[i] += number % 5
    if (snafu_number[i]) >= 3:
        snafu_number[i-1] += 1
    number //= 5
    i -= 1

snafu_number = [list(snafu.keys())[i % 5] for i in snafu_number]
while snafu_number[0] == "0":
    snafu_number.pop(0)
print(''.join(snafu_number))
