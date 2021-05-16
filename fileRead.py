dataFileDumpLocation = "C:/testfolder/datadump.txt"
with open(dataFileDumpLocation) as fp:
    for line in fp:
        #print(line.split('|')[9])
        print("Program process data from file...")
        filename = line.split('|')[9]
        if(filename):
            with open("C:/testfolder/Country_"+filename+".txt","a+") as countryFile:
                countryFile.write(format(line.strip())+'\n')
        else:
            with open("C:/testfolder/NoCountryData.txt","a+") as NoCountryData:
                NoCountryData.write(format(line.strip())+'\n')

    print("Process Completed !!! Successfully !")