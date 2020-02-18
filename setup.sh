#chmod +x setup.sh
#./setup.sh
#
# python3 version 3.8.1
# javac version 1.8.0_242
# java version openjdk 1.8.0_242
# g++ version 5.4.0
# hamcrest-core version 1.3
# junit version 4.13

sudo apt update
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
wget -O hamcrest-core-1.3.jar https://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar
wget -O junit-4.13.jar https://search.maven.org/remotecontent?filepath=junit/junit/4.13/junit-4.13.jar
tar -xf Python-3.8.1.tgz
cd Python-3.8.1
./configure --enable-eptimizations
make -j4
sudo make install
cd ..
sudo apt install -y default-jre
sudo apt install -y default-jdk
sudo cp junit-4.13.jar /usr/lib/jvm/default-java/jre/lib/ext/junit-4.13.jar
sudo cp hamcrest-core-1.3.jar /usr/lib/jvm/default-java/jre/lib/ext/hamcrest-core-1.3.jar
sudo rm -rf Python-3.8.1 Python-3.8.1.tgz junit-4.13.jar hamcrest-core-1.3.jar
chmod +x grade.sh
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install PyGithub
sudo python3 -m pip install python-dotenv
mkdir "Testing Files"
mv TF.tar.gz Testing\ Files/TF.tar.gz
cd "Testing Files"
tar -xf TF.tar.gz
cd ..
mv env .env
echo "Restart the terminal to complete setup"