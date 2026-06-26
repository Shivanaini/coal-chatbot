import os

FILES = [
    "infra/cloudformation/network.yaml",
    "infra/cloudformation/security.yaml",
    "infra/cloudformation/ecr.yaml",
    "infra/cloudformation/alb.yaml",
    "infra/cloudformation/ecs.yaml",
    "infra/cloudformation/iam.yaml",
    "infra/cloudformation/autoscaling.yaml",
    "infra/cloudformation/monitoring.yaml",
    "infra/cloudformation/alerts.yaml"
]

score = 10
issues = []

for file in FILES:
    if not os.path.exists(file):
        score -= 1
        issues.append(file)

print("Infra Review Agent")
print("==================")
print(f"Infrastructure Score: {score}/10")

if issues:
    print("\nMissing files:")
    for issue in issues:
        print("-", issue)
else:
    print("Infra structure looks good.")