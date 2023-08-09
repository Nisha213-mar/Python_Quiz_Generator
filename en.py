perguntas = {1: "What is the equation for an ellipse??", #medium
             2: "Find the Discriminant:\n x² - 5x + 6 = 0", #easy
             3: "Which Newton's Law is the Law of Inertia?", #easy
             4: "What's the volume of a cylinder with a radius of 2 meters\n and height of 10m? Consider π = 3.14", #hard
             5: "Which suffix represents the\nDouble bond in a hydrocarbon?", #easy
             6: "How does the relationship between resistance and electric current take place?", #hard
             7: "What's the constant value of the\nspeed of light in vacuum?", #hard
             8: "How many passwords with 4 different digits\ncan we write with the following digits 1, 2, 3, a, b, c, !, @, # ?", #easy
             9: "An object in resting position develops a constant \n acceleration of 3 m/s² for 4 seconds.\n What's the displacement of the object?", #medium
             10: "Which one of the following periodic properties represents \n the trend of an atom to attract electrons to itself?", #Dificil
             11: "Cesium-137 has a half-life of 30 years.\n Considering that there is 48g of that element?\n How much of it will remains after 120 years?", #Facil
             12: "Which one of the following elements has 3 electrons in the valence shell?", #Media
             13: "Which of the following scientists was responsible\n for the model of the atom known as 'raisin bread'?", #Fac
             14: "Which of the following acids is the least volatile?", #media
             15: "Between water, vinegar, oxygen gas and salt,\nWhich one is a simple substance?", #Fac
             16: "Solve the following inequality: \n 3(1 - 2x) < 2(x + 1) + x  7:", #Media
             17: "Convert 2 * 10⁵ ml to cubic meters,\n the result is:", #Dificl
             18: "Calculate the difference of the area between ​​the two circles,\n the first one has 35 cm radius and the second one 25 cm radius", #Media
             19: "Determine the frequency with the wavelength equals\n1 m, knowing that the speed of the sound equals to 340 m/s.", #dificil
             20: "Considering an ideal gas, having only 1 mol,\nunder a temperature of 273 K and a pressure of 1 atm,\nwhat is the volume?\n\nConsider R = 0,082 atm*L/mol*K"} #media



alternativas = {1.1: "x² + y²/3 = 0",
                1.2: "x³/a + y²/2 = 1",
                1.3: "x²/a = -y³/b",
                1.4: "x²/a² + y²/b² = 1", #correct 1 d)
                1.5: "x² - a²/3y² = 0",
                2.1: "1", #correct 2 a)
                2.2: "0",
                2.3: "4",
                2.4: "16",
                2.5: "38",
                3.1: "First Law", #correct 3 a)
                3.2: "Second Law",
                3.3: "Third Law",
                3.4: "Fourth Law",
                3.5: "Fifth Law",
                4.1: "125.6 m³", #correct 4 a)
                4.2: "123.8 m³", 
                4.3: "75.3  m³",
                4.4: "79.7  m³",
                4.5: "78.8  m³",
                5.1: "an",
                5.2: "dien",
                5.3: "in",
                5.4: "en", #correct 5 d)
                5.5: "diin",
                6.1: "The electric current and resistance are directly proportional.",
                6.2: "The electric current and resistance do not relate.",
                6.3: "The electric current and resistance are inversely proportional.", #correta 6 c)
                6.4: "The electric current and resistance always have the same value.",
                6.5: "None of the options are correct.",
                7.1: "2 x 10⁶ m/s",
                7.2: "3 x 10⁷ m/s",
                7.3: "2 x 10⁸ km/s",
                7.4: "3 x 10⁵ km/s", #correct 7 d)
                7.5: "2 x 10⁶ km/s",
                8.1: "2048",
                8.2: "4124",
                8.3: "3024", #correct 8 c)
                8.4: "1890",
                8.5: "1024",
                9.1: "18 m",
                9.2: "22 m",
                9.3: "30 m", 
                9.4: "12 m",
                9.5: "24 m", #correct 9 e)
                10.1: "Electro-affinity",
                10.2: "Electronegativity", #correct 10 b)
                10.3: "Electropositivity",
                10.4: "Ionization Potential",
                10.5: "Electroneutrality",
                11.1: "3  g", #correct 11 a)
                11.2: "12 g",
                11.3: "6 g",
                11.4: "24 g",
                11.5: "48 g",
                12.1: "Potassium (K)",
                12.2: "Phosphor (P)",
                12.3: "Nihonium (Nh)", # correct 12 c)
                12.4: "Iron (Fe)",
                12.5: "Sodium (Na)",
                13.1: "Chadwick", #rip
                13.2: "Dalton",
                13.3: "Rutherford",
                13.4: "Thomson", #correct 13 d)
                13.5: "Newton",
                14.1: "NaCl",
                14.2: "HF",
                14.3: "HI",
                14.4: "H₂SO₃",
                14.5: "H₂SO₄", #correct 14 e)
                15.1: "Water",
                15.2: "Oxygen Gas", #correct 15 b)
                15.3: "Vinegar salse", 
                15.4: "Sodium",
                15.5: "Salt",
                16.1: "x < 9/8",
                16.2: "x > 3/2",
                16.3: "x < 7/3",
                16.4: "x < 2/7",
                16.5: "x > 8/9", #correct 16 e)
                17.1: "0.002",
                17.2: "0.02", #correct 17 b)
                17.3: "0.0002",
                17.4: "0.2",
                17.5: "0.00002",
                18.1: "100π cm²",
                18.2: "300π cm²",
                18.3: "600π cm²", #correct 18 c)
                18.4: "900π cm²",
                18.5: "1200π cm²",
                19.1: "10 Hz",
                19.2: "25 Hz",
                19.3: "15 Hz",
                19.4: "30 Hz",
                19.5: "20 Hz", #correct 19 e)
                20.1: "2.24 L",
                20.2: "22.4 L", #correct 20 b)
                20.3: "224 L",
                20.4: "224.4 L",
                20.5: "24.2 L"}

explic = {1: "The correct equation for the ellipse is x²/a² + y²/b² = 1" ,
          2: "The formula to find the discriminant is b² - 4*a*c\n Hence, (-5²) - 4*1*6 = 25 - 24 = 1" ,
          3: "The law corresponding to the law of inertia is the 1st Law.\nNewton's First Law of Motion states that a body at rest will remain at rest unless an outside force acts on it.",
          4: "The formula to find the cylinder volume is V = π*R²*h.\n Hence, V = 3.14*2²*10 = 125,6m³.",
          5: "According to IUPAC, the suffix 'en' represents the presence of a douple bond in the hydrocarbon",
          6: "\nAccording to the formula of the 1st Ohm's Law:\nU = r*i\nIt can be proved mathematically that the electrical resistance and the current resistance are inversely proportional.",
          7: "The alternative that correctly represents the speed of light in a vacuum is the\nd) 3 x 10^5 km/s.",
          8: "As the question asked for 4 different digits, \nthe number of possibilities should be reduced by 1 for each new digits.\n There are 10 digits in total, hence it will contain: 9 * 8 * 7 * 6 = 3024 passwords.",
          9: "The equation of uniformly accelerated motion is:\nDeltaS = v0 * t + a * t²/2\n Hence, 0 * 3 + 3 * 4²/2 = 2 meters.",
          10: "Electronegativity is a property that describes\n The tendency of an atom to attract electrons toward itself.",
          11: "Every time the half-life happens,\nthe mass of the element is divided by 2,\nhence the mass is divided 4 times (120/30=4), resulting in 3 grams of cesio-137",
          12: "The correct answer is the nihonium element, as it belongs to family 3A.\nAnd those in this family have 3 electrons in the valence shell.",
          13: "Thomson was responsible for the idea of ​​an atom being positive\nwith negative particles in it, making the model look like a rising bread.",
          14: "H2SO4, sulfuric acid, is the least volatile acid\nfor being considered as a fixed acid.",
          15: "Oxygen gas is a simple substance because\n it's formed by two atoms of the same chemical element, oxygen.",
          16: "We calculate the inequality, do the distribution\n3 - 6x < 2x + + x - 7, resulting in x > 8/9",
          17: "To calculate, we divide the value by 1e+6",
          18: "To calculate the difference,\n first we use the formula of the area which is A = π · r² \nthen we subtract the value of the large circle with the smallest one\n and obtain the result 600π cm²",
          19: "We use the formula f = v ÷ λ, then we replace the values ​​reaching the correct option.",
          20: "Because it's an ideal gas we are going to use the Clapeyron equation which is\np*V = n*R*T\n then replacing the values we get 1*V = 1*0,082*273, hence V = 22.4 L." }