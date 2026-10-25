# ================================
# MY SCHOOL SUBJECT PLANNER
# ================================
 
# PART 1 — TUPLES
 
student_profile = ("Riches", "Grade 4", "Section West", 6)
 
print("Student Profile:", student_profile)
 
 
# PART 2 — ACCESSING TUPLE ELEMENTS
 
student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]
 
print("\nStudent Name:", student_name)
print("Grade:", grade)
print("Section:", section)
print("Total Subjects:", total_subjects)
 
print("First two details:", student_profile[0:2])
 
 
# PART 3 — SETS
 
monday_subjects = {"Dictation", "English Composition", "Maths", "Computing", "Art"}
tuesday_subjects = {"Sports", "English Composition", "Maths", "Arts", "U.C.M.A.S"}
 
print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
 
 
# PART 4 — MODIFYING SETS
 
monday_subjects.add("Library")
print("\nAfter adding Library to Monday:", monday_subjects)
 
monday_subjects.discard("Dictation")
print("After removing Art from Monday:", monday_subjects)
 
tuesday_subjects.add("Computing")
print("After adding Computer to Tuesday:", tuesday_subjects)
 
tuesday_subjects.discard("Maths")
print("After removing Music from Tuesday:", tuesday_subjects)
 
 
# PART 5 — SET OPERATIONS
 
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects)
 
print("\nAll Subjects:", all_subjects)
print("Common Subjects:", common_subjects)
print("Only Monday Subjects:", only_monday)
print("Only Tuesday Subjects:", only_tuesday)
print("Different Subjects:", different_subjects)
 
 
# FINAL SUMMARY
 
print("\n================================")
print("SCHOOL  SUBJECT PLANNER")
print("================================")
print("Student:", student_name)
print("Grade:", grade)
print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print("Subjects on Both Days:", common_subjects)
print("All Unique Subjects:", all_subjects)
print("================================")