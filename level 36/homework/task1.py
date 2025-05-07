""""""
# coding_languages = ["js","python","c","c++","Swift","Rust","Kotlin","Dart","Ruby","Vala"]

# coding_languages[7] = "CMS-2"
# coding_languages[8] = "COMAL"

# print("პირველიდან 5-ის ჩათვლით:", l"anguages"[0:5])
# print("2-დან ბოლომდე:", "languages"[2:])
# print("4-დან 8-მდე:", "languages"[4:8])
    
# 10 პროგრამირების ენის სია
languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "C#", "Go", "Perl", "Assembly"]

# არასასურველი ენის ჩანაცვლება (ვთქვათ, არ გვიყვარს Assembly და ვცვლით Rust-ით)
languages[-1] = "Rust"
languages[8] = "COMAL"
# დადებითი slicing
print("პირველიდან 5-ის ჩათვლით:", languages[0:5])
print("2-დან ბოლომდე:", languages[2:])
print("4-დან 8-მდე:", languages[4:8])

# უარყოფითი slicing
print("მეექვსედან ბოლომდე:", languages[-6:])
print("მეექვსემდე ყველაფერი:", languages[:-5])
print("მეექვსეს ჩათვლით თავიდან ყველაფერი:", languages[:6])

# ბონუსი: სია შემობრუნებულად
print("სია შემობრუნებულად:", languages[::-1])
