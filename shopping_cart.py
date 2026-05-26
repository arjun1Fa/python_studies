shopping_cart = []

while True:
    
    choice = int(input("Enter 1 If you want add an item\nEnter 2 if you want to delete an item\nEnter 3 if you want to view the cart\nEnter 4 to quit the cart\n"))
    if choice ==1:
        item = input("Enter item you want to input:\t")
        shopping_cart.append(item)
        print(item," has been added")

    elif choice == 2:
        if not shopping_cart:
            print("\nCart is empty!")
        else:

            print("Your cart:   ")
            
            for i , item in enumerate(shopping_cart):
                print(f" {i+1}, {shopping_cart[i]}")
                
            item = int(input("Enter the number of the item you want to delete:\t"))
            removed = shopping_cart.pop(item-1)
            print(removed, " has been removed")
       

    elif choice == 3:
        
            print("Your cart:   ")
           
            for i , item in enumerate(shopping_cart):
                print(f" {i+1}, {shopping_cart[i]}")


    elif choice == 4:
            break

    

