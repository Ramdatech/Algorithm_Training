import sys
input = sys.stdin.readline
text = input().strip()
result = set()
for i in range(1, len(text)+1):
    for j in range(len(text)-i+1):
        result.add(''.join(text[j:j+i]))
print(len(result))