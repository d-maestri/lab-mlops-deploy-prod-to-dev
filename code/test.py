# ======================
# STEPS TO DO IN TERMINAL
# =======================
# 1- Create a new environment
# python -m venv venv
#
# 2 - Git ignore venv folder
# echo "venv" > .gitignore
#

import pandas as pd

print("Hello World!")
print("The world needs pandas!")

housingdat = pd.read_csv('../data/king_county_houses_aa.csv')

housingdat.head()