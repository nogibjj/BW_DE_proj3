sudo apt-get update
sudo apt install zip unzip
pip install -r requirements.txt

rm -rf ~/.kaggle
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
