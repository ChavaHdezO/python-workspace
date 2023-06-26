"""
#--------------------------------------------------
sams_age = 16
too_young = sams_age < 17
car_driver = sams_age >= 17

print(f"Is Sam too young to drive? {too_young}")
print(f"Can Sam drive a car? {car_driver}")
#--------------------------------------------------
old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321"
compare_new = new_password == repeat_new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")
#--------------------------------------------------
age = 15
adult_ticket = age >= 12

print(f"Buy one adult ticket: {adult_ticket}")
"""
student_name = "Sam"
math_grade = 88
science_grade = 75
english_grade = 90
geology_grade = 69
total_grade = math_grade + science_grade + english_grade + geology_grade
max_grade = 400
total_percentage = total_grade / max_grade * 100
print(f"Sam's total percentage is {total_percentage}%")
total_percentage = int(total_percentage)
did_student_pass = total_percentage >= 50
sporting_activities = bool(0)
print(f"Sam participated in sporting activities: {sporting_activities}")
print(f"Sam's total percentage as an integer is {total_percentage}%")
print(f"Sam passed to the next semester: {did_student_pass}")