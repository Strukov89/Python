q = 0
q1 = 1
q2 = 2
dil = 0


def timeline():
    f = open("timeline.csv", encoding='utf-8')
    p = []
    for s in f:
        p.append(s.split(";"))
    f.close
    return data(p)


def data(p):
    t = []
    for i in range(len(p)):
        t.append(p[i][q].split("-"))

    ma = 0
    mi = 0
    for i in range(len(t)):
        if ma < int(t[i][q]):
            ma = int(t[i][q])
            a = int(t[i][q1])
            b = int(t[i][q2])
        if mi == 0:
            mi = int(t[i][q])
            c = int(t[i][q1])
            d = int(t[i][q2])
        if mi > int(t[i][q]):
            mi = int(t[i][q])
            c = int(t[i][q1])
            d = int(t[i][q2])

    print('между макс и мин датами прошло:', ma - mi, 'лет', abs(a - c), 'месяцев', abs(b - d) + 30 * abs(a - c),
          'дней')


def people():
    f = open("people.csv", encoding='utf-8')
    c = 0
    t = []
    for s in f:
        t.append(s.split(";"))
        del t[c][dil]
        c = c + 1
    f.close
    print(t)
    return static(t)


def static(t):
    y = [1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020,
         2024, 2028, 2032]
    p = []
    for i in range(len(t)):
        if len(t[i]) < 3:
            if (int(t[i][q1][:4]) in y) and (2021 - int(t[i][q1][:4]) <= 20):
                p.append(t[i][q])
        if len(t[i]) == 3:
            if (int(t[i][q1][:4]) in y) and (int(t[i][q2][:4]) - int(t[i][q1][:4]) <= 20):
                p.append(t[i][q])
    print(p)


timeline()
people()