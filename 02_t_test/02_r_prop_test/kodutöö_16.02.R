#Esimeses külas on 120st inimesest 21 vasakukäelised
#Teises külas on 110st inimesest 8 vasakukäelissed

print(prop.test(c(21, 8), c(120, 110)))

#data:  c(21, 8) out of c(120, 110) - andmestik

#X-squared = 4.5593 - näitab kui suur erinevus on kahe mõõdiku vahel, 4.6 viitab, et pigem suur

#df = 1

#p-value = 0.03274 - 0.0327 on väiksem kui 0.05, seega kogukondade vahel on statistiliselt oluline erinevus

#alternative hypothesis: two.sided - testin kas nad on erinevad?

#95 percent confidence interval: 0.01003307 0.19451239 - erinevus kogukondade vahel on vahemikus 1-19%

#sample estimates:
#   prop 1     prop 2 
#0.17500000 0.07272727 - esimeses grupis 17.5% vasakukäelisi teises grupis 7.3%.


#vastus: esimeses kogukonnas on vasakukäelisi oluliselt rohkem kui teises kogukonnas.






#p-value: Kui tegelikult oleks mõlemas kogukonnas sama vasakukäelisuse osakaal
#siis nii suure erinevuse nägemise tõenäosus oleks umbes 3.3%.
