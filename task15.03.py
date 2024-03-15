# 1. while istifadə edərək listin məlumatlarını çap edin.
# 2. Hərflərdən ibarət list yaradın. While və continue istifadə edərək bəzi hərflərin üzərindən keçərək digər hərfləri çap edin
# 3.  while istifadə edərək Sıfırdan daxil edilmiş ədədə qədər(ədəd daxil olmaqla) çap edin
# 4. Static bir password yaradin. Daxil edilen parolun 3 dəfə səhv yazılma şansı olsun və hər səhv yazıldıqda 1 şansınız azaldı mesajı versin. Əgər şanslar bitərsə block olundunuz mesajı verilsin. For-dan istifadə edin
# 5. Test sistemi yaradin. Doğru və yanlış sualların sayını hesablasın. Əlavə olaraq 4 səhv 1 düz cavabı silib son nəticəni çap edin




# task1 

# list1 = ["bazarstore", "araz", "bravo", "rahat"]
# i = 0

# while i < len(list1):
#     print(list1[i])
#     i+=1



# task2 
    
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
# index = 0
# while index < len(alphabet):   
#     if alphabet[index] == "d":
#         index+=1
#         continue
#     print(alphabet[index])
#     index+=1



# task3 

# number = int(input("nomre daxil et: "))

# i = 0

# while i <= number:

#     print(i)
#     i+=1

    


# task4 


# for i in range(3):
#     password = input("Sifreni reqemle daxil edin ve gozleyin: ")
#     if password == "2024":
#         print("Daxil olundu")
#         break
#     else:
#         print("Maksimum 3 sehv ede bilersiniz eks halda sansiniz olmayacaq")
# else:
#     print("prosesde sehv ve sansiniz bitti")





# task5 


# test1 = input("Misal həll edin: 8 + 2 = ? a)40 b)10 c)20 d)35  " "variantlarin birini sec:")
# test2 = input("Misal həll edin: 6 + 1 = ? a)15 b)7 c)10 d)15  " "variantlarin birini sec:")
# test3 = input("Misal həll edin: 10 - 5 = ? a)15 b)20 c)5 d)50 "  "variantlarin birini sec:")
# test4 = input("Misal həll edin: 10 + 2 - 6 = ? a)15 b)20 c)6 d)50  "  "variantlarin birini sec:")
# test5 = input("Misal həll edin: 2 + 3 + 5 = ? a)50 b)20 c)10  d)60 "  "variantlarin birini sec:")
# test6 = input("Misal həll edin: 15 + 8 + 2 = ?? a)15 b)25 c)10  d)50 "  "variantlarin birini sec:")
# test7 = input("Misal həll edin: 55 + 5 + 10 = ?? a)15 b)70 c)10  d)50 "  "variantlarin birini sec:")
# test8 = input("Misal həll edin: 10 + 10 + 10 = ? a)15 b)30 c)10  d)40  "  "variantlarin birini sec:")
# test9 = input("Misal həll edin: 5 + 8 + 2 = ? a)20 b)15 c)10  d)55  "  "variantlarin birini sec:")
# test10 = input("Misal həll edin: 15 + 5 + 10 + 10 = ? a)15 b)40 c)10  d)60  "  "variantlarin birini sec:")

# true_answer = 0
# false_answer = 0

# if test1 == "a":
#     true_answer += 1
# else:
#     false_answer +=1

# if test2 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if test3 == "c":
#     true_answer += 1
# else:
#     false_answer +=1

# if test4 == "c":
#     true_answer += 1
# else:
#     false_answer +=1

# if test5 == "a":
#     true_answer += 1
# else:
#     false_answer +=1

# if test6 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if test7 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if test8 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if test9 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if test10 == "b":
#     true_answer += 1
# else:
#     false_answer +=1

# if false_answer %4 == 0:
#     true_answer -= 1

# print("Dogru cavablar : ", true_answer)
# print("Sehv cavablar : ", false_answer)