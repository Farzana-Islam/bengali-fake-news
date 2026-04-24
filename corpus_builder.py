# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 10:36:01 2019
Creates Data Set as files from CSV
@author: Farzana Islam
Reads from csv, writes the title and body texts in separate files
"""
import csv
import os

os.makedirs('./output/fake', exist_ok=True)
os.makedirs('./output/real', exist_ok=True)

with open('./data/dataset_fake.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            out_file = open(f'./output/fake/{row[0]}.txt', 'w', encoding='utf-8')
            out_file.write(row[1] + '\n' + row[2])
            line_count += 1
    print(f'total {line_count}.')

with open('./data/dataset_real.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            out_file = open(f'./output/real/{row[0]}.txt', 'w', encoding='utf-8')
            out_file.write(row[1] + '\n' + row[2])
            line_count += 1
    print(f'total {line_count}.')
