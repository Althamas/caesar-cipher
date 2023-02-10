def highest_bider(dic):
    high = 0
    winner = ""
    for bidder in dic:
        bid_amount = dic[bidder]
        if bid_amount > high:
            high = bid_amount
            winner = bidder
    print(f"Highest bid was done by {winner} that is {high}")
    
from replit import clear
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
End = True
dis = {}
while End:
 name = input("Enter your name:")
 bit = int(input("Enter your bid: $"))
 dis[name] = bit
 ask = input("Is there anyone else to bid:").lower()
 if ask == "no":
     highest_bider(dis)
     End = False
     
 if ask == "yes":
     clear()