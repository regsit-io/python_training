tel = input('Podaj swój numer telefonu: ')
telr = tel.replace('-','').replace(' ', '')
privd = (len(telr) - 6) * 'X'
print(f'Twój numer telefonu to: {telr[:6]}{privd}')