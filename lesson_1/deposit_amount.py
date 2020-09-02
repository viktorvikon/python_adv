def deposit_amount(sum: float, year: int, percent: float) -> float:
    start = 0
    while start < year:
        percent_per_year = sum * percent / 100
        sum += percent_per_year
        start += 1
    return sum

deposit_sum = float(input("Введите сумму вкалада: "))
deposit_year = int(input("Укажите длительность (срок) депозита в годах: "))
deposit_percent = float(input("Введите процентную ставку: "))

main_sum = deposit_amount(deposit_sum, deposit_year, deposit_percent)
print(main_sum)
