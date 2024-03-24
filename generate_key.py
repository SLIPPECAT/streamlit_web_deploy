import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["류준영", "김호연"]
usernmaes = ["vnueryu", "vnuekim"]
paswords = ["vnueryu", "vnuekim"]

## stauth.Hasher는 Bcrypt 알고리즘 사용
hashed_passwords = stauth.Hasher(paswords).generate()

file_path = Path(__file__).parent  / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

