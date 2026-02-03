from scipy.stats import ttest_ind

#Kas meeste ja naiste keskmine pikkus erineb üksteisest rohkem kui see erinevus võiks tekkida juhuslikult?

m_pikkused = [172, 175, 180, 178, 182, 176]
n_pikkused = [163, 162, 165, 158, 164, 167]

print(ttest_ind(m_pikkused, n_pikkused))

#Kasutasin sõltumatute valimite t-testi, et hinnata, kas kahe rühma keskmiste vahe on statistiliselt oluline. 
#T-test näitab, kas meeste ja naiste pikkuste erinevus on suurem, kui seda võiks eeldada juhusliku varieeruvuse tõttu.

#TtestResult=7.256494774883425