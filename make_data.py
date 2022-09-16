def clean():
	print("Gathering Repos...")
	os.system("gh repo list nuames-cs --json name -L 4444 > temp.json")
	old = []
	d = shelve.open('data.dat')
	tags = d['assignments']
	d.close()
	with open("temp.json") as file:
		repos = json.load(file)
	os.system("rm temp.json")
	print("Filtering Results...")
	for r in repos:
		if r["name"][:3] in tags and r["name"][-3:] != '.py':
			old.append(r['name'])
			print(f"{r['name']} added")
	total = len(old)
	print(f"{total} repos collected")
	if input("Delete?\n").lower() in ('yes','y'):
		c = 0
		print("checking authentication")
		os.system("gh auth refresh -h github.com -s delete_repo")
		for i in old:
			print(f"deleting nuames-cs/{i} ({c}/{total})")
			os.system(f"gh repo delete nuames-cs/{i} --confirm")
	print("Done.")
