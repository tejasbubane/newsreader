echo "Instaling newsreader...\n\n"
sudo apt-get install espeak mbrola mbrola-en1
wget https://github.com/parente/pyttsx/archive/master.zip
unzip master.zip
sudo python pyttsx/master/setup.py install
echo"\n\nNewsreader is installed.\nPlease run read_news.py each time you need to listen to news\n"
