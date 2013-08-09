echo "Installing newsreader....\n\n"
sudo apt-get install espeak mbrola mbrola-en1 python-pip
pip install git+https://github.com/parente/pyttsx/
echo "\n\nNewsreader is installed.\nPlease run read_news.py each time you need to listen to news\n"
