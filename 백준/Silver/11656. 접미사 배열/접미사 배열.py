import sys
input = sys.stdin.readline
text = input().strip()
res = [text[x:] for x in range(len(text))]
print("\n".join(sorted(res)))