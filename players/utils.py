from .models import Power
import random

def narration(comb, p1, p2):
    """Function describing each movement"""

    powers = Power.objects.filter(player__username=p1)
    energy_pk = 1
    my_power = None

    #search if my combintion is a power
    for p in powers:
        if p.combination == comb:
            my_power =  p

    cases = {
        "case1": [
            f"{p1} avanza y le da un patadazo al pobre {p2}.",
            f"{p1} avanza y le da una patadazo a {p2}.",
            f"{p1} avanza y le da un patadazo",
            f"{p1} avanza y da una patada",
        ],
        "case2": [
            f"{p1} avanza y le da un puñetazo al pobre {p2}.",
            f"{p1} avanza y le da una puñetazo a {p2}.",
            f"{p1} avanza y le da un puñetazo",
            f"{p1} avanza y da una puñete",
        ],
        "case3": [
            f"{p1} le da un patadazo al pobre {p2}.",
            f"{p1} le da una patadazo a {p2}.",
            f"{p1} le da un patadazo",
            f"{p1} le da un patada",
        ],
        "case4": [
            f"{p1} le da un puñetazo al pobre {p2}.",
            f"{p1} le da un puñete a {p2}.",
            f"{p1} le da un puñetazo",
            f"{p1} le da un puñete",
        ],
        "case5": [
            f"{p1} usa un {my_power.name if my_power else ''}",
            f"{p1} conecta un {my_power.name if my_power else ''}.",
        ]
        
    }

    case1 = [
        'DK','DDK','DDDK','DDDDK','DDDDDK',
        'AK','AAK','AAAK','AAAAK','AAAAAK'
    ]

    case2 = [
        'DP','DDP','DDDP','DDDDP','DDDDDP',
        'AP','AAP','AAAP','AAAAP','AAAAAP'
    ]

    if len(my_power.name if my_power else '') > 1:
        return [
            random.choice(cases["case5"]),
            my_power.energy
        ]
    elif comb in case1:
        return [
            random.choice(cases["case1"]),
            energy_pk
        ]
    elif comb in case2:
        return [
            random.choice(cases["case2"]),
            energy_pk
        ]
    elif comb[-1] == 'K':
        return [
            random.choice(cases["case3"]),
            energy_pk
        ]
    elif comb[-1] == 'P':
        return [
            random.choice(cases["case4"]),
            energy_pk
        ]
    else:
        return [
            f"{p1} se mueve", 
            energy_pk
        ]