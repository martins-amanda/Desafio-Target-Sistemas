data = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(data.values())
percentages = {state: (revenue / total) * 100 for state, revenue in data.items()}
print("Faturamento mensal por estado:")
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")
