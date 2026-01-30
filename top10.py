"""
Návrh modelu ukládání top 10 výsledků. Slovník ve formátu:
{
    '3': { 
        '1': {'name': 'Lukáš',
              'attempts': 7,
              'time': 70.3}
    },
    '4': { 
        '1': {'name': 'Jan',
              'attempts': 8,
              'time': 101.3}
    }
}

"""

top10 = {
    3: {
        1: {'name': 'Lukáš',
              'attempts': 7,
              'time': 70.3},
        2: {'name': 'Jan',
              'attempts': 8,
              'time': 69.3}
    },
    4: {
        1: {'name': 'Jan',
              'attempts': 9,
              'time': 120.3},
        2: {'name': 'Petr',
              'attempts': 13,
              'time': 139.3}
    }
}

