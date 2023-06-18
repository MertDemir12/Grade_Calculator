db = {}  # For Literature
liste1 = {}  # For Math
liste2 = {}  # For Physics
liste3 = {}  # For Biology
liste4 = {}  # For Chemistry
liste5 = {}  # For History
liste6 = {}  # For Geography
liste7 = {}  # For Philosophy
liste8 = {}  # For English
liste9 = {}  # For German
print("***********************************************************")
print("Grade Calculator")
print("***********************************************************")
h = input("Name And Surname: ")
k = int(input("Which grade are you in: "))
while(True):
    print("Type [N] Or [n] To See Notes!")
    print("Type [YE] Or [ye] To Add Exam Grade!")
    print("Type [SE] Or [se] To Add The Verbal Note!")
    print("Type [O] Or [o] To Calculate Average Grade!")
    print("Type [Q] or [q] Exit!")
    a = input()
    if(a == "N" or a == "n" and k == 9):
        print("Literature: {}\nMath: {}\nPhysics: {}\nBiology: {}\nChemistry: {}\nHistory: {}\nGeography: {}\nEnglish: {}\nGerman: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste6,liste8,liste9))
    elif(a == "N" or a == "n" and k == 10):
        print("Literature: {}\nMath: {}\nPhysics: {}\nBiology: {}\nChemistry: {}\nHistory: {}\nGeography: {}\nPhilosophy: {}\nEnglish: {}\nGerman: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8,liste9))
    elif(a == "N" or a == "n" and k == 11 or k == 12):
        print("Literature: {}\nMath: {}\nPhysics: {}\nBiology: {}\nChemistry: {}\nHistory: {}\nPhilosophy: {}\nEnglish: {}\nGerman: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste7,liste8,liste9))
    elif(a == "YE" or a == "ye"):
        while(True):
            print("Which Course Will You Add?")
            print("Write [E] Or [e] For Literature!")
            print("Write [M] Or [m] For Math!")
            print("Write [F] Or [f] For Physics!")
            print("Write [B] Or [b] For Biology!")
            print("Write [T] Or [t] For History!")
            if(k == 9 or k == 10):
                print("Write [C] Or [c] For Geography!")
            if(k == 10 or k == 11 or k == 12):
                print("Write [FE] Or [fe] For Philosophy!")
            print("Write [İ] Or [i] For English!")
            print("Write [A] Or [a] For German!")
            print("Write [G] And [g] To Go Back!")
            b = input()
            if(b == "E" or b == "e"):  # To Enter Literature Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    db["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    db["Second Exam"] = y
            elif(b == "M" or b == "m"):  # To Enter Mathematics Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste1["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste1["Second Exam"] = y
            elif(b == "F" or b == "f"):  # To Enter Physics Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste2["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste2["Second Exam"] = y
            elif(b == "B" or b == "b"):  # To Enter Biology Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste3["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste3["Second Exam"] = y
            elif(b == "K" or b == "k"):  # To Enter Chemistry Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste4["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste4["Second Exam"] = y
            elif(b == "T" or b == "t"):  # To Enter History Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste5["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste5["Second Exam"] = y
            elif(b == "C" or b == "c"):  # To Enter Geography Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste6["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste6["Second Exam"] = y
            elif(b == "FE" or b == "fe"):  # To Enter Philosophy Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste7["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste7["Second Exam"] = y
            elif(b == "İ" or b == "i"):  # To Enter English Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste8["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste8["Second Exam"] = y
            elif(b == "A" or b == "a"):  # To Enter German Exam Grades
                print("If First Exam, Write [1]!\nIf Second Exam, Write [2]!\n")
                c = input()
                if(c == "1"):
                    x = int(input("How Many Did You Get From The Exam: "))
                    liste9["First Exam"] = x
                elif(c == "2"):
                    y = int(input("How Many Did You Get From The Exam: "))
                    liste9["Second Exam"] = y
            elif(b == "G" or b == "g"):  # For Go Back
                break
    elif (a == "SE" or a == "se"):
        while(True):
            print("Which Course Will You Add?")
            print("Write [E] Or [e] For Literature!")
            print("Write [M] Or [m] For Math!")
            print("Write [F] Or [f] For Physics!")
            print("Write [B] Or [b] For Biology!")
            print("Write [T] Or [t] For History!")
            if (k == 9 or k == 10):
                print("Write [C] Or [c] For Geography!")
            if (k == 10 or k == 11 or k == 12):
                print("Write [FE] Or [fe] For Philosophy!")
            print("Write [İ] Or [i] For English!")
            print("Write [A] Or [a] For German!")
            print("Write [G] And [g] To Go Back!")
            b = input()
            if (b == "E" or b == "e"):  # To Enter Literature Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    db["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    db["Second Verbal"] = y
            elif (b == "M" or b == "m"):  # To Enter Mathematics Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste1["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste1["Second Verbal"] = y
            elif (b == "F" or b == "f"):  # To Enter Physics Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste2["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste2["Second Verbal"] = y
            elif (b == "B" or b == "b"):  # To Enter Biology Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste3["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste3["Second Verbal"] = y
            elif (b == "K" or b == "k"):  # To Enter Chemistry Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste4["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste4["Second Verbal"] = y
            elif (b == "T" or b == "t"):  # To Enter History Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste5["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste5["Second Verbal"] = y
            elif (b == "C" or b == "c"):  # To Enter Geography Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste6["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste6["Second Verbal"] = y
            elif (b == "FE" or b == "fe"):  # To Enter Philosophy Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste7["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste7["Second Verbal"] = y
            elif (b == "İ" or b == "i"):  # To Enter English Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste8["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste8["Second Verbal"] = y
            elif (b == "A" or b == "a"):  # To Enter German Verbal Notes
                print("If First Verbal, Write [1]!\nIf Second Verbal, Write [2]!\n")
                c = input()
                if (c == "1"):
                    x = int(input("How Many Did You Get From The Verbal: "))
                    liste9["First Verbal"] = x
                elif (c == "2"):
                    y = int(input("How Many Did You Get From The Verbal: "))
                    liste9["Second Verbal"] = y
            elif (b == "G" or b == "g"):  # For Go Back
                break
    elif(a == "O" or a == "o" and k == 9):  # To Calculate Grade Point Average
        edebi =  (int(db["First Exam"]) + int(db["Second Exam"]) + int(db["First Verbal"]) + int(db["Second Verbal"])) / 4  # For Literature
        mat = (int(liste1["First Exam"]) + int(liste1["Second Exam"]) + int(liste1["First Verbal"]) + int(liste1["Second Verbal"])) / 4  # For Mathematics
        fizi = (int(liste2["First Exam"]) + int(liste2["Second Exam"]) + int(liste2["First Verbal"]) + int(liste2["Second Verbal"])) / 4  # For Physics
        biyo = (int(liste3["First Exam"]) + int(liste3["Second Exam"]) + int(liste3["First Verbal"]) + int(liste3["Second Verbal"])) / 4  # For Biology
        kim = (int(liste4["First Exam"]) + int(liste4["Second Exam"]) + int(liste4["First Verbal"]) + int(liste4["Second Verbal"])) / 4  # For Chemistry
        tar = (int(liste5["First Exam"]) + int(liste5["Second Exam"]) + int(liste5["First Verbal"]) + int(liste5["Second Verbal"])) / 4  # For History
        cog = (int(liste6["First Exam"]) + int(liste6["Second Exam"]) + int(liste6["First Verbal"]) + int(liste6["Second Verbal"])) / 4  # For Geography
        ing = (int(liste8["First Exam"]) + int(liste8["Second Exam"]) + int(liste8["First Verbal"]) + int(liste8["Second Verbal"])) / 4  # For English
        alm = (int(liste9["First Exam"]) + int(liste9["Second Exam"]) + int(liste9["First Verbal"]) + int(liste9["Second Verbal"])) / 4  # For German
        genel = (edebi + mat + fizi + biyo + kim + tar + cog + ing + alm) / 9  # For Overall Average
        print("Your average:")
        print("Literature: {}. Your Literature Average: {}".format(db, edebi))
        print("Math: {}. Your Math Average: {}".format(liste1, mat))
        print("Physics: {}. Your Physics Average: {}".format(liste2, fizi))
        print("Biology: {}. Your Biology Average: {}".format(liste3, biyo))
        print("Chemistry: {}. Your Chemistry Average: {}".format(liste4, kim))
        print("History: {}. Your History Average: {}".format(liste5, tar))
        print("Geography: {}. Your Geography Average: {}".format(liste6, cog))
        print("English: {}. Your English Average: {}".format(liste8, ing))
        print("German: {}. Your German Average: {}".format(liste9, alm))
        print("Your Overall Average: {}".format(genel))
    elif(a == "O" or a == "o" and k == 10):  # To Calculate Grade Point Average
        edebi = (int(db["First Exam"]) + int(db["Second Exam"]) + int(db["First Verbal"]) + int(db["Second Verbal"])) / 4  # For Literature
        mat = (int(liste1["First Exam"]) + int(liste1["Second Exam"]) + int(liste1["First Verbal"]) + int(liste1["Second Verbal"])) / 4  # For Mathematics
        fizi = (int(liste2["First Exam"]) + int(liste2["Second Exam"]) + int(liste2["First Verbal"]) + int(liste2["Second Verbal"])) / 4  # For Physics
        biyo = (int(liste3["First Exam"]) + int(liste3["Second Exam"]) + int(liste3["First Verbal"]) + int(liste3["Second Verbal"])) / 4  # For Biology
        kim = (int(liste4["First Exam"]) + int(liste4["Second Exam"]) + int(liste4["First Verbal"]) + int(liste4["Second Verbal"])) / 4  # For Chemistry
        tar = (int(liste5["First Exam"]) + int(liste5["Second Exam"]) + int(liste5["First Verbal"]) + int(liste5["Second Verbal"])) / 4  # For History
        cog = (int(liste6["First Exam"]) + int(liste6["Second Exam"]) + int(liste6["First Verbal"]) + int(liste6["Second Verbal"])) / 4  # For Geography
        fel = (int(liste7["First Exam"]) + int(liste7["Second Exam"]) + int(liste7["First Verbal"]) + int(liste7["Second Verbal"])) / 4  # For Philosophy
        ing = (int(liste8["First Exam"]) + int(liste8["Second Exam"]) + int(liste8["First Verbal"]) + int(liste8["Second Verbal"])) / 4  # For English
        alm = (int(liste9["First Exam"]) + int(liste9["Second Exam"]) + int(liste9["First Verbal"]) + int(liste9["Second Verbal"])) / 4  # For German
        genel = (edebi + mat + fizi + biyo + kim + tar + cog + fel + ing + alm) / 10  # For Overall Average
        print("Your average:")
        print("Literature: {}. Your Literature Average: {}".format(db,edebi))
        print("Math: {}. Your Math Average: {}".format(liste1,mat))
        print("Physics: {}. Your Physics Average: {}".format(liste2,fizi))
        print("Biology: {}. Your Biology Average: {}".format(liste3,biyo))
        print("Chemistry: {}. Your Chemistry Average: {}".format(liste4,kim))
        print("History: {}. Your History Average: {}".format(liste5,tar))
        print("Geography: {}. Your Geography Average: {}".format(liste6,cog))
        print("Philosophy: {}. Your Philosophy Average: {}".format(liste7,fel))
        print("English: {}. Your English Average: {}".format(liste8,ing))
        print("German: {}. Your German Average: {}".format(liste9,alm))
        print("Your Overall Average: {}".format(genel))
    elif(a == "O" or a == "o" and k == 11 or k == 12):  # To Calculate Grade Point Average
        edebi = (int(db["First Exam"]) + int(db["Second Exam"]) + int(db["First Verbal"]) + int(db["Second Verbal"])) / 4  # For Literature
        mat = (int(liste1["First Exam"]) + int(liste1["Second Exam"]) + int(liste1["First Verbal"]) + int(liste1["Second Verbal"])) / 4  # For Mathematics
        fizi = (int(liste2["First Exam"]) + int(liste2["Second Exam"]) + int(liste2["First Verbal"]) + int(liste2["Second Verbal"])) / 4  # For Physics
        biyo = (int(liste3["First Exam"]) + int(liste3["Second Exam"]) + int(liste3["First Verbal"]) + int(liste3["Second Verbal"])) / 4  # For Biology
        kim = (int(liste4["First Exam"]) + int(liste4["Second Exam"]) + int(liste4["First Verbal"]) + int(liste4["Second Verbal"])) / 4  # For Chemistry
        tar = (int(liste5["First Exam"]) + int(liste5["Second Exam"]) + int(liste5["First Verbal"]) + int(liste5["Second Verbal"])) / 4  # For History
        fel = (int(liste7["First Exam"]) + int(liste7["Second Exam"]) + int(liste7["First Verbal"]) + int(liste7["Second Verbal"])) / 4  # For Philosophy
        ing = (int(liste8["First Exam"]) + int(liste8["Second Exam"]) + int(liste8["First Verbal"]) + int(liste8["Second Verbal"])) / 4  # For English
        alm = (int(liste9["First Exam"]) + int(liste9["Second Exam"]) + int(liste9["First Verbal"]) + int(liste9["Second Verbal"])) / 4  # For German
        genel = (edebi + mat + fizi + biyo + kim + tar + fel + ing + alm) / 9  # For Overall Average
        print("Your average:")
        print("Literature: {}. Your Literature Average: {}".format(db, edebi))
        print("Math: {}. Your Math Average: {}".format(liste1, mat))
        print("Physics: {}. Your Physics Average: {}".format(liste2, fizi))
        print("Biology: {}. Your Biology Average: {}".format(liste3, biyo))
        print("Chemistry: {}. Your Chemistry Average: {}".format(liste4, kim))
        print("History: {}. Your History Average: {}".format(liste5, tar))
        print("Philosophy: {}. Your Philosophy Average: {}".format(liste7, fel))
        print("English: {}. Your English Average: {}".format(liste8, ing))
        print("German: {}. Your German Average: {}".format(liste9, alm))
        print("Your Overall Average: {}".format(genel))
    elif(a == "Q" or a == "q"):  # To Stop Code
        print("Good Bye!")
        break
    else:
        print("***********************************************************")
        print("Wrong Code!")
        print("***********************************************************")