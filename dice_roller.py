import random
def main(min,max):
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
   roll = random.randint(1,6)
  dice_sum += roll
  print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')
  # while True:
#  dice_rolls = 2
#  for i in range(0,dice_rolls):
#   roll = random.randint(1,6)
#  print(f'You rolled a {roll}')
    # print(f"your number  :{random.randint(min,max)}")
    # choice = input("Do you want roll the dice again? (yes/no)")
    # if choice.lower() == 'no':
        # break
if __name__== "__main__":
  main(1,6)