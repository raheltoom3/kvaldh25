print(prop.test(20, 120))
print(prop.test(20, 120, p=0.2))
print(prop.test(165, 170)) #ei toimi


#Norral seitse kuldmedalit, kokku 37 kuldmedalit

print(prop.test(7, 37))

#data:  7 out of 37, null probability 0.5 - Ehk testid, kas Norra sai 50% kõigist kuldmedalitest.
#X-squared = 13.081 - Mida suurem see number, seda rohkem erineb sinu tulemus nullhüpoteesist.
#df = 1 - Proportsioonitestis on see 1.
#p-value = 0.0002983 - Kui tegelikult oleks Norra osakaal 50%, siis nii äärmusliku tulemuse (või veel äärmuslikuma) saamise tõenäosus on 0.03%.
#alternative hypothesis: true p is not equal to 0.5 - Testid, kas p ≠ 0.5 (mitte lihtsalt väiksem või suurem).
#95 percent confidence interval: - Meie hinnangul on Norra tegelik osakaal kuskil 8.6% ja 35.7% vahel.
#0.08555159 0.35708984
#sample estimates:# 0,189 - Ehk Norra sai umbes 18,9% kuldmedalitest.

norra=7
kokku=37
vahemik=prop.test(norra, kokku)$conf.interval
print(vahemik)
print(vahemik*kokku)


#isamaa valijad
print(prop.test(266, 1000))
#95 percent confidence interval: 0.2390650 0.2947586 - 23-29% valisid Isamaa

#reform ja sotsid
print(prop.test(147, 1000))
print(prop.test(139, 1000))

print(prop.test(c(147, 139), c(1000, 1000), conf.level=0.90)) #conf.level=0.9 - 90%list tõenäosust tahan

#p-value = 0.6548 - tõenäosus, et neil on sama reiting

print(prop.test(644, 1586))
print(prop.test(13, 1586))
print(prop.test(c(644, 13), c(1586, 1342)))

#X-squared = 653.93 → väga suur χ² väärtus, mis tähendab, et erinevus on suur.
#p-value < 2.2e-16 → peaaegu null, seega nullhüpoteesi p₁ = p₂ saab julgelt tagasi lükata.
#95% usaldusvahemik (0.371 – 0.422) → erinevus naiste ja meeste proportsioonis (“a”-ga lõppevad nimed) on kuskil 37–42%.
#Proportsioonid: Naised: 0.406 (~41%) Mehed: 0.0097 (~1%)
#Kokkuvõte: naiste nimed lõppevad “a”-ga oluliselt sagedamini kui meeste nimed.