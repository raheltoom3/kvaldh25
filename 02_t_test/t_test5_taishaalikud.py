from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa Ei leia mina iial teal see suure laia ilma peal"

th="aeiouöäõü"
print(lause1.lower())
print([t for t in "koolimajja" if t in th])
print(len([t for t in "koolimajja" if t in th]))

def t_arv(sona):
    return len([t for t in sona if t in th])

print(t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)



th="aeiouöäõü"
print(lause2.lower())

def t_arv(sonad22):
    return len([t for t in sonad22 if t in th])


#kuva ka teise teksti iga sõna täishäälikute arv, kontrolli pisteliselt
arvud2=[t_arv(sonad22) for sonad22 in lause2.lower().split()]
print(arvud2)

#võrdle nende arvude artimeetilisi keskmisi t-testiga
print(ttest_ind(arvud1, arvud2))

#kuva kummagi arvujada aritmeetiline keskmine

def keskmine(m):
    return sum(m)/len(m)

print(keskmine(arvud1), keskmine(arvud2))


#Osakaalud
#osakaal arno tekstis

def t_osa(sona):
    return len([t for t in sona if t in th])/len(sona)

osakaalud1=[t_osa(sona) for sona in lause1.lower().split()]
print(osakaalud1)
print(keskmine(osakaalud1))

#osakaal hümnis
#leidke täishäälikute osakaalud ja nende keskmine hümni tekstis

def t_osa1(sonad22):
    return len([t for t in sonad22 if t in th])/len(sonad22)

osakaalud2=[t_osa1(sonad22) for sonad22 in lause2.lower().split()]
print(osakaalud2)
print(keskmine(osakaalud2))

#võrrelge t-tekstiga kahe teksti sõnade täishäälikute osakaale

print(ttest_ind(osakaalud1, osakaalud2))



#Statsmodels

import statsmodels.stats.api as sms
cm = sms.CompareMeans(sms.DescrStatsW(osakaalud1), sms.DescrStatsW(osakaalud2))
print(cm.tconfint_diff(usevar='unequal'))

#pip install statsmodels

