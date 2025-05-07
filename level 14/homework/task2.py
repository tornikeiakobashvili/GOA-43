"""3) გააკეთეთ ყველა შესაძლო კომბინაცია (ვარიანტი) ლოგიკურ ოპერატორებზე: and, or, not.  კომენტარების საშვლაებით გვერდით მიუწერეთ შედეგი"""


# საწყისი მნიშვნელობები
a = True
b = False

# 1. and ოპერატორი
print(a and b)  # False

# 2. or ოპერატორი
print(a or b)   # True

# 3. not ოპერატორი
print(not a)    # False
print(not b)    # True

# 4. კომბინაცია and და or
print((a and b) or a)  # True

# 5. კომბინაცია or და and
print(a or (a and b))  # True

# 6. კომბინაცია not და and
print(not (a and b))   # True

# 7. კომბინაცია not და or
print(not (a or b))    # False

# 8. უფრო დიდი კომბინაცია: not, and, or
print(not (a and (b or a)))  # False

# 9. უფრო დიდი კომბინაცია: and, or, not
print((not a or b) and (a or not b))  # False

# 10. სულ ყველაფერი ერთად
print(not (a and b) or (a and not b))  # True
