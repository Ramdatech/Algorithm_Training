import sys
input = sys.stdin.readline
text = input().strip()
result = set()
for i in range(0, len(text)+1):
    for j in range(i+1, len(text)+1):
        result.add(text[i:j])
print(len(result))
