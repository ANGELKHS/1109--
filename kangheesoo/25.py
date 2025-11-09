keys = input().split()
values = list(map(int, input().split()))

# 딕셔너리 생성 (zip 사용)
data = dict(zip(keys, values))

result = {k: data[k] for k in ['brovo','charlie','echo','foxtrot','golf']}

print(result)