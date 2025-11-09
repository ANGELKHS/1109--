park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

# 90점 이상인 과목의 key만 출력 (dictionary comprehension 사용)
high_scores = {k: v for k, v in park.items() if v >= 90}

print(high_scores.keys())