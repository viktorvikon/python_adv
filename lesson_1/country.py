country_capital = {
    'Австрия': "Вена",
    'Азербайджан': "Баку",
    'Албания': "Тирана",
    'Андорра': "Андорра-ла-Велья",
    'Армения': "Ереван",
    'Беларусь': "Минск",
    'Бельгия': "Брюссель",
    'Болгария': "София",
    'Босния и Герцеговина': "Сараево",
    'Ватикан': "Ватикан"
}

list_country = ['Австрия', 'Албания', 'Болгария', 'Ватикан', 'Греция', 'Казахстан']

for k in country_capital:
    if k in list_country:
        print(country_capital[k])
