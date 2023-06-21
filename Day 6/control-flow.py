minAge = 16
applicantAge = 19

match applicantAge :
    case 16:
        print("Allowed")
    case 17|18:
        print("Supper allowed")
    case _:
        print("Declined")

# if applicantAge == minAge:
#     print("Allowed")
# elif applicantAge > minAge:
#     print("Super Allowed")
# else:
#     print("Declined")
