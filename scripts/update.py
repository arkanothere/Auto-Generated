import requests
from bs4 import BeautifulSoup


# ======================
# SETTINGS
# ======================

TAG = "Roswell_SS"

PAGE = 1

BASE = "https://rule34.paheal.net"

URL = f"{BASE}/post/list/{TAG}/{PAGE}"


headers = {
    "User-Agent": "Mozilla/5.0"
}



# ======================
# GET LIST PAGE
# ======================

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", response.status_code)


if response.status_code != 200:
    raise Exception("Gagal membuka halaman")



soup = BeautifulSoup(
    response.text,
    "html.parser"
)



# ======================
# ONLY MAIN POSTS
# ======================

post_area = soup.find(
    id="posts"
)


if not post_area:

    raise Exception(
        "Container post tidak ditemukan"
    )



post_links = []



for a in post_area.find_all("a"):


    href = a.get("href")


    if href and "/post/view/" in href:


        if href.startswith("/"):

            href = BASE + href


        post_links.append(href)



# hapus duplikat

post_links = list(
    dict.fromkeys(post_links)
)



print(
    "Post halaman:",
    len(post_links)
)



# ======================
# GET ORIGINAL IMAGE
# ======================


images = []



for link in post_links:


    r = requests.get(
        link,
        headers=headers,
        timeout=30
    )


    detail = BeautifulSoup(
        r.text,
        "html.parser"
    )


    img = detail.find(
        "img",
        id="main_image"
    )


    if img:


        src = img.get("src")


        if src:


            if src.startswith("//"):

                src = "https:" + src


            images.append(src)



print(
    "Gambar:",
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

<img src="{img}" width="220">

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
