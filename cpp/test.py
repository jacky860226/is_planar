import glob
import time
import subprocess

input_files = sorted(glob.glob('data/*/*.in'), key=lambda x: int(x.split('/')[-1].split('.')[0]))

for input_file in input_files:
    i = input_file.split('.')[0]
    output_file = f'{i}.ans'

    with open(input_file, 'r') as f:
        input_data = f.read()

    start_time = time.time()

    if True:
        commandList = ['./main']
    else:
        commandList = ['python', 'main.py']
    process = subprocess.Popen(commandList, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    end_time = time.time()

    execution_time = end_time - start_time

    with open(output_file, 'r') as f:
        expected_output = f.read()

    if stdout == expected_output:
        print(f'Test case {i}: Passed (Execution time: {execution_time:.4f} seconds)')
    else:
        print(f'\033[91mTest case {i}: Failed (Execution time: {execution_time:.4f} seconds)\033[0m')