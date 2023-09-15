import subprocess
import datetime
from collections import defaultdict


def print_process_info(info):
    print(info)

    current_date = datetime.datetime.now().strftime('%d-%m-%y-%H:%M')

    with open(f'{current_date}-scan.txt', 'a') as file:
        file.write(f'{info}\n')


def convert_to_mb(val):
    return round((val / 1024), 2)


output = subprocess.run(['ps', 'aux'], capture_output=True)
lines = output.stdout.decode().splitlines()

num_process = (len(lines)-1)
num_users_process = defaultdict(int)
vsz = 0
cpu = 0
max_vsz = 0
max_cpu = 0
process_max_vsz = ''
process_max_cpu = ''

for line in lines[1:]:
    parts = line.split()
    num_users_process[parts[0]] += 1
    vsz += int(parts[4])
    cpu += float(parts[2])
    if max_vsz < int(parts[4]):
        process_max_vsz = parts[10]
    if max_cpu < float(parts[2]):
        process_max_cpu = parts[10]

print_process_info('Отчёт о состоянии системы:')
print_process_info(f'Пользователи системы: {", ".join(num_users_process.keys())}')
print_process_info(f'Процессов запущено: {num_process}')
print_process_info('Пользовательских процессов:')
for user, count in num_users_process.items():
    print_process_info(f'{user}: {count}')
print_process_info(f'Всего памяти используется: {convert_to_mb(vsz)} mb')
print_process_info(f'Всего CPU используется: {round(cpu, 1)} %')
print_process_info(f'Больше всего памяти использует: {process_max_vsz[:20]}')
print_process_info(f'Больше всего CPU использует: {process_max_cpu[:20]}')
