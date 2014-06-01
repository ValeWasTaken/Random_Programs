# Oreo experiment
# How many oreos, laid side to side in a straight line, will fit in 1 light year?
# If it takes me 2.35 seconds to place each oreo, how many days will it take me to place them all?

def main():
    lightyear = 372469718092929000 # 1 light-year in inches
    oreoDiameter = 1.78            # 1 oreo cookie in diameter (average)

    oreos = ( lightyear / oreoDiameter)
    print("The amount of oreos would be: %.20g" % oreos)

    timePlacing = ((((oreos / 2.35) / 60) / 60) / 24) # days
    print("The amount of days placing oreos would be: %.20g" % timePlacing)
main()
