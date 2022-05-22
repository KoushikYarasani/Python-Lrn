#welcome code
print("#########################|Tip Calculator|#########################")

#total bill
bill = input("What is the total bill: ")

#persentage tip
tip_persentage = input("How much persent of tip do you wanna give? 0,10,12 or 15: ")

#how many memebers to split
split_bill = input("How many peaple to split the bill: ")

#calculating
tip_persentage = int(tip_persentage)
tip = tip_persentage / 100

total_bill = int(bill) + tip
spliting_persons_bill = (total_bill) / int(split_bill)
# spliting_persons_bill = round(spliting_persons_bill, 2)
#Or
#spliting_persons_bill = "{:.2f}".format(spliting_persons_bill) 
spliting_persons_bill = round(spliting_persons_bill, 2) 

#print
print(f"Each has to pay: {spliting_persons_bill}")
