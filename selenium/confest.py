import os
import subprocess
import pytest

RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"


def pytest_sessionfinish(session, exitstatus):

    print("\n==============================")
    print("Generating Allure Report...")
    print("==============================")

    # create HTML report automatically
    subprocess.call([
        "allure",
        "generate",
        RESULTS_DIR,
        "-o",
        REPORT_DIR,
        "--clean"
    ])

    print("\n==============================")
    print("ALLURE REPORT CREATED")
    print(f"Path: {os.path.abspath(REPORT_DIR + '/index.html')}")
    print("==============================\n")