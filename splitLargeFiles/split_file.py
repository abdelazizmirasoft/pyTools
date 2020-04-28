import io
lines_per_file = 250001
smallfile = None
with io.open('liste_non_covid_pp.data', encoding="utf-8") as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = io.open(small_filename, "w", encoding="utf-8")
        smallfile.write(line)
    if smallfile:
        smallfile.close()

    
