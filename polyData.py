
salaries = [100,200,300,400]

[salary * 2 for salary in salaries]


[salary * 2 for salary in salaries if salary < 400]


[salary * 2 if  400 <= salary else salary * 0 for salary in salaries ]

[(salary * 2) if  400 <= salary else salary * 0 for salary in salaries ]


ulkeler = ["türkiye","rusya","afganistan","abd","çin","bangladeş"]
guclu_ulkeler = ["türkiye","afganistan","bangladeş"]


[ulke.upper() if ulke in guclu_ulkeler else ulke.lower() for ulke in ulkeler ]





numbers()
