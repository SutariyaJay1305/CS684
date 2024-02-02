import os

for i in range(1, 51):
    file_name = f"simple{i}.avl"
    coverage_run_command = f"coverage run --append avl.py {file_name}"
    os.system(coverage_run_command)

coverage_report_command = "coverage report"
os.system(coverage_report_command)
