import os
import kaggle

def download() -> None:
    dataset = 'abecklas/fifa-world-cup'
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset, path="./data/", unzip=True)

if __name__ == '__main__':
    #if file does not exist, download it
    if not os.path.isdir('./data/'):
        print("downloading...")
        download()
        print("downloaded")
        