import requests
import xml.etree.ElementTree as ET


# ======================
# SETTINGS
# ======================

TAG = "Roswell_SS"

LIMIT = 100


API = (
    "https://rule34.paheal.net/api/danbooru/"
    f"?page=dapi&s=post&q=index&tags={TAG}&limit={LIMIT}"
)



# ======================
# REQUEST
# ======================

headers = {

    "User-Agent":
    "Mozilla/5.0 github-actions-gallery"

}


response = requests.get(
    API,
    headers=headers,
    timeout=30
)


print("Status:", response.status_code)


if response.status_code != 200:

    raise Exception(
        "API gagal"
    )



# ======================
# XML PARSE
# ======================


root = ET.fromstring(
    response.text
)


images = []



for post in root.findall("post"):


    file_url = post.attrib.get(
        "file_url"
    )


    if file_url:

        images.append(file_url)



print(
    "Jumlah gambar:",
    len(images)
)



# ======================
# CREATE README
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
    "README berhasil dibuat"
)
