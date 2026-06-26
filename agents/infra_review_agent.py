import os

FILES = [
    "infra/cloudformation/network.yaml"
]

score = 10
issues = []

for file in FILES:
    if not os.path.exists(file):
        score -= 2
        issues.append(f"Missing file: {file}")

print("Infra Review Agent")
print("==================")
print(f"Infrastructure Score: {score}/10")

if issues:
    print("\nIssues:")
    for issue in issues:
        print("-", issue)
else:
    print("No infra issues found.")