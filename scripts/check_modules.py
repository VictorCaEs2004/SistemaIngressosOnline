import importlib

for pkg in ["docx", "markdown"]:
    spec = importlib.util.find_spec(pkg)
    print(f"{pkg} ok" if spec else f"{pkg} missing")
