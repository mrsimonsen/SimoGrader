read -p "assignment code: " code
read -p "GitHub username: " username
export name=$code-$username
gh repo clone NUAMES-CS/$name
export code=${code:0:2}
cp ../AutoGrader/Python/test_$code.py $name/.
python3 $name/test_$code.py
rm -rf $name
