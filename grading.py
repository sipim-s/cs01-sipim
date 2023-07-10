score_work= int(input("กรุณากรอกคะแนนเก็บ"))
score_mid= int(input("กรุณากรอกคะแนนกลางภาค"))
score_final= int(input("กรุณากรอกคะแนนปลายภาค"))

if score >=80:
    grade = "A"
elif score >=75:
    grade = "B+"
elif score >=70:
    grade = "B"
elif score >=65:
    grade = "c+"
elif score >= 60:
    grade= "c"
elif score >=55:
    grade = "D+"
elif score >=50:
    grade = "D"
else:
    grade= "F"
    print("เกรดของคุณคือ:",grade)

