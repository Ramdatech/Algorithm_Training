h, m = list(map(int, input().split()))
m_input = int(input())
total_m = h*60 + m + m_input
print(f"{total_m//60%24} {total_m%60}")