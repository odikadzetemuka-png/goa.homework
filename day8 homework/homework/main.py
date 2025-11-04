# 1) დაწერეთ if-else statement, სადაც თუ საათი ნაკლებია ათზე დაპრინტეთ, 'დილამშვიდობისა', თუ საათი ნაკლებია ოცზე მაშინ დაწერეთ 'საღამო მშვიდობისა მშვიდობისა', სხვა შემთხვევაში გამოიტანეთ 'ღამე მშვიდობისა'
# 2) მიიღებთ ტემპერატურა, რომელიც იქნება მთელი რიცხვი, თუ ტემპერატურა ნაკლებია ნულზე გამოიტანეთ 'ცივა', თუ ტემპერატურა ნაკლებია 15ზე გამოიტანეთ 'გრილა', სხვა შემთხვევაში გამოიტანეთ 'ცხელა'

# dro=int(input("enter your dro:"))

# if dro<10:
#     print("dilamshvidobisa")
# elif dro<18:
#     print ("sagamomshvidobisa")
    
# else:
#     print("gamemshvidobisa")



# temperatura=int(input("enter your temperatur"))
# if temperatura<-5 and temperatura>15 :
#     print("civa")
    
# elif temperatura<15:
#     print("grila")

# else:
#     print("tbila")



# if elif-ის მეშვებოით მომხმარებლისაგნ მიღებული ქულა საატესტო შეამომწე თუ 90ზე და 100 შორის არის მაშინ აიღო მან A თუ 80სა და 90ს შორის არის მაშინ მან აიღო B თუ 70სა და 80 შორის არის მაშინ მან აიღო C თუ 
# რიცხვი 60სა და 70ს შორის არის მაშინ მან აიღო C-(მინუსით))
score= int(input("enter your score "))

if score> 90 and score <+ 100:
    print("sheni shefasea: A")

elif score >= 80 and score <=90:
    print("sheni shefaseba: B")
elif score >= 70 and score <80:
    print("sheni shefaseba: C")
elif score >= 60 and score <70:
    print("sheni shefaseba: C-")

else:
    print("qula dzalian dabalia an arasworia")
