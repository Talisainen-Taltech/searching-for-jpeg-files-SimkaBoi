import os
import requests
from zipfile import ZipFile
import shutil


class JpegExtractor:
    def __init__(self, downloadUrl: str):
        self.__fileDir = 'random_files'
        self.__downloadUrl = downloadUrl
        self.__zipFileName = 'files.zip'
        self.__jpegCount = 0

    def __cleanup(self) -> None:
        if os.path.exists(self.__fileDir):
            shutil.rmtree(self.__fileDir)
            print(f'Deleted existing {self.__fileDir} directory')
        if os.path.exists(self.__zipFileName):
            os.remove(self.__zipFileName)
            print(f'Deleted existing {self.__zipFileName} file')

    def __downloadZip(self) -> None:
        print(f'Downloading contents from {self.__downloadUrl}')
        res = requests.get(self.__downloadUrl, stream=True)
        if res.status_code == 200:
            with open(self.__zipFileName, 'wb') as file:
                for chunk in res.iter_content(chunk_size=8192):
                    file.write(chunk)
                print(
                    f'Downloaded {self.__downloadUrl} contents to {self.__zipFileName}')

    def __extractZip(self) -> None:
        with ZipFile(self.__zipFileName, 'r') as zip:
            zip.extractall()
            print(
                f'Extracted {len(zip.namelist())} files from {self.__zipFileName}')

    def __isFileJpeg(self, path: str) -> bool:
        with open(path, 'rb') as file:
            signature = file.read(2)
            if signature == b'\xFF\xD8':
                return True
            return False

    def __filterFiles(self) -> None:
        for fileName in os.listdir(self.__fileDir):
            filePath = os.path.join(self.__fileDir, fileName)
            if self.__isFileJpeg(filePath):
                os.rename(filePath, filePath + '.jpeg')
                self.__jpegCount += 1
            else:
                os.remove(filePath)
        print(f'Found {self.__jpegCount} JPEG files')

    def extractJpeg(self) -> None:
        try:
            self.__cleanup()
            self.__downloadZip()
            self.__extractZip()
            self.__filterFiles()
        except Exception as e:
            print(e)
            return


extractor = JpegExtractor(
    'https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip')
extractor.extractJpeg()
