cities=["Kashmore","Lahore","Peshawar","Quetta","GIT"]
Province=["Sindh","Punjab","KPK","Balochistan","Gilgit"]
z=zip(cities,Province)
d={province:cities for cities , province in zip(cities,Province)}
print(d)