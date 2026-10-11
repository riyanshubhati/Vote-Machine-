first_party = "BJP"
second_party = "CONGRESS"
third_party = "SP"

age = int(input("Enter your age: "))
if(age>=145 or age<=0):
     print("Invalid Age")
elif (age>=18):
    print("You can vote.")
    user = input("Enter your party's name which you want to vote (Enter name in capital letters only!): ")
    if(user==first_party):
        print(f"You chose Bharatiya Janta Party which is the party of Narendra Modi, Thanks for voting, Your vote is counted")

    elif(user == second_party):
        print(f"You chose {second_party} which is the party of Rahul Gandhi, Thanks for voting, Your vote is counted")

    elif (user == third_party):
            print(f"You chose Samajwadi Party which is the party of Akhilesh Yadav, Thanks for voting, Your vote is counted")
else:
     print("You cannot vote") 
            
