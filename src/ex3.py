import json

with open("dados.json", "r") as file:
    data = json.load(file)

daily_revenues = [d["valor"] for d in data if d["valor"] > 0]
min_revenue = min(daily_revenues)
max_revenue = max(daily_revenues)
average_revenue = sum(daily_revenues) / len(daily_revenues)
days_above_average = sum(1 for dias in daily_revenues if dias > average_revenue)

print(f"Menor faturamento: R$ {min_revenue:.2f}")
print(f"Maior faturamento: R$ {max_revenue:.2f}")
print(f"Média de faturamento: R$ {average_revenue:.2f}")
print(f"Dias com faturamento acima da média: {days_above_average}")
