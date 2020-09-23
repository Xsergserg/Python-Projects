def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    saves = 0
    currentOld = startPriceOld
    currentNew = startPriceNew
    perc = percentLossByMonth
    i = 0
    while (round(saves + currentOld - currentNew) < 0):
        i += 1
        if (i % 2 == 0):
            perc += 0.5
        saves += savingperMonth
        currentOld -= currentOld * perc / 100
        currentNew -= currentNew * perc / 100
        #print('end month ' + str(i) + ': percent: ' + str(perc) + ' available: ' + str(saves + currentOld - currentNew))
    return [i, round(saves + currentOld - currentNew)]

print (nbMonths(2000, 8000, 1000, 1.5))
