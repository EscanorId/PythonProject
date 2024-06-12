import os

item = ["Processor", "VGA", "RAM", "Power Supply", "Casing"]
stockStore = [30, 20, 15, 45, 32]
stockInventory = [55, 43, 12, 23, 44]

def move(param1, param2):
  chooseItem = int(input("Input item number (1-5): "))
  stock = int(input("How many : "))
  param1[chooseItem-1] -= stock
  param2[chooseItem-1] += stock
  print("Item has been moved")
  input("Press enter to continue")


while True:
  os.system("clear")
  print("="*33+ "  "+ "="*34)
  print("|{:^32}| |{:^32}|".format("Store", "Inventory"))
  print("="*33+ "  "+ "="*34)
  print("|{:^3}|{:^17}|{:^10}| |{:^3}|{:^17}|{:^10}|".format("No", "Item", "Stock", "No", "Item", "Stock"))
  print("-"*33+ "  "+ "-"*34)
  for i in range(5):
    print("|{:^3}|{:<17}|{:^10}| |{:^3}|{:<17}|{:^10}|".format(i+1, item[i], stockStore[i], i+1, item[i], stockInventory[i]))
  print("="*33+ "  "+ "="*34)
  choice = int(input("Option:\n1. Store > Inventory\n2. Inventory > Store\n\nChoice (1/2) : "))
  if choice == 1:
    move(stockStore, stockInventory)
  elif choice == 2:
    move(stockInventory, stockStore)
  else:
    input("Please only choose 1 or 2\nPress enter")
