import json

with open("schemes.json", "r") as f:
    schemes = json.load(f)

def check_eligibility(age, income, occupation):

    eligible = []

    for scheme in schemes:

        if scheme.get("occupation") != occupation:
            continue

        if "min_age" in scheme:
            if age < scheme["min_age"]:
                continue

        if "max_age" in scheme:
            if age > scheme["max_age"]:
                continue

        if "max_income" in scheme:
            if income > scheme["max_income"]:
                continue

        eligible.append(scheme["scheme"])

    return eligible