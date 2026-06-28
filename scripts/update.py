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
# GET LIST POST
# ======================

r = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", r.status_code)



soup = BeautifulSoup(
    r.text,
    "html.parser"
)



post_links = []



for a in soup.find_all("a"):

    href = a.get("href")


    if href and "/post/view/" in href:


        if href.startswith("/"):

            href = BASE + href


        post_links.append(href)



post_links = list(dict.fromkeys(post_links))



print(
    "Post ditemukan:",
    len(post_links)
)



# ======================
# AMBIL GAMBAR ASLI
# ======================

images = []



for link in post_links:


    page = requests.get(
        link,
        headers=headers,
        timeout=30
    )


    detail = BeautifulSoup(
        page.text,
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
    "Gambar asli:",
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

<img src="{img}" width="220">

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



print(
    "README updated"
)
