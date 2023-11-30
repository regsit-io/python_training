expenditures = {
    'jedzenie': float(input('Ile miesięcznie wydajesz na jezenie: ')),
    'rozrywka': float(input('Ile miesięcznie wydajesz na rozrywkę ')),
    'opłaty': float(input('Ile miesięcznie wydajesz na opłaty: ')),
    'inne': float(input('Ile miesięcznie masz innych wydatków: '))
}

expenditures_sum = expenditures['jedzenie'] + expenditures['rozrywka'] + expenditures['opłaty'] + expenditures['inne']
expenditures['jedzenie'] = expenditures['jedzenie']/expenditures_sum * 100
expenditures['rozrywka'] = expenditures['rozrywka']/expenditures_sum * 100
expenditures['opłaty'] = expenditures['opłaty']/expenditures_sum * 100
expenditures['inne'] = expenditures['inne']/expenditures_sum * 100

print(expenditures[input('[jedzenie, rozrywka, opłaty, inne] Podaj jaki wydatek procentowy chcesz obliczyć: ').lower().replace(' ', '')])