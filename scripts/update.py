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


r = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", r.status_code)


if r.status_code != 200:

    raise Exception(
        "Tidak bisa membuka Rule34 Paheal"
    )



# ======================
# PARSE
# ======================

soup = BeautifulSoup(
    r.text,
    "html.parser"
)


images = []



# Paheal menyimpan gambar di tag img

for img in soup.find_all("img"):


    src = img.get("src")


    if src:


        if "images" in src or "rule34" in src:


            if src.startswith("//"):

                src = "https:" + src


            images.append(src)



# hapus duplikat

images = list(dict.fromkeys(images))



print(
    "Jumlah gambar:",
    len(images)
)



# ======================
# README
# ======================

readme = f"""

# 🎨 Rule34 Gallery


Tag:

`{TAG}`


<div align="center">

"""



for img in images:


    readme += f"""

<img src="{img}" width="200">

"""



readme += """

</div>

"""



with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(readme)



print(
    "README selesai"
)
