# def calculate_lcm(x, y): 
 
#     if x > y: 
#         greater = x 
#     else: 
#         greater = y 
# while(True): 
#             if((greater % x == 0) and(greater % y == 0)): 
#                 lcm = greater 
#                 break 
#             greater += 1 
#             return lcm
# Источник: https://pythonstart.ru/list/nahozhdenie-nok-i-nod-v-python-primery


test_str = "45 + 25 * 10"

print("The original string is : " + test_str)

res = eval(test_str)

print("The evaluated result is : " + str(res))