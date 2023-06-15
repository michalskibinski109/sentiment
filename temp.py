import argostranslate.package
import argostranslate.translate


argostranslate.package.update_package_index()
packages = argostranslate.package.get_available_packages()
for package in packages:
    # do not en -> *
    if str(package).startswith('En'):
        print(f'Skipping package: {package}')
        continue
    print(f'downloading package: {package}')
    download_package = package.download()
    print(f'installing package: {package}')
    argostranslate.package.install_from_path(download_package)
