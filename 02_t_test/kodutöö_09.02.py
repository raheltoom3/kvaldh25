from scipy.stats import ttest_ind

#Kas meeste ja naiste pikkuste vahe on päriselt olemas või võiks see vahe tekkida lihtsalt juhuslikult?

m_pikkused = [172, 175, 180, 178, 182, 176]
n_pikkused = [163, 162, 165, 158, 164, 167]

print(ttest_ind(m_pikkused, n_pikkused))

#Kasutasin sõltumatute valimite t-testi, et hinnata, kas kahe rühma keskmiste vahe on statistiliselt oluline. 

#TtestResult(statistic=np.float64(7.256494774883425), pvalue=np.float64(2.7375353557920887e-05), df=np.float64(10.0))

#7.26 viitab sellele, kui suur vahe on võrreldes juhuslikkusega - pigem suur

#2.7 kui meeste ja naiste keskmine pikkus oleks tegelikult sama, siis kui suure tõenäosusega need arvud olid juhuslikud - väga ebatõenäoline

#Meeste ja naiste keskmine pikkus erineb statistiliselt olulisel määral.
#See erinevus ei ole juhuslik, vaid väga suure tõenäosusega päriselt olemas.


#Aritmeetline keskmine

def keskmine(m):
    return sum(m) / len(m)

print(keskmine(m_pikkused), keskmine(n_pikkused))

#Statsmodels

import statsmodels.stats.api as sms

cm = sms.CompareMeans(
    sms.DescrStatsW(m_pikkused),
    sms.DescrStatsW(n_pikkused)
)

print(cm.tconfint_diff(usevar='unequal'))


#Selle andmestiku põhjal olen 95% kindel, et mehed on keskmiselt umbes 9,7–18,3 cm pikemad kui naised

#Erinevus on statistiliselt oluline, sest mehed on igal juhul pikemad.

