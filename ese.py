import os
import numpy as np

directory = '/Users/muhammadshahzebali/Desktop/research papers/datasets/qm9 data'
elements = []
files = sorted(os.listdir(directory))

for file_name in files[:50000]:
    file_path = os.path.join(directory, file_name)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >=2:
                second = lines[1].split()
                if len(second) >= 11:
                    elements.append(float(second[10]))
    except Exception as e:
        print(f"Error {file_name}: {e}")




