import os
import urllib.request as request
from zipfile import ZipFile
from DeepClassifier.entity import DataIngestionConfig
from DeepClassifier import logger
from DeepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file ...")
        # file present or not
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading file ")
            # help to download from url
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following information :\n{headers}")
        else:
            logger.info(f"File Already paresent of size: {get_size(Path(self.config.local_data_file))}")

    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        # file present or not
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        # if img size is zero remove it
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"Removing file:{target_filepath} with size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info("Unzipping file and remove unwanted file")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)