label AfterFlood:

    $ WakeupChoice = "null"
    $ correct = 0
    $ TerrestrialPlanetChoice = "null"
    $ GasGiantsChoice = "null"
    $ AstronomyChoice = "null"
    $ DwarfPlanetChoice = "null"
    $ PlayOrHomeworkChoice = "null"

    stop music fadeout 2.0
    show text("{size=40}Isang linggo ang nakalipas simula noong pagbaha.{/size}") with dissolve
    with Pause (3)
    scene trans_relativesHouse with dissolve
    show bautista family with dissolve
    show text("{size=40}Isang buwan na din sila\nnagsimula makitira sa kanilang kamag-anak.{/size}") with dissolve
    with Pause (5)
    show text("{size=40}Ang Pamilya Bautista ay nagsimula na ding masanay\nsa kanilang bagong pamumuhay.{/size}") with dissolve
    with Pause (5)
    scene black with dissolve
    show text("{size=40}Ngunit...{/size}") with dissolve
    with Pause (3)
    hide text with dissolve
    none "..."
    play sound "assets/SFX/PhoneRing.mp3"
    none "(Ring ring.)"
    Joseph_left "Hello?"
    Man_right "Hello, Mr. Bautista."
    Man_right "Good news po galing sa insurance company nyo po. Isa po sa mga tauhan namin na nag-aayos ng inyong bahay na nasunog."
    Man_right "Sinabi sa amin na naayos na po ang inyong bahay at pwede na po ulit tirahan ng inyong pamilya."
    Joseph_left "Talaga? Maraming salamat!"
    Man_right "Wala pong anuman."
    none "..."
    Joseph_left "Ma, Makakauwi na tayo!"
    Mary_center "Talaga?"
    Juan_center "Yehey!"
    May_center "Yehey!"

    scene trans_house with dissolve
    show mode confirm with dissolve
    show text("{size=60}Ang paglisan ng bagyo{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve

    none "..."
    play music "assets/FreeBGM/TheEveningSky.mp3"
    Mary_center "'.....Gising-gising na batang antukin.'"
    none "(A familiar words break my sleep.)"

    scene daytimeBedroom with dissolve
    show Mary neutral with dissolve
    
    Mary_center "Juan maleleyt ka na sa school mo, handa na ang almusal!"
    Juan_left "Mmmm.."

    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Inaantok pa si Juan ngunit kinakailangan na nyang pumasok sa paaralan."
    $ Text1="Mamaya na lang.."
    $ Text2="Bumangon"
    $ Icon1 = Image("assets/Sprites/Items/icon_sleep.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_wakeup.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeupChoice",Icon1,Text1,"later",Icon2,Text2,"wake",False) with dissolve
    hide mode confirm with dissolve

    if WakeupChoice == "wake":
        Juan_left "Good morning po mama"
        show Juan neutralLeft with dissolve
        show Mary panRight with dissolve
        Mary_right "Good morning, Juan!"
    if WakeupChoice == "later":
        show Juan neutralLeft with dissolve
        show Mary panRight with dissolve
        Juan_left "..Mamaya..na lang. Five minutes pa, Ma..."
        show Mary surprised with dissolve
        Mary_right "Tara na Juan kailangan mo na bumangon"

    Mary_right "Nakalimutan mo ba iset yung alarm clock mo kagabi?"
    show Mary talking with dissolve
    Mary_right "Inaantay kita sa kusina."
    Juan_left "Ayy! sorry mama nakalimutan ko nga."
    show Mary smile with dissolve
    none "*Natawa si Mary."
    Mary_right "O sya handa na yung almusal sa kusina kumain ka na at bilisan mo maleleyt ka na!"
    Juan_left "Okay."

    scene kitchen with dissolve 
    show Juan neutral with dissolve
    Juan_center "(Matagal tagal na rin akong di nakakapagalmusal sa sarili naming bahay)"
    Juan_center "..."
    show Juan smile1
    Juan_center "Yummy!"
    show Joseph neutralright with easeinright
    show Juan panLeft with dissolve
    Joseph_right "Good morning Juan!"
    Juan_left "Good morning po Papa!"
    show Joseph talking with dissolve
    Joseph_right "Musta pagtulog mo mahimbing ba?"
    Joseph_right "Namiss mo na ba yung kwarto mo?"
    show Joseph neutral with dissolve
    show Juan smile2 with dissolve
    Juan_left "Opo papa!, Namiss ko din po yung paglalaro ko ng video games sa kwarto ko."    
    show Joseph laugh with dissolve
    Joseph_right "Ala talagang tatalo kapag nasa sariling bahay ka hahaha!"
    show Joseph neutral with dissolve
    show Juan neutral with dissolve
    Mary_center "Pa!, Handa niyo na po yung mga dadalhin nyo."
    Joseph_right "Ayy! Muntik ko na makalimutan."
    Joseph_right "O sya mamaya na lang Juan."
    Juan_left "Ingat ka po papa."
    hide Joseph with moveoutright
    none "Tapos na si Juan mag-almusal."    
    show Mary neutralright with easeinright
    Mary_right "Juan tapos ka na ba kumain?"
    show Juan smile2 with dissolve
    Juan_left "Opo mama ang sarap talaga ng luto nyo!"
    show Juan neutral with dissolve
    show Mary talking with dissolve
    Mary_right "Aa Juan may nakalimutan nga pala ko sabihin sayo."
    Juan_left "Ano po yon mama?"
    Mary_right "Nasunog ko kasi yung niluluto kong babaunin mo mamayang tanghali."
    Mary_right "Inaasikaso ko kasi yung kapatid mo hindi ko na namalayan na may niluluto nga pala ako naamoy ko na lang na may nasusunog."
    Juan_left "Ay ganun po ba?!"
    Mary_right "O sya, Eto 100 pesos bili ka na lang ng makakain mo mamayang tanghali."
    Mary_right "Siguraduhin mo lang hindi tsitsirya bibilhin mo ha?"
    show Mary neutral with dissolve
    Juan_left "Opo mama."
    show Mary smile with dissolve
    Mary_right "Hehe sensya talaga anak."
    Mary_right "Ingat ka ha!"
    show Mary panRCenter with dissolve
    show May neutralright with easeinright
    May_right "Bye kuya Juan, Ingat ka!"
    show Juan smile1 with dissolve
    Juan_left "Bye mama!, Bye May!"

    play sound "assets/SFX/Door.mp3"
    scene daytimeStreet1 with dissolve
    show Juan neutral with dissolve
    none "..."
    Juan_center "Kakamiss na maglakad sa lugar nato!"
    Juan_center "Matagal tagal na rin ako di napapadpad dito."
    Juan_center "Sana wala ngayon yung aso."
    none "(May naalala bigla si Juan.)"
    Juan_center "Ay! Muntik ko na makalimutan."
    Juan_center "Kailangan ko nga pala bumili ng makakakain ko para mamayang tanghali."
    Juan_center "Kelangan ko na magmadali!"
    scene black with dissolve


    play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    none "Dumating si Juan sa isang Sari-Sari store."
    scene groceryshelf with dissolve
    Juan_center "Hmm ano kaya bibilhin ko?"
    Juan_center "Meron akong 100 pesos para pagkasyahin."

    show mode confirm with dissolve
    call screen Grocery()
    hide mode confirm with dissolve

    if not persistent.JuanExtravagant and money == 0:
        $ renpy.notify("Unlocked: Juan extravagant")
        $ persistent.JuanExtravagant=True
        $ persistent.totalAchievement +=1

    Juan_center "Ayos may pagkain na ko para mamaya!"
    scene daytimeStreet1 with dissolve
    show Juan neutral with dissolve
    Juan_center "Oras na para pumasok!"

    none "Habang naglalakad si Juan, May napansin siyang pamilyar na tao"
    Juan_center "Teka, siya ba yung?"
    show Alice neutralright with easeinright
    show Juan panLeft with dissolve

    if Alice_unlock == False:  
        Juan_left "Hello."
        show Alice surprised with dissolve
        Girl_right "Ah!"
        show Alice smile with dissolve
        Girl_right "Diba ikaw yung nagligtas saken sa aso noon."
        Girl_right "Napansin ko din na pareho tayo ng uniform, kaso nahihiya ako kausapin ka sa school."
        Girl_right "So..aaaaa..."
        Girl_right "Maraming salamat!"
        Juan_left "Wala yon hehe!"
        Juan_left "Ako nga pala si Juan"
        Girl_right "Nagagalak ako makilala ka Juan, Ako naman si Alice!"
        $ Alice_unlock == True 
    else:
        show Juan smile1 with dissolve
        Juan_left "Hi Alice!"
        show Juan neutral with dissolve
        show Alice surprised with dissolve
        Alice_right "Ah!"
        show Alice smile with dissolve
        Alice_right "Good morning Juan!"
        Alice_right "Nabalitaan ko pala na naayos na daw yung bahay nyo at doon na ulit kayo nakatira?"
        show Juan smile2 with dissolve
        Juan_left "Oo! Kaya nakakapaglaro na ulit ako sa sarili kong kwarto."
        show Juan neutral with dissolve
        Alice_right "Mabuti naman."
    
    none "..."
    Alice_right "Anu nga pala yang dala dala mo Juan??"
    Juan_left "Ah eto? Nasunog kasi ni mama yung niluluto nya na baon ko kaya sabi nya saken bumili na lang muna ako ng pagkain ko para mamaya."
    show Alice surprised with dissolve
    Alice_right "Ay ganun?!"
    show Alice smile with dissolve
    Alice_right "Mahirap sigurong maging nanay."
    Alice_right "Malapit na pala mag 7 AM kaylangan na natin magmadali!"
    Juan_left "Ay oo nga pala"
    show Juan smile2 with dissolve
    Juan_left "Tara!"

    scene black with dissolve
    none "Si Juan at Alice ay dali-daling pumunta sa Paaralan upang makaabot sila sa kanilang 7am class"
    scene schoolbuilding with dissolve
    none "Kahit papaano, Nakariting si Juan at Alice sa kanilang paaralan at nakaabot sa kanilang klase."
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"
    scene classroom with dissolve

    show Cathy neutral with easeinleft

    Cathy_center "Good morning class, Kamusta kayo?"
    Class_center "Good morning po, Teacher!"
    Cathy_center "Lahat ba nakaattend sa ating flag ceremony?"
    Class_center "Opo, Teacher!"
    show Cathy smile with dissolve
    Cathy_center "Very good!"
    show Cathy neutral with dissolve
    Cathy_center "So magsisimula na ko ng ating lesson para sa ngayung umaga."
    Cathy_center "Alam kong marami sa inyo ang hindi pa naririnig o alam ang salitang Astronomy!"
    Cathy_center "Okay let's begin!"

    play music "assets/BGM/FeudalNight.mp3"
    show Cathy panningRight
    show school solarsystem with dissolve
    Cathy_center "{color=#adf569}Astronomy{/color} ay isang sangay ng agham na nag-aaral tungkol sa mga celestial objects and phenomenas."
    Cathy_center "Ang ating solar system ay binubuo ng 1 star at 8 planeta"
    show Cathy smile with dissolve
    Cathy_center "Tama ang rinig nyo Class! Ang ating Araw ay isang star naniniwala ba kayo?"
    show Cathy neutral with dissolve
    show school planet1 with dissolve
    Cathy_center "Ang ating planeta, Earth kasama ang Mars, Venus at Mercury ay tinatawag na {color=#adf569}Terrestrial Planets{/color}."
    Cathy_center "Ibig sabhin ay binubuo sila ng mga bato at iba't ibang uri ng metal."
    show school planet2 with dissolve
    Cathy_center "Samantala, Ang Jupiter, Saturn, Uranus and Neptune ay tinatawag namang {color=#adf569}Gas Giants{/color}."
    Cathy_center "Kaya sila tinawag na 'Gas Giants' ay dahil binubuo sila ng ibat'ibang uri ng gas."
    Cathy_center "These planets usually form farther from the sun due to it's size and lower density."
    Class_center "Ano naman po ang Pluto Teacher?"
    Cathy_center "Ang Pluto naman ay isang {color=#adf569}Dwarf planet{/color}."
    Cathy_center "Tulad ng Ceres, Eris and Haumea dahil sa sobrang liit nila at di malinaw ang kanilang orbit o pag-ikot sa araw."
    show Cathy smile with dissolve
    Cathy_center "Pwede nyo silang isipin na isang malaking Asteroid na halos mukhang planeta!"
    show Cathy neutral with dissolve
    hide school with dissolve
    show Cathy panningBack with dissolve
    Cathy_center "Ok Class sinulat niyo ba ang mga tinalakay naten?"
    show Cathy smile with dissolve
    Cathy_center "Because it's Quiz time!"
    show Cathy neutral with dissolve
    Cathy_center "Ok class let's begin, Walang cheating okay?"

    Cathy_center "Question#1: Ano ang tawag sa kinabibilangan ng Earth at Venus?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "1.) Ano ang tawag sa kinabibilangan \n ng Earth at Venus?"
    $ ans1 = "A.) Planets"
    $ ans2 = "B.) Moon"
    $ ans3 = "C.) Terrestrial Planets"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"TerrestrialPlanetChoice",ans1,ans2,ans3,"Planets","Moon","Terrestrial Planets") with dissolve
    hide mode confirm with dissolve
    
    if TerrestrialPlanetChoice == "Terrestrial Planets":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Excellent Juan!"
    if TerrestrialPlanetChoice == "Planets":
        show Cathy sad with dissolve
        Cathy_center "Yes, Pero hindi iyon ang tamang sagot Juan."
    if TerrestrialPlanetChoice == "Moon":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#2: Ano naman ang tawag sa kinabibilangan ng Jupiter and Saturn?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "2.) Ano naman ang tawag sa kinabibilangan\nng Jupiter and Saturn?"
    $ ans1 = "A.) Terrestrial Planets"
    $ ans2 = "B.) Gas Giants"
    $ ans3 = "C.) A Star"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"GasGiantsChoice",ans1,ans2,ans3,"Terrestrial Planets","Gas Giants","A Star") with dissolve
    hide mode confirm with dissolve

    if GasGiantsChoice == "Gas Giants":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Very good Juan!"
    if GasGiantsChoice == "Terrestrial Planets":
        show Cathy sad with dissolve
        Cathy_center "Kabaligtaran ang iyong sagot Juan."
    if GasGiantsChoice == "A Star":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#3: Ano ang isang sangay ng agham na nag-aaral tungkol sa mga celestial objects and phenomenas?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "3.) Ano ang isang sangay ng agham\nna nag-aaral tungkol sa\nmga celestial objects and phenomenas?"
    $ ans1 = "A.) Astronomy"
    $ ans2 = "B.) Gastroenterology"
    $ ans3 = "C.) Science"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"AstronomyChoice",ans1,ans2,ans3,"Astronomy","Gastroenterology","Science") with dissolve
    hide mode confirm with dissolve

    if AstronomyChoice == "Astronomy":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Correct!"
    if AstronomyChoice == "Gastroenterology":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."
    if AstronomyChoice == "Science":
        show Cathy sad with dissolve
        Cathy_center "Mali Juan, pero isa ito sa mga sangay ng Science."

    show Cathy neutral with dissolve
    Cathy_center "Question#4: Ano ang tawag sa kinabibilangan ng Pluto?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "4.) Ano ang tawag sa kinabibilangan ng pluto?"
    $ ans1 = "A.) Goblin"
    $ ans2 = "B.) Dwarf Planet"
    $ ans3 = "C.) Asteroid"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"DwarfPlanetChoice",ans1,ans2,ans3,"Goblin","Dwarf Planet","Asteroid") with dissolve
    hide mode confirm with dissolve

    if DwarfPlanetChoice== "Dwarf Planet":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Yes Juan that is correct!"
    if DwarfPlanetChoice == "Goblin":
        show Cathy sad with dissolve
        Cathy_center "Ano? No Juan mali."
    if DwarfPlanetChoice == "Asteroid":
        show Cathy sad with dissolve
        Cathy_center "Malapit na pero hindi iyon ang tamang sagot."

    show Cathy neutral
    Cathy_center "Okay class That's it for your quiz."
    Cathy_center "Juan you got [correct] of 4 right."

    if not persistent.LittleEinstein and correct == 4:
        $ renpy.notify("Unlocked: Little Einstein")
        $ persistent.LittleEinstein=True
        $ persistent.totalAchievement +=1

    Cathy_center "At dito nagtatapos ang ating quiz for today!"
    Cathy_center "Oo nga pala class, Nakalimutan kong sabihin."
    Cathy_center "Kung napapansin nyo dumadami ang mga minor earthquakes, especially sa mga lugar sa Visayas at Mindanao."
    
    if ListenChoice == "Listen":
        Cathy_center "Nakikipag usap ako kay Mr. Rey kung paano natin maproprotektahan ang ating mga sarili in case na magkaroon ng earthquake."
    else:
        Cathy_center "Nakikipag usap ako sa local fire department kung paano natin maproprotektahan ang ating mga sarili in case na magkaroon ng earthquake."
    show Cathy smile with dissolve
    Cathy_center "At ang pinakamabisa paring paraan para maproktahan naten ang mga sarili kung sakaling lumindol earthquake ay ang {color=#fe7e66}Drop, Cover, Hold{/color} method."
    show Cathy panningRight with dissolve
    with Pause(2)
    show earthquake duck with dissolve
    Cathy_right"{color=#fe7e66}Drop{/color} Kung saan ka nakatayo, dumapa ka." 
    Cathy_right "Ang nagagawa nito ay upang maiwasan ang pagkabuwal at pagkabagok at makagapang sa mas ligtas na lugar."
    show earthquake cover with dissolve
    Cathy_right "{color=#fe7e66}Cover{/color} Ilagay ang kamay sa batok at ulo upang maproteksyunan ito."
    Cathy_right "Kapag mayroong upuan o lamesa na malapit gumapang at pumunta sa ilalim nito upang maproteksyunan sa mga bagay bagay na bumabagsak."
    Cathy_right "Kung walang masisilungan gumapang sa isang malapit na pader na malayo sa mga bintana."
    Cathy_right "Manatiling nakabaluktot ang mga binti sa harap ng katawan upang maproteksyunan ang mga maseselang bahagi ng katawan."
    show earthquake hold with dissolve
    Cathy_right "{color=#fe7e66}Hold{/color} hanggang tumigil ang pag lindol."
    Cathy_right "Kapag may nasisilungan: Hawakan ito ng isang kamay; at ihanda ang sarili."
    Cathy_right "Kapag walang masisilungan: Hawakan at takpan ng mga kamay at braso ang Parte ng ulo at batok"
    hide earthquake with dissolve
    show Cathy panningBack
    Cathy_center "Kapag ikaw naman ay nasa labas lumayo sa mga matataas na gusali at magpunta sa isang open area."
    Cathy_center "Upang maproteksyonan ka sa mga bagay bagay na mahuhulog na pwede kang masaktan."
    Cathy_center "Naiintindihan nyo ba class?"
    Class_center "Yes po Teacher!"
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell rings.)"
    show Cathy smile with dissolve
    Class_center "So iyon lang para sa klase niyo ngayung umaga, Enjoy your lunch!"
    stop music

    play music "assets/FreeBGM/DreamOfChildrensRoom.mp3"
    scene black with dissolve
    Juan_center "(Pagtapos ng klase, Magkasama kami umuwi ni Peter at madami kaming napagkwentuhan.)"
    scene afternoonStreet1 with dissolve
    show Peter neutralRight with dissolve
    show Juan neutralLeft with dissolve
    Juan_left "Grabe! kapagod ngayung araw."
    Juan_left "Madami na naman binigay mga teacher naten na homeworks."
    Peter_right "Oo nga e.."
    Peter_right "Sya nga pala Juan diba birthday mo bukas?"
    show Juan confident with dissolve
    Juan_left "Oo! Sasabihin ko nga kila Mama at Papa na bilhan ako nung bagong Sword Style Online."
    show Peter smile with dissolve
    Peter_right "Oh! Yung Sword Style Online 2?"
    Peter_right "Paka astig nun!, Kalalabas lang nun last week masyado kasing mahal kaya kaylangan ko pa mag-ipon para makabili."
    Peter_right "Hindi ko pa nga din alam kung mabibili ko nga ba."
    show Peter neutral with dissolve
    show Juan neutral with dissolve
    Juan_left "Haha! Aantayin kita makabili gusto kita makalaro sa SSO 2."
    Peter_right "Sure!"
    show Juan smile2 with dissolve
    Juan_left "Bukas na lang ulit Peter!"

    scene black with dissolve
    none "Nakauwi na si Juan matapos ang nakakapagod na gawain nya sa paaralan."
    none "Napansin ni Juan na mayroon silang bisita."
    scene nighttimeLivingRoom with dissolve
    show Juan neutralLeft with dissolve
    show Joseph neutralright with dissolve
    Joseph_right "Oh Juan! Nakauwi ka na pala, Kamusta sa school?"
    Juan_left "Ok naman Papa! Masaya."
    show Joseph talking with dissolve
    Joseph_right "May mga nag-aantay nga pala sa iyo."
    show Joseph neutral with dissolve
    Juan_left "Sino? Di kaya sila!?"
    hide Joseph with moveoutright
    with Pause(2)
    Joseph_right "James!, Glenn! Nakauwi na si Juan!"

    show James neutral with easeinright
    show Glenn neutralRight with easeinright
    show James laugh with dissolve
    James_center "Hi Juan!"
    show Glenn laugh with dissolve
    Glenn_right "Hello Juan!"
    show Juan smile1 with dissolve
    Juan_left "Glenn! James!"
    show Juan smile2 with dissolve
    Juan_left "Ang sabi nyo mga bandang summer kayo bibista di ko inaakala na dadalawin nyo ko bago ako mag birthday."
    show James talking with dissolve
    James_center "Hehe!, Syempre naisip namen na eto pinakamagandang araw na bisitahin ka."
    show Glenn talking with dissolve
    Glenn_right "Pinilit pa nga namen sila Mama at Papa para dito muna kami ng 3 araw."
    James_center "Buti na lang malapit si Tito nakatira dito mga ilang bahay lang pagitan."
    Glenn_right "Inimbitahan nga din pala kami ng mga magulang mo na dito na maghapunan."
    Juan_left "Haha! Matagal tagal na rin tayong hindi nagkakasama-sama, Namiss ko kayo!"
    Mary_right "Mga bata! Handa na ang hapunan halika na kayo bago pa lumamig ang pagkain."
    show James neutral
    show Glenn neutral
    show Juan neutral
    James_center "Maya na tayo magkwentuhan at maglaro, Tara kain muna tayo hehe!"
    Juan_left "Oo nga gutom na gutom na ko eh."
    Glenn_right "Tara!"

    scene black with dissolve
    none "Pumunta sila Juan, Glenn and James sa hapag kainan at nagulat sa sarap ng mga niluto na pagkain ng kanyang Ina na si Mary."
    none "..."
    none "Matapos kumain agad bumalik ang tatlo sa kwarto ni Juan at nagsimulang maglaro."
    scene nighttimeBedroom with dissolve 
    show James neutral with dissolve    
    show Glenn neutralRight with dissolve
    show Juan neutralLeft with dissolve
    Glenn_right "Napakasarap ng mga pagkain na niluto ng Mama mo Juan!"
    Juan_left "Diba?, Mama ko ata ang pinakamagaling mag luto dito sa baryo!"
    show James talking with dissolve
    James_center "Nga pala Juan, Meron ka na bang Sword Style Online 2?"
    Juan_left "Wala pa eh, Pero kakausapin ko sila Mama at Papa bukas na bilhan ako."
    show Glenn laugh with dissolve
    Glenn_right "Hahaha! tignan mo kami tumalo ng mga Malalakas na Players, Nakakatuwa!"
    show Glenn neutral
    show Juan smile2 with dissolve
    Juan_left "Woah Talaga!? Sabik na talaga ako makalaro kayo"
    show Glenn laugh with dissolve
    Glenn_right "Hahahaha!"
    show James laugh with dissolve
    James_center "Hahahaha!"
    show Juan smile2 with dissolve
    Juan_left "Hahahaha!"
    show Glenn neutral with dissolve
    show James talking with dissolve
    show Juan neutral with dissolve
    James_center "Ah Juan, kung maglaro kaya tayo hanggang 9?"
    Juan_left "(Hmm meron pa akong mga homeworks pero gusto ko pa makipaglaro kila James at Glenn..)"

    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Ano sasabihin ni Juan kila James at Glenn?"
    $ Text1="Gusto ko pa maglaro!"
    $ Text2="Gagawin ko na mga Homeworks ko."
    $ Icon1 = Image("assets/Sprites/Items/icon_play_games.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_do_homework.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"PlayOrHomeworkChoice",Icon1,Text1,"play",Icon2,Text2,"dontplay",False) with dissolve
    hide mode confirm with dissolve

    if PlayOrHomeworkChoice == "play":
        show Juan smile2 with dissolve

        if not persistent.LetsParty:
            $ renpy.notify("Unlocked: Let's party!")
            $ persistent.LetsParty=True
            $ persistent.totalAchievement +=1

        Juan_left "Sige ba!! bakit hindi, Kaya nga kayo nandito diba?"
        show James laugh with dissolve
        James_center "Yown! Ok na, Ready na kayo maglaro!"
        James_center "Gusto namin pakita sayo yung natutunan namen nung nakaraan."
        show Glenn laugh with dissolve
        Glenn_right "Tara!"
        scene black with dissolve
        none "Magdamag na naglaro sila Juan, James, at Glenn."
        none "Naging masaya silang tatlo ngayon dahil apat na taon na ang nakalipas bago sila ulit sila magkakasama."
    else:
        Juan_left "Sorry mga tol may mga gagawin pa kasi akong homework ngaung gabi."
        Juan_left "Baka bukas? Pangako maglalaro tayo pag mayroon na kong SSO 2."
        James_center "Aww.. okay Juan bukas na lang."
        Glenn_right "Sige Juan kita kits na lang bukas."
        show Juan smile2 with dissolve
        James_center "Kita kits Bukas!"
        scene black with dissolve
        none "At nagpaalam na sila Glenn at James kay Juan at sa kanyang mga magulang at umuwi patungo sa bahay ng kanilang tito."
        none "Nagsimula na si Juan gawin ang kanyang mga homework kahit na gustong gusto pa nya makipag laro kila Glenn at James dahil apat na taon na ang nakalipas bago ulit sila magkakasama."

    jump EarthquakeDisaster
    #======================Custom Scenes=======================================

    screen Grocery():
        modal True

        $ ResetText = Text("Reset",bold=True ,size=70, color="#adf569")
        $ BuyText = Text("Buy",bold=True ,size=70, color="#adf569")
        $ bread = Image("assets/Sprites/Items/bread.png")
        $ chocolate = Image("assets/Sprites/Items/chocolate.png")
        $ juice = Image("assets/Sprites/Items/juice.png")
        $ soda = Image("assets/Sprites/Items/soda.png")
        $ water = Image("assets/Sprites/Items/waterbottle.png")

        vbox xpos -1200 ypos 900:
            textbutton(ResetText) xpos 1400 action [SetVariable("bread_selected", False),SetVariable("chocolate_selected", False),SetVariable("juice_selected", False),SetVariable("soda_selected", False),SetVariable("water_selected", False),SetVariable("money", 100)]

        
        vbox ypos 900:
            if not money < 0 and not money == 100:
                textbutton(BuyText) xpos 1400 action Return()


        if money >= 0:
            text(Text("Money: " + "%d" % money, bold=True ,size=60, xpos=0.0, color="#adf569"))
        else:
            text(Text("Money: " + "%d" % money, bold=True ,size=60, xpos=0.0, color="#FF3600"))

        vbox xalign 0.5:
            text(Text("Juan should buy food for his lunch for today",size=50))
        

        vbox xpos 350 ypos 250:
            if bread_selected == False:
                text(Text("Bread: P25"))
                imagebutton idle Transform(bread, zoom=0.3) action [SetVariable("bread_selected", True),SetVariable("money", money - 25)] activate_sound sfx_click1
        
        vbox xpos 1450 ypos 250:
            if chocolate_selected == False:
                text(Text("Chocolate: P45"))
                imagebutton idle Transform(chocolate, zoom=0.08) action [SetVariable("chocolate_selected", True),SetVariable("money", money - 45)] activate_sound sfx_click1
            
        vbox xpos 350 ypos 600:
            if juice_selected == False:
                text(Text("Juice: P15"))
                imagebutton idle Transform(juice, zoom=0.5) action [SetVariable("juice_selected", True),SetVariable("money", money - 15)] activate_sound sfx_click1
            
        vbox xpos 900 ypos 600:
            if soda_selected == False:
                text(Text("Soda: P30"))
                imagebutton idle Transform(soda, zoom=0.17) action [SetVariable("soda_selected", True),SetVariable("money", money - 30)] activate_sound sfx_click1
            
        vbox xpos 1450 ypos 600:
            if water_selected == False:
                text(Text("Water: P15"))
                imagebutton idle Transform(water, zoom=0.25) action [SetVariable("water_selected", True),SetVariable("money", money - 15)] activate_sound sfx_click1