import csv
my_dict = {}
my_list = [{'name': 'Ирина', 'job_title': 'Руководитель департамента'},
           {'name': 'Константин', 'job_title': 'Маркетолог'},
           {'name': 'Николай', 'job_title': 'Рекрутер'},
           {'name': 'Алена', 'job_title': 'Специалист'},
           {'name': 'Евгений', 'job_title': 'Руководитель департаментаs'}]

with open('my_csv.csv') as my_csv:
    reader = csv.DictReader(my_csv)
    # a = list(reader)
    for row in reader:
        my_dict['name'] = row['Имя']
        my_dict['job_title'] = row['Должность']


keys = ['name', 'job_title']
with open('title_job.csv', 'w') as title_job:
    writer = csv.DictWriter(title_job, fieldnames=keys)
    writer.writeheader()
    writer.writerows(my_list)


# a = [{k: str(v) for k, v in row.items()}
#          for row in csv.DictReader(my_csv, skipinitialspace=True)]
