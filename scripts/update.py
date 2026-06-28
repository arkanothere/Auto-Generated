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

    "User-Agent":
    "Mozilla/5.0 github-actions-gallery"

}



response = requests.get(

    URL,

    headers=headers,

    timeout=30

)



if response.status_code != 200:

    raise Exception(
        f"Failed {response.status_code}"
    )



# ======================
# PARSE HTML
# ======================


soup = BeautifulSoup(

    response.text,

    "html.parser"

)



images = []



for img in soup.find_all("img"):


    src = img.get("src")


    if src and "sample" in src:


        if src.startswith("//"):

            src = "https:" + src


        images.append(src)



# ======================
# README
# ======================


readme = f"""

# 🎨 Rule34 Gallery


Tag:

`{TAG}`



Automatically updated.



<div align="center">


"""



for image in images:


    readme += f"""


<img src="{image}" width="200">


"""



readme += """

</div>

"""



with open(

    "README.md",

    "w",

    encoding="utf-8"

) as file:


    file.write(readme)



print(

    f"Updated {len(images)} images"

)
