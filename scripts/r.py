import requests
from bs4 import BeautifulSoup


# ======================
# SETTINGS
# ======================

TAG = "Roswell_SS"

PAGE = 1

URL = f"https://rule34.paheal.net/post/list/{TAG}/{PAGE}"



headers = {
    "User-Agent": "Mozilla/5.0"
}



# ======================
# GET PAGE
# ======================

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)


if response.status_code != 200:

    raise Exception(
        f"Error {response.status_code}"
    )



soup = BeautifulSoup(
    response.text,
    "html.parser"
)



# ======================
# FIND IMAGES
# ======================

images = []


for img in soup.find_all("img"):

    src = img.get("src")


    if src and "preview" in src:

        if src.startswith("//"):

            src = "https:" + src


        images.append(src)



print(
    "Images found:",
    len(images)
)



# ======================
# CREATE README
# ======================


readme = f"""

# 🎨 Paheal Gallery

Tag:

`{TAG}`


Automatically updated.


"""


for img in images:


    readme += f"""

<img src="{img}" width="250">


"""



with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(readme)



print("README generated")
