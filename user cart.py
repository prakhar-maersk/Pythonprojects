
# dict={"Bread": 100,
#       "Munch": 50,
#       "Kitkat":25,
#       "Dairy Milk":60,
#       "Perk":10,
#       "Neutella":200,
#       "Tomato Sauce":140,
#       "Soap":30,
#       "Chips":35,
#       "Waffers":35,
#       "Cold Drinks":70}

product=['Bread','Munch','Kitkat','Dairy Milk','Perk','Neutella','Tomato Sauce','Soap','Chips','Waffers','Cold Drinks']
price=[100,50,25,60,10,200,140,30,35,35,70]
def add():
    for i in range(len (product)):
        print(i+1,"  ", product[i],"  ",price[i])
    p=int (input("Enter product no. you want to add in cart\n"))
    amount=int(input("How much quantity\n"))
    if p<=len(product):
        cart.append(product[p].lower())
        
    else:
        print("Enter the no. of product that are visible in the list\n")
        add()
def remove():
    if len(cart)==0:
        print("Cart is already empty")
    else:
        r=input("Enter product name that you want to remove from cart\n").lower()
        print(r)
        if r in cart:
            cart.remove(r)
        else:
            print("Item was not found in cart")
def clear():
    cart.clear()
def show():
    print("items in cart are:\n")
    for i in cart:
        print(i)
def quit():
    pass

cart=[]
x=1
while(x!=5):
    print("Items in cart are",cart)
    try :
        x=int (input("What action do you want to perform? \n 1. Add\n 2. Remove\n 3. Clear\n 4. Show\n 5. Quit\n"))
        if x==1:
            add()
        elif x==2:
            remove()
        elif x==3:
            clear()
        elif x==4:
            show()
        elif x==5:
            break
        else:
            print("Enter correct value\n")
    except:
        print("Please enter number value from 1 to 5")
print("Final items in cart are:\n",cart,"\n")
print("Thank you")