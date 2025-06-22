# test_imports.py

modules = [
    'numpy', 'pandas', 'matplotlib', 'seaborn',
    'sklearn', 'scipy', 'jupyter'
]

for module in modules:
    try:
        __import__(module)
        print(f"[✓] {module} importé avec succès")
    except ImportError:
        print(f"[X] Le module '{module}' est manquant")
