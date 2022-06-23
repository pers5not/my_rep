# Учащиеся в классе получают свои оценки как Pass/Fail. 60 и более баллов (из 100) означают, что оценка «зачетно». При более низких баллах ставится оценка «Неудовлетворительно». Кроме того, баллы выше 95 (не включены) оцениваются как «Высший балл». Заполните эту функцию, чтобы она возвращала правильную оценку.

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail
