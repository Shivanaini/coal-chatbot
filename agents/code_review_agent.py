import subprocess


def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout + result.stderr


def review_code():
    print("=" * 50)
    print("CODE REVIEW AGENT STARTED")
    print("=" * 50)

    print("\nRunning Flake8...")
    flake8_output = run_command("flake8 backend agents")

    print("\nRunning Pylint...")
    pylint_output = run_command(
        "pylint backend agents --disable=C0114,C0115,C0116"
    )

    print("\nReview Report")
    print("-" * 50)

    if flake8_output.strip():
        print("\nFlake8 Issues:")
        print(flake8_output)
    else:
        print("No Flake8 issues found.")

    if pylint_output.strip():
        print("\nPylint Report:")
        print(pylint_output)
    else:
        print("No Pylint issues found.")

    print("=" * 50)
    print("CODE REVIEW AGENT COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    review_code()