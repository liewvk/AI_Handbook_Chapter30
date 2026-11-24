checks = {
    "Clear objective": True,
    "Test cases prepared": True,
    "Sensitive data protected": True,
    "Failures documented": False,
    "Human review defined": True,
}
completed = sum(checks.values())
print(f"Readiness: {completed}/{len(checks)} checks")
for name, done in checks.items():
    if not done:
        print("Action required:", name)

