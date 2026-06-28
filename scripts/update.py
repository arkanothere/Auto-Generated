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
# GET PAGE
# ======================

response = requests.get(
    URL,
    headers=headers,
    timeout=30
)


print("Status:", response.status_code)



if response.status_code != 200:
    raise Exception("Halaman gagal dibuka")



soup = BeautifulSoup(
    response.text,
    "html.parser"
)



# ======================
# ONLY POST LINKS
# ======================

post_links = []


for a in soup.find_all("a"):


    href = a.get("href")


    if not href:
        continue



    # hanya post halaman
    if "/post/view/" in href:


        if href.startswith("/"):

            href = BASE + href


        post_links.append(href)



# hapus duplikat

post_links = list(
    dict.fromkeys(post_links)
)



print(
    "Post ditemukan:",
    len(post_links)
)



# ======================
# GET IMAGE
# ======================

images = []


for link in post_links:


    try:

        r = requests.get(
            link,
            headers=headers,
            timeout=20
        )


        page = BeautifulSoup(
            r.text,
            "html.parser"
        )



        # ambil gambar utama
        img = page.find(
            "img",
            id="main_image"
        )



        if img:


            src = img.get("src")


            if src:


                if src.startswith("//"):

                    src = "https:" + src


                images.append(src)



    except Exception as e:

        print(
            "Skip:",
            link
        )



print(
    "Gambar ditemukan:",
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
