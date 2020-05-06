mkdir testing
python3 simogit.py
cp all.py testing/.
mv Repos/ testing/.
cd testing/
cp Repos/* .
clear
python3 all.py