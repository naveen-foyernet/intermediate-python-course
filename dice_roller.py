import random
def main(min,max):
  while True:
    print('You rolled a die')
    print(f"your number  :{random.randint(min,max)}")
    choice = input("Do you want roll the dice again? (yes/no)")
    if choice.lower() == 'no':
        break
if __name__== "__main__":
  main(1,6)