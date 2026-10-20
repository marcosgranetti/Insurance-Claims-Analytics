
import csv
from pathlib import Path

# Localizar a pasta onde está o código Python
pasta_projeto = Path(__file__).resolve().parent

# Encontrar o CSV dentro da pasta Dados
caminho_csv = pasta_projeto / "Dados" / "sinistros_2025.csv"

# Abrir a base de dados
with open(caminho_csv, "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo)
    sinistros = list(leitor)


# 2. Criar variáveis para os indicadores
total_sinistros = len(sinistros)
total_reclamado = 0
total_pago = 0

# 3. Percorrer os registros
for sinistro in sinistros:
    total_reclamado += float(sinistro["valor_reclamado"])
    total_pago += float(sinistro["valor_pago"])

# 4. Calcular o valor médio pago por sinistro
media_pago = total_pago / total_sinistros

# 5. Mostrar os resultados
print("===== INSURANCE CLAIMS ANALYTICS =====")
print("Total de sinistros:", total_sinistros)
print(f"Valor total reclamado: R$ {total_reclamado:,.2f}")
print(f"Valor total pago: R$ {total_pago:,.2f}")
print(f"Valor médio pago por sinistro: R$ {media_pago:,.2f}")


# 6. Análise por tipo de sinistro

quantidade_por_tipo = {}
valor_por_tipo = {}

for sinistro in sinistros:
    tipo = sinistro["tipo_sinistro"]
    valor = float(sinistro["valor_pago"])

    if tipo not in quantidade_por_tipo:
        quantidade_por_tipo[tipo] = 0
        valor_por_tipo[tipo] = 0

    quantidade_por_tipo[tipo] += 1
    valor_por_tipo[tipo] += valor

print("\n===== SINISTROS POR TIPO =====")

for tipo in quantidade_por_tipo:
    print(f"\nTipo: {tipo}")
    print(f"Quantidade: {quantidade_por_tipo[tipo]}")
    print(f"Valor pago: R$ {valor_por_tipo[tipo]:,.2f}")


# 7. Severidade dos sinistros pagos

quantidade_pagos = {}
total_pago_tipo = {}

for sinistro in sinistros:
    if sinistro["status"] == "Pago":
        tipo = sinistro["tipo_sinistro"]
        valor = float(sinistro["valor_pago"])

        if tipo not in quantidade_pagos:
            quantidade_pagos[tipo] = 0
            total_pago_tipo[tipo] = 0

        quantidade_pagos[tipo] += 1
        total_pago_tipo[tipo] += valor

print("\n===== SEVERIDADE POR TIPO =====")

for tipo in quantidade_pagos:
    media = total_pago_tipo[tipo] / quantidade_pagos[tipo]

    print(f"\nTipo: {tipo}")
    print(f"Sinistros pagos: {quantidade_pagos[tipo]}")
    print(f"Custo médio pago: R$ {media:,.2f}")
