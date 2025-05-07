"""3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ ოპერაციათა შედეგებს, გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები"""

# 1. and ოპერატორი
a = True and False   # False, რადგან and-ს უნდა ორივე True რომ შედეგიც True იყოს

# 2. or ოპერატორი
b = False or True    # True, რადგან or-ს საკმარისია ერთი True

# 3. not ოპერატორი
c = not False        # True, რადგან not აბრუნებს საწინააღმდეგოს

# 4. კომბინაცია and + or
d = (True or False) and (False or False)  # False, რადგან (True or False) = True, (False or False) = False, ბოლოს True and False = False

# 5. კომბინაცია not + and
e = not (True and True)   # False, რადგან (True and True) = True, და not True = False
