def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   Mars = weight*0.38
   Jupiter = weight*2.34

   print("\nOn Mars you would weigh", Mars, "pounds.\nOn Jupiter you would weigh", Jupiter, "pounds.")
      
   
if __name__ == '__main__':
   weight_on_planets()