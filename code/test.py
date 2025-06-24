# ======================
# STEPS TO DO IN TERMINAL
# =======================
# 1- Create a new environment
# python -m venv venv
#
# 2 - Git ignore venv folder
# echo "venv" > .gitignore
#
# 3 - Activate Environment
# Linux: . ./venv/bin/activate
#
# 4 - Install dependencies (if you forked the repo jump to 6)
# python -m pip install pandas
#
# 5 - Freeze dependencies
# python -m pip freeze > requirements.txt
#
# 6 - Install dependencies from requirements.txt
# python -m pip install -r requirements.txt

import pandas as pd

print("Hello World!")
print("The world needs pandas!")

housingdat = pd.read_csv('../data/king_county_houses_aa.csv')

print(housingdat.head())
print("Hello World!")


print("Now that I have direct access, I can just do what I want, harharharhar")

print(housingdat.describe())
