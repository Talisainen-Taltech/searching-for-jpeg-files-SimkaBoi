### Name: Siim Ristjõe

### UniID: sirist

Folder random files contains files without extention. Five of them are pictures and the rest does not contain any meaningful information.
Your task is to detect detect picture files by opening them in binary mode and checking their [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures). The first two bytes of JPEG files are `FF 8D`.
The same set of files is located on [TalTech server](https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip).

1. Open files in binary mode using [os module](https://docs.python.org/3/library/os.html), check their signature and either add jpeg extention or delete them
2. Download the files from TalTech server automatically using [requests](https://docs.python-requests.org/en/latest/index.html) module and extract them automatically using [zipfile](https://docs.python.org/3/library/zipfile.html) module.
