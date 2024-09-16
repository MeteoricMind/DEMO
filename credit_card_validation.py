credit = "3782-8223-6310-005"
credit_card = credit.replace('-','').replace(' ','')
a = len(credit_card)
sum_0= 0
list_even = []
for i in range (a,0,-1):
    if i%2 != 0:
        sum_0 = sum_0 + int(credit_card[i])
    else:
        list_even.append(int(credit_card[i-1]))


list_even_double = list(map(lambda x: x*2,list_even))
final_list=[]
final_list_1 = []
for j in list_even:
    if j>=10:
        list_sum_even_double = list(map(lambda x: x[0]+x[1],list_even_double))
        final_list.append(list_sum_even_double)
    else:
        final_list_1.append(j)
sum_2 = sum(final_list)
sum_1 = sum(final_list_1)
total = sum_2+sum_1
total_sum = total + sum_0
if total_sum%10 == 0:
    print("Valid")
else:
    print("Not valid")
    
    










# list = []
# for i in range(a,0,-1):
#     if i%2 == 0:
#         list.append(credit_card[i-1])
#     else:
#         continue


# print(list)


