"""
학생1: 영어: 100, 국어: 100
학생2: 영어: 90, 국어: 80
학생3: 영어: 70, 국어: 50
학생4: 영어: 50, 국어: 100
학생5: 영어: 30, 국어: 20
"""
# 같은 정보여도 여러가지로 표현할 수 있다


students = ["학생1", "학생2", "학생3", "학생4", "학생5"]
eng_scores = [100, 90, 70, 50, 30]
kor_scores = [100, 80, 50, 100, 20]

print(students[0])
print(eng_scores[0])
print(kor_scores[0])

student_info = [
    ["학생1", 100, 100],
    ["학생2", 100, 100],
    ["학생3", 100, 100],
    ["학생4", 100, 100],
    ["학생5", 100, 100]
]
print(student_info[0])