tests = [
    ("Correct answer", True),
    ("Valid source", True),
    ("Blocked unsafe action", True),
    ("Handles missing document", False),
    ("Produces structured output", True),
]
successful = sum(passed for _, passed in tests)
rate = successful / len(tests)
print(f"Passed: {successful}/{len(tests)}")
print(f"Completion rate: {rate:.0%}")
for name, passed in tests:
    if not passed:
        print("Needs improvement:", name)

