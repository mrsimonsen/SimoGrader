python3 simogit.py
cd Repos
python3 grader.py 12
cp -r testing ../testing
cd ..
rm -rf Repos
cp all.py testing/all.py
cd testing
cp ../Java/data_maker.py data_maker.py
cp ../Java/SystemCommands.py SystemCommands.py
cp "../Java/username - Form Responses 1.csv" "username - Form Responses 1.csv"
python3 all.py