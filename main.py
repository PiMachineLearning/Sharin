import os, shutil, re, hashlib, atexit


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()

open("lock", 'a').close()
atexit.register(os.remove("lock")) # potential issues if two instances of Sharin run at the same time

if os.path.exists("./dist"):
    shutil.rmtree("./dist")

os.makedirs("./dist/simple/", exist_ok=True)

index = "<!DOCTYPE html><html><body>"

for dir in os.listdir("wheels"):
    if not re.match("^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$", dir, re.IGNORECASE):
        print(f"warning: {dir} is not a compliant name, ignoring")
        continue

    dir = normalize(dir)
    shutil.copytree(f"wheels/{dir}", f"dist/simple/{dir}")
    index += f'<a href="{dir}/">{dir}</a>\n'

    page = f"<!DOCTYPE html><html><head><title>Links for {dir}</title></head><body><h1>Links for {dir}</h1>"

    for file in os.listdir(f"wheels/{dir}"):
        crypt_hash = hashlib.sha256()
        with open(f"wheels/{dir}/{file}", "rb") as f:
            while f.peek(1) != b"":
                crypt_hash.update(f.read(16384))
        crypt_hash = crypt_hash.hexdigest()
        page += f'<a href="{file}#sha256={crypt_hash}">{file}</a><br>'
    page += "</body></html>"
    with open(f"dist/simple/{dir}/index.html", "w") as f:
        f.write(page)

index += "</body></html>"

with open("dist/simple/index.html", "w") as f:
    f.write(index)
