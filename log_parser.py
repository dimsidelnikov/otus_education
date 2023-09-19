import argparse
import os
import re
import json
import datetime
from collections import defaultdict
from operator import itemgetter


parser = argparse.ArgumentParser(description='Parser log files')

parser.add_argument('--path', action='store', help='Path to log files', required=True)
args = parser.parse_args()

if os.path.isfile(args.path):
    log_files = [args.path]
elif os.path.isdir(args.path):
    log_files = []
    for file in os.listdir(args.path):
        file_path = os.path.join(args.path, file)
        if file.endswith('.log') and os.path.isfile(file_path):
            log_files.append(file_path)
else:
    raise ValueError(f"'{args.path}' is not a file or directory")

results = []
method_req_count = defaultdict(int)
ip_req_count = defaultdict(int)
all_requests = []

for log_file in log_files:
    with open(log_file, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        total_req_count = len(lines)
        for line in lines:
            method = re.search(r'\b(GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)\b', line)[0]
            method_req_count[method] += 1

            url = line.split()[10][1:-1]

            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)[0]
            ip_req_count[ip] += 1

            time = int(line.split()[-1])
            date = re.search(r'\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}', line)[0]

            request = {'method': method, 'url': url, 'ip': ip, 'time': time, 'date': date}
            all_requests.append(request)

        sorted_ip_req_count = sorted(ip_req_count.items(), key=lambda x: x[1], reverse=True)
        top_three_ip = dict(sorted_ip_req_count[0:3])

        sorted_all_req_by_time = sorted(all_requests, key=itemgetter('time'), reverse=True)
        top_slowest_req = sorted_all_req_by_time[0:3]

        result = {
            'Log file': file.name.split('/')[-1],
            'Total count requests': total_req_count,
            'Count of requests by HTTP methods': method_req_count,
            'Top 3 IP addresses from which requests were made': top_three_ip,
            'Top 3 slowest requests': top_slowest_req
        }

        results.append(result)

print(json.dumps(results, indent=4))

current_date = datetime.datetime.now().strftime('%d-%m-%y-%H:%M')
with open(f'{current_date}_log_parse.json', 'w', encoding='UTF-8') as file:
    json.dump(results, file, indent=4)
