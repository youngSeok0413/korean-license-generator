import re

# 결과를 저장할 집합 (중복 제거용)
unique_lowercase_words = set()

# memo.txt 파일 읽기
with open("memo.txt", "r", encoding="utf-8") as file:
    for line in file:
        # 소문자만 추출
        lowercase_parts = re.findall(r'[a-z]+', line)
        # 각 소문자 문자열을 중복 없이 추가
        for word in lowercase_parts:
            unique_lowercase_words.add(word)

# 결과 출력
for word in sorted(unique_lowercase_words):
    print(word)
