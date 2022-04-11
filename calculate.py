# E-juice nicotine mixing calculator
import math

def calculate():

    amount = int(input('Bottle size in (ml): '))
    current = int(input('Current nicotine concentration of E-liquid (mg/ml): '))
    nic_base = int(input('Nicotine base strength (mg/ml): '))
    target = int(input('Desired nicotine strength (mg/ml): '))


    # Calculate what the new target should be from user input if current is > 0mg
    target_converted = target - current

    # Run calculation based on 0mg ejuice
    if current == 0:
      print(' ({}ml bottle) / ({}mg/ml nicotine strength) x ({}mg/ml nicotine target strength) = '\
        .format(amount, nic_base, target))
      no_base = round(amount / nic_base * target, 2)
      print(no_base,'ml')
    # Run calculation based on  > 0mg ejuice
    else:
      print('You entered a current nicotine level of {}mg and target of {}mg, gap in \'mg\' is {}mg ' \
        .format(current, target, target_converted))
      print(' ({}ml bottle) / ({}mg/ml nicotine strength) x ({}mg/ml nicotine target strength) = '\
        .format(amount, nic_base, target_converted))
      with_base = round(amount / nic_base * target_converted, 2)
      print(with_base,'ml')

if __name__ == '__main__':
    calculate()
#       print(amount / nic_base * target,'ml')