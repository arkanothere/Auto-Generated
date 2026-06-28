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
# OPEN TAG PAGE
# ======================

r = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", r.status_code)


if r.status_code != 200:
    raise Exception("Gagal membuka halaman")



soup = BeautifulSoup(
    r.text,
    "html.parser"
)



# ======================
# ONLY POST THUMBNAILS
# ======================

post_links = []



# ambil hanya thumbnail area

for thumb in soup.select(".shm-thumb a"):


    href = thumb.get("href")


    if href:


        if href.startswith("/"):

            href = BASE + href


        post_links.append(href)



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


    try:


        page = requests.get(
            link,
            headers=headers,
            timeout=20
        )


        detail = BeautifulSoup(
            page.text,
            "html.parser"
        )



        img = detail.select_one(
            "#main_image"
        )



        if img:


            src = img.get("src")


            if src.startswith("//"):

                src = "https:" + src


            images.append(src)



    except:

        pass



print(
    "Gambar asli:",
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
