import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
  if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
  elif roll == dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:
    print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

  # dice_rolls = 2
  # dice_sum = 0
  # for i in range(0,dice_rolls):
  #   roll = random.randint(1,6)
  #   dice_sum += roll
  # if roll == 1:
  #   print(f'You rolled a {roll}! Critical Fail')
  # elif roll == 6:
  #   print(f'You rolled a {roll}! Critical Success!')
  # else:
  #   print(f'You rolled a {roll}')
  # print(f'You have rolled a total of {dice_sum}')

  # dice_rolls = 2
  # dice_sum = 0
  # for i in range(0,dice_rolls):
  #  roll = random.randint(1,6)
  # dice_sum += roll
  # print(f'You rolled a {roll}')
  # print(f'You have rolled a total of {dice_sum}')
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
  main()