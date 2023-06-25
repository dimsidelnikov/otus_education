import json
import csv
import os.path


def gen_file_path(directory, file):
    file_path = os.path.join(directory, file)
    return file_path


def read_json_file(directory, file):
    with open(gen_file_path(directory, file), 'r') as json_file:
        return json.load(json_file)


def write_json_file(directory, file, content):
    with open(gen_file_path(directory, file), 'w') as json_file:
        json.dump(content, json_file, indent=4)


def read_csv_file(directory, file):
    with open(gen_file_path(directory, file), 'r', encoding='utf-8') as csv_file:
        dict_object = csv.DictReader(csv_file)
        row_list = [row for row in dict_object]

        return row_list


def create_users_list(directory, file):
    input_list = read_json_file(directory, file)
    output_list = [
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }
        for user in input_list
    ]
    return output_list


def create_books_list(directory, file):
    input_list = read_csv_file(directory, file)
    output_list = [
        {
            'title': book['Title'],
            'author': book['Author'],
            'pages': int(book['Pages']),
            'genre': book['Genre']
        }
        for book in input_list
    ]
    return output_list


def distribution_books(users_list, books_list):
    len_users_list = len(users_list)
    len_books_list = len(books_list)
    for num in range(len_books_list):
        users_list[num % len_users_list]['books'].append(books_list[num])

    return users_list


dir_name = 'data'
users_json = 'users.json'
books_csv = "books.csv"
result_file = 'result.json'

users = create_users_list(dir_name, users_json)
books = create_books_list(dir_name, books_csv)
output_content = distribution_books(users, books)
write_json_file(dir_name, result_file, output_content)
