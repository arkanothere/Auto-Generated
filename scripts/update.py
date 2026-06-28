import requests
from bs4 import BeautifulSoup


# ======================
# SETTINGS
# ======================

TAG = "Roswell_SS"

PAGE = 1

URL = f"https://rule34.paheal.net/post/list/{TAG}/{PAGE}"


# ======================
# REQUEST
# ======================

headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", response.status_code)


if response.status_code != 200:

    raise Exception(
        "Website tidak bisa diakses"
    )



# ======================
# PARSE
# ======================

soup = BeautifulSoup(
    response.text,
    "html.parser"
)


images = []



# ambil semua link gambar

for a in soup.find_all("a"):


    href = a.get("href")


    if href:


        if href.endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):


            if href.startswith("//"):

                href = "https:" + href


            images.append(href)



# ======================
# DEBUG
# ======================


print(
    "Jumlah gambar:",
    len(images)
)



# ======================
# README
# ======================


content = f"""

# 🎨 Rule34 Gallery


Tag:

`{TAG}`


<div align="center">

"""


for img in images:


    content += f"""

<img src="{img}" width="200">


"""



content += """

</div>

"""



with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:


    f.write(content)



print("README updated")
