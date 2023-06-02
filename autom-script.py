import calendar
from pathlib import Path

meses_ano =list(calendar.month_name[1:])
dia_semana = ['dia 1', 'Dia 10', 'Dia 21', 'Dia 30']

for i, mes in enumerate(meses_ano):
    for dia in dia_semana:
        Path(f'2023/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)
