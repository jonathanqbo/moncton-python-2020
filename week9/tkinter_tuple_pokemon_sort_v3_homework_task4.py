import tkinter

pokemons = (('Sentret', 35, 46, 34),
            ('Furret', 85, 76, 64),
            ('Hoothoot', 60, 30, 30),
            ('Noctowl', 100, 50, 50),
            ('Ledyba', 40, 20, 30),
            ('Ledian', 55, 35, 50),
            ('Spinarak', 40, 60, 40),
            ('Ariados', 70, 90, 70),
            ('Crobat', 85, 90, 80),
            ('Chinchou', 75, 38, 38),
            ('Lanturn', 125, 58, 58),
            ('Pichu', 20, 40, 15),
            ('Cleffa', 50, 25, 28),
            ('Igglybuff', 90, 30, 15),
            ('Togepi', 35, 20, 65),
            ('Togetic', 55, 40, 85),
            ('Natu', 40, 50, 45),
            ('Xatu', 65, 75, 70),
            ('Mareep', 55, 40, 40),
            ('Flaaffy', 70, 55, 55),
            ('Ampharos', 90, 75, 75),
            ('Bellossom', 75, 80, 85),
            ('Marill', 70, 20, 50),
            ('Azumarill', 100, 50, 80),
            ('Sudowoodo', 70, 100, 115),
            ('Politoed', 90, 75, 75),
            ('Hoppip', 35, 35, 40),
            ('Skiploom', 55, 45, 50),
            ('Jumpluff', 75, 55, 70),
            ('Aipom', 55, 70, 55),
            ('Sunkern', 30, 30, 30),
            ('Sunflora', 75, 75, 55),
            ('Yanma', 65, 65, 45),
            ('Wooper', 55, 45, 45),
            ('Quagsire', 95, 85, 85),
            ('Espeon', 65, 65, 60),
            ('Umbreon', 95, 65, 110),
            ('Murkrow', 60, 85, 42),
            ('Slowking', 95, 75, 80),
            ('Misdreavus', 60, 60, 60),
            ('Unown', 48, 72, 48),
            ('Wobbuffet', 190, 33, 58),
            ('Girafarig', 70, 80, 65),
            ('Pineco', 50, 65, 90),
            ('Forretress', 75, 90, 140),
            ('Dunsparce', 100, 70, 70),
            ('Gligar', 65, 75, 105),
            ('Steelix', 75, 85, 200),
            ('Snubbull', 60, 80, 50),
            ('Granbull', 90, 120, 75),
            ('Qwilfish', 65, 95, 75),
            ('Scizor', 70, 130, 100),
            ('Shuckle', 20, 10, 230),
            ('Heracross', 80, 125, 75),
            ('Sneasel', 55, 95, 55),
            ('Teddiursa', 60, 80, 50),
            ('Ursaring', 90, 130, 75),
            ('Slugma', 40, 40, 40),
            ('Magcargo', 50, 50, 120),
            ('Swinub', 50, 50, 40),
            ('Piloswine', 100, 100, 80),
            ('Corsola', 55, 55, 85),
            ('Remoraid', 35, 65, 35),
            ('Octillery', 75, 105, 75),
            ('Delibird', 45, 55, 45),
            ('Mantine', 65, 40, 70),
            ('Skarmory', 65, 80, 140),
            ('Houndour', 45, 60, 30),
            ('Houndoom', 75, 90, 50),
            ('Kingdra', 75, 95, 95),
            ('Phanpy', 90, 60, 60),
            ('Donphan', 90, 120, 120),
            ('Porygon2', 85, 80, 90),
            ('Stantler', 73, 95, 62),
            ('Smeargle', 55, 20, 35),
            ('Tyrogue', 35, 35, 35),
            ('Hitmontop', 50, 95, 95),
            ('Smoochum', 45, 30, 15),
            ('Elekid', 45, 63, 37),
            ('Magby', 45, 75, 37),
            ('Miltank', 95, 80, 105),
            ('Blissey', 255, 10, 10),
            ('Raikou', 90, 85, 75),
            ('Entei', 115, 115, 85),
            ('Suicune', 100, 75, 115),
            ('Larvitar', 50, 64, 50),
            ('Pupitar', 70, 84, 70),
            ('Tyranitar', 100, 134, 110),
            ('Lugia', 106, 90, 130),
            ('Ho-oh', 106, 130, 90),
            ('Celebi', 100, 100, 100),
            ('Treecko', 40, 45, 35),
            ('Grovyle', 50, 65, 45),
            ('Sceptile', 70, 85, 65),
            ('Torchic', 45, 60, 40),
            ('Combusken', 60, 85, 60),
            ('Blaziken', 80, 120, 70),
            ('Mudkip', 50, 70, 50),
            ('Marshtomp', 70, 85, 70),
            ('Swampert', 100, 110, 90),
            ('Poochyena', 35, 55, 35),
            ('Mightyena', 70, 90, 70),
            ('Zigzagoon', 38, 30, 41),
            ('Linoone', 78, 70, 61),
            ('Wurmple', 45, 45, 35),
            ('Silcoon', 50, 35, 55),
            ('Beautifly', 60, 70, 50),
            ('Cascoon', 50, 35, 55),
            ('Dustox', 60, 50, 70),
            ('Lotad', 40, 30, 30),
            ('Lombre', 60, 50, 50),
            ('Ludicolo', 80, 70, 70),
            ('Seedot', 40, 40, 50),
            ('Nuzleaf', 70, 70, 40),
            ('Shiftry', 90, 100, 60),
            ('Taillow', 40, 55, 30),
            ('Swellow', 60, 85, 60),
            ('Wingull', 40, 30, 30),
            ('Pelipper', 60, 50, 100),
            ('Ralts', 28, 25, 25),
            ('Kirlia', 38, 35, 35),
            ('Gardevoir', 68, 65, 65),
            ('Surskit', 40, 30, 32),
            ('Masquerain', 70, 60, 62),
            ('Shroomish', 60, 40, 60),
            ('Breloom', 60, 130, 80),
            ('Slakoth', 60, 60, 60),
            ('Vigoroth', 80, 80, 80),
            ('Slaking', 150, 160, 100),
            ('Nincada', 31, 45, 90),
            ('Ninjask', 61, 90, 45),
            ('Shedinja', 1, 90, 45),
            ('Whismur', 64, 51, 23),
            ('Loudred', 84, 71, 43),
            ('Exploud', 104, 91, 63),
            ('Makuhita', 72, 60, 30),
            ('Hariyama', 144, 120, 60),
            ('Azurill', 50, 20, 40),
            ('Nosepass', 30, 45, 135),
            ('Skitty', 50, 45, 45),
            ('Delcatty', 70, 65, 65),
            ('Sableye', 50, 75, 75),
            ('Mawile', 50, 85, 85),
            ('Aron', 50, 70, 100),
            ('Lairon', 60, 90, 140),
            ('Aggron', 70, 110, 180),
            ('Meditite', 30, 40, 55),
            ('Medicham', 60, 60, 75),
            ('Electrike', 40, 45, 40),
            ('Manectric', 70, 75, 60),
            ('Plusle', 60, 50, 40),
            ('Minun', 60, 40, 50),
            ('Volbeat', 65, 73, 55),
            ('Illumise', 65, 47, 55),
            ('Roselia', 50, 60, 45),
            ('Gulpin', 70, 43, 53),
            ('Swalot', 100, 73, 83),
            ('Carvanha', 45, 90, 20),
            ('Sharpedo', 70, 120, 40),
            ('Wailmer', 130, 70, 35),
            ('Wailord', 170, 90, 45),
            ('Numel', 60, 60, 40),
            ('Camerupt', 70, 100, 70),
            ('Torkoal', 70, 85, 140),
            ('Spoink', 60, 25, 35),
            ('Grumpig', 80, 45, 65),
            ('Spinda', 60, 60, 60),
            ('Trapinch', 45, 100, 45),
            ('Vibrava', 50, 70, 50),
            ('Flygon', 80, 100, 80),
            ('Cacnea', 50, 85, 40),
            ('Cacturne', 70, 115, 60),
            ('Swablu', 45, 40, 60),
            ('Altaria', 75, 70, 90),
            ('Zangoose', 73, 115, 60),
            ('Seviper', 73, 100, 60),
            ('Lunatone', 70, 55, 65),
            ('Solrock', 70, 95, 85),
            ('Barboach', 50, 48, 43),
            ('Whiscash', 110, 78, 73),
            ('Corphish', 43, 80, 65),
            ('Crawdaunt', 63, 120, 85),
            ('Baltoy', 40, 40, 55),
            ('Claydol', 60, 70, 105),
            ('Lileep', 66, 41, 77),
            ('Cradily', 86, 81, 97),
            ('Anorith', 45, 95, 50),
            ('Armaldo', 75, 125, 100),
            ('Feebas', 20, 15, 20),
            ('Milotic', 95, 60, 79),
            ('Castform', 70, 70, 70),
            ('Kecleon', 60, 90, 70),
            ('Shuppet', 44, 75, 35),
            ('Banette', 64, 115, 65),
            ('Duskull', 20, 40, 90),
            ('Dusclops', 40, 70, 130),
            ('Tropius', 99, 68, 83),
            ('Chimecho', 65, 50, 70),
            ('Absol', 65, 130, 60),
            ('Wynaut', 95, 23, 48),
            ('Snorunt', 50, 50, 50),
            ('Glalie', 80, 80, 80),
            ('Spheal', 70, 40, 50),
            ('Sealeo', 90, 60, 70),
            ('Walrein', 110, 80, 90),
            ('Clamperl', 35, 64, 85),
            ('Huntail', 55, 104, 105),
            ('Gorebyss', 55, 84, 105),
            ('Relicanth', 100, 90, 130),
            ('Luvdisc', 43, 30, 55),
            ('Bagon', 45, 75, 60),
            ('Shelgon', 65, 95, 100),
            ('Salamence', 95, 135, 80),
            ('Beldum', 40, 55, 80),
            ('Metang', 60, 75, 100),
            ('Metagross', 80, 135, 130),
            ('Regirock', 80, 100, 200),
            ('Regice', 80, 50, 100),
            ('Registeel', 80, 75, 150),
            ('Latias', 80, 80, 90),
            ('Latios', 80, 90, 80),
            ('Kyogre', 100, 100, 90),
            ('Groudon', 100, 150, 140),
            ('Rayquaza', 105, 150, 90),
            ('Jirachi', 100, 100, 100),
            ('Deoxys (N)', 50, 150, 50),
            ('Deoxys (A)', 50, 180, 20),
            ('Deoxys (D)', 50, 70, 160),
            ('Deoxys (S)', 50, 95, 90),
            ('Turtwig', 55, 68, 64),
            ('Grotle', 75, 89, 85),
            ('Torterra', 95, 109, 105),
            ('Chimchar', 44, 58, 44),
            ('Monferno', 64, 78, 52),
            ('Infernape', 76, 104, 71),
            ('Piplup', 53, 51, 53),
            ('Prinplup', 64, 66, 68),
            ('Empoleon', 84, 86, 88),
            ('Starly', 40, 55, 30),
            ('Staravia', 55, 75, 50),
            ('Staraptor', 85, 120, 70),
            ('Bidoof', 59, 45, 40),
            ('Bibarel', 79, 85, 60),
            ('Kricketot', 37, 25, 41),
            ('Kricketune', 77, 85, 51),
            ('Shinx', 45, 65, 34),
            ('Luxio', 60, 85, 49),
            ('Luxray', 80, 120, 79),
            ('Budew', 40, 30, 35),
            ('Roserade', 60, 70, 55),
            ('Cranidos', 67, 125, 40),
            ('Rampardos', 97, 165, 60),
            ('Shieldon', 30, 42, 118),
            ('Bastiodon', 60, 52, 168),
            ('Burmy', 40, 29, 45),
            ('Wormadam (P)', 60, 59, 85),
            ('Wormadam (S)', 60, 79, 105),
            ('Wormadam (T)', 60, 69, 95),
            ('Mothim', 70, 94, 50),
            ('Combee', 30, 30, 42),
            ('Vespiquen', 70, 80, 102),
            ('Pachirisu', 60, 45, 70),
            ('Buizel', 55, 65, 35),
            ('Floatzel', 85, 105, 55),
            ('Cherubi', 45, 35, 45),
            ('Cherrim', 70, 60, 70),
            ('Shellos', 76, 48, 48),
            ('Gastrodon', 111, 83, 68),
            ('Ambipom', 75, 100, 66),
            ('Drifloon', 90, 50, 34),
            ('Drifblim', 150, 80, 44),
            ('Buneary', 55, 66, 44),
            ('Lopunny', 65, 76, 84),
            ('Mismagius', 60, 60, 60),
            ('Honchkrow', 100, 125, 52),
            ('Glameow', 49, 55, 42),
            ('Purugly', 71, 82, 64),
            ('Chingling', 45, 30, 50),
            ('Stunky', 63, 63, 47),
            ('Skuntank', 103, 93, 67),
            ('Bronzor', 57, 24, 86),
            ('Bronzong', 67, 89, 116),
            ('Bonsly', 50, 80, 95),
            ('Mime Jr.', 20, 25, 45),
            ('Happiny', 100, 5, 5),
            ('Chatot', 76, 65, 45),
            ('Spiritomb', 50, 92, 108),
            ('Gible', 58, 70, 45),
            ('Gabite', 68, 90, 65),
            ('Garchomp', 108, 130, 95),
            ('Munchlax', 135, 85, 40),
            ('Riolu', 40, 70, 40),
            ('Lucario', 70, 110, 70),
            ('Hippopotas', 68, 72, 78),
            ('Hippowdon', 108, 112, 118),
            ('Skorupi', 40, 50, 90),
            ('Drapion', 70, 90, 110),
            ('Croagunk', 48, 61, 40),
            ('Toxicroak', 83, 106, 65),
            ('Carnivine', 74, 100, 72),
            ('Finneon', 49, 49, 56),
            ('Lumineon', 69, 69, 76),
            ('Mantyke', 45, 20, 50),
            ('Snover', 60, 62, 50),
            ('Abomasnow', 90, 92, 75),
            ('Weavile', 70, 120, 65),
            ('Magnezone', 70, 70, 115),
            ('Lickilicky', 110, 85, 95),
            ('Rhyperior', 115, 140, 130),
            ('Tangrowth', 100, 100, 125),
            ('Electivire', 75, 123, 67),
            ('Magmortar', 75, 95, 67),
            ('Togekiss', 85, 50, 95),
            ('Yanmega', 86, 76, 86),
            ('Leafeon', 65, 110, 130),
            ('Glaceon', 65, 60, 110),
            ('Gliscor', 75, 95, 125),
            ('Mamoswine', 110, 130, 80),
            ('Porygon-Z', 85, 80, 70),
            ('Gallade', 68, 125, 65),
            ('Probopass', 60, 55, 145),
            ('Dusknoir', 45, 100, 135),
            ('Froslass', 70, 80, 70),
            ('Rotom', 50, 50, 77),
            ('Rotom (Heat)', 50, 65, 107),
            ('Rotom (Wash)', 50, 65, 107),
            ('Rotom (Frost)', 50, 65, 107),
            ('Rotom (Spin)', 50, 65, 107),
            ('Rotom (Cut)', 50, 65, 107),
            ('Uxie', 75, 75, 130),
            ('Mesprit', 80, 105, 105),
            ('Azelf', 75, 125, 70),
            ('Dialga', 100, 120, 120),
            ('Palkia', 90, 120, 100),
            ('Heatran', 91, 90, 106),
            ('Regigigas', 110, 160, 110),
            ('Giratina', 150, 100, 120),
            ('Giratina (O)', 150, 120, 100),
            ('Cresselia', 120, 70, 120),
            ('Phione', 80, 80, 80),
            ('Manaphy', 100, 100, 100),
            ('Darkrai', 70, 90, 90),
            ('Shaymin', 100, 100, 100),
            ('Shaymin (S)', 100, 103, 75),
            ('Arceus', 120, 120, 120),
            ('Victini', 100, 100, 100),
            ('Snivy', 45, 45, 55),
            ('Servine', 60, 60, 75),
            ('Serperior', 75, 75, 95),
            ('Tepig', 65, 63, 45),
            ('Pignite', 90, 93, 55),
            ('Emboar', 110, 123, 65),
            ('Oshawott', 55, 55, 45),
            ('Dewott', 75, 75, 60),
            ('Samurott', 95, 100, 85),
            ('Patrat', 45, 55, 39),
            ('Watchog', 60, 85, 69),
            ('Lillipup', 45, 60, 45),
            ('Herdier', 65, 80, 65),
            ('Stoutland', 85, 100, 90),
            ('Purrloin', 41, 50, 37),
            ('Liepard', 64, 88, 50),
            ('Pansage', 50, 53, 48),
            ('Simisage', 75, 98, 63),
            ('Pansear', 50, 53, 48),
            ('Simisear', 75, 98, 63),
            ('Panpour', 50, 53, 48),
            ('Simipour', 75, 98, 63),
            ('Munna', 76, 25, 45),
            ('Musharna', 116, 55, 85),
            ('Pidove', 50, 55, 50),
            ('Tranquill', 62, 77, 62),
            ('Unfezant', 80, 105, 80),
            ('Blitzle', 45, 60, 32),
            ('Zebstrika', 75, 100, 63),
            ('Roggenrola', 55, 75, 85),
            ('Boldore', 70, 105, 105),
            ('Gigalith', 85, 135, 130),
            ('Woobat', 55, 45, 43),
            ('Swoobat', 67, 57, 55),
            ('Drilbur', 60, 85, 40),
            ('Excadrill', 110, 135, 60),
            ('Audino', 103, 60, 86),
            ('Timburr', 75, 80, 55),
            ('Gurdurr', 85, 105, 85),
            ('Conkeldurr', 105, 140, 95),
            ('Tympole', 50, 50, 40),
            ('Palpitoad', 75, 65, 55),
            ('Seismitoad', 105, 85, 75),
            ('Throh', 120, 100, 85),
            ('Sawk', 75, 125, 75),
            ('Sewaddle', 45, 53, 70),
            ('Swadloon', 55, 63, 90),
            ('Leavanny', 75, 103, 80),
            ('Venipede', 30, 45, 59),
            ('Whirlipede', 40, 55, 99),
            ('Scolipede', 60, 90, 89),
            ('Cottonee', 40, 27, 60),
            ('Whimsicott', 60, 67, 85),
            ('Petilil', 45, 35, 50),
            ('Lilligant', 70, 60, 75),
            ('Basculin', 70, 92, 65),
            ('Sandile', 50, 72, 35),
            ('Krokorok', 60, 82, 45),
            ('Krookodile', 95, 117, 70),
            ('Darumaka', 70, 90, 45),
            ('Darmanitan', 105, 140, 55),
            ('Darmanitan (Z)', 105, 30, 105),
            ('Maractus', 75, 86, 67),
            ('Dwebble', 50, 65, 85),
            ('Crustle', 70, 95, 125),
            ('Scraggy', 50, 75, 70),
            ('Scrafty', 65, 90, 115),
            ('Sigilyph', 72, 58, 80),
            ('Yamask', 38, 30, 85),
            ('Cofagrigus', 58, 50, 145),
            ('Tirtouga', 54, 78, 103),
            ('Carracosta', 74, 108, 133),
            ('Archen', 55, 112, 45),
            ('Archeops', 75, 140, 65),
            ('Trubbish', 50, 50, 62),
            ('Garbodor', 80, 95, 92),
            ('Zorua', 40, 65, 40),
            ('Zoroark', 60, 105, 60),
            ('Minccino', 55, 50, 40),
            ('Cinccino', 75, 95, 60),
            ('Gothita', 45, 30, 50),
            ('Gothorita', 60, 45, 70),
            ('Gothitelle', 70, 55, 95),
            ('Solosis', 45, 30, 40),
            ('Duosion', 65, 40, 50),
            ('Reuniclus', 110, 65, 75),
            ('Ducklett', 62, 44, 50),
            ('Swanna', 75, 87, 63),
            ('Vanillite', 36, 50, 50),
            ('Vanillish', 51, 65, 65),
            ('Vanilluxe', 71, 95, 85),
            ('Deerling', 60, 60, 50),
            ('Sawsbuck', 80, 100, 70),
            ('Emolga', 55, 75, 60),
            ('Karrablast', 50, 75, 45),
            ('Escavalier', 70, 135, 105),
            ('Foongus', 69, 55, 45),
            ('Amoonguss', 114, 85, 70),
            ('Frillish', 55, 40, 50),
            ('Jellicent', 100, 60, 70),
            ('Alomomola', 165, 75, 80),
            ('Joltik', 50, 47, 50),
            ('Galvantula', 70, 77, 60),
            ('Ferroseed', 44, 50, 91),
            ('Ferrothorn', 74, 94, 131),
            ('Klink', 40, 55, 70),
            ('Klang', 60, 80, 95),
            ('Klinklang', 60, 100, 115),
            ('Tynamo', 35, 55, 40),
            ('Eelektrik', 65, 85, 70),
            ('Eelektross', 85, 115, 80),
            ('Elgyem', 55, 55, 55),
            ('Beheeyem', 75, 75, 75),
            ('Litwick', 50, 30, 55),
            ('Lampent', 60, 40, 60),
            ('Chandelure', 60, 55, 90),
            ('Axew', 46, 87, 60),
            ('Fraxure', 66, 117, 70),
            ('Haxorus', 76, 147, 90),
            ('Cubchoo', 55, 70, 40),
            ('Beartic', 95, 110, 80),
            ('Cryogonal', 70, 50, 30),
            ('Shelmet', 50, 40, 85),
            ('Accelgor', 80, 70, 40),
            ('Stunfisk', 109, 66, 84),
            ('Mienfoo', 45, 85, 50),
            ('Mienshao', 65, 125, 60),
            ('Druddigon', 77, 120, 90),
            ('Golett', 59, 74, 50),
            ('Golurk', 89, 124, 80),
            ('Pawniard', 45, 85, 70),
            ('Bisharp', 65, 125, 100),
            ('Bouffalant', 95, 110, 95),
            ('Rufflet', 70, 83, 50),
            ('Braviary', 100, 123, 75),
            ('Vullaby', 70, 55, 75),
            ('Mandibuzz', 110, 65, 105),
            ('Heatmor', 85, 97, 66),
            ('Durant', 58, 109, 112),
            ('Deino', 52, 65, 50),
            ('Zweilous', 72, 85, 70),
            ('Hydreigon', 92, 105, 90),
            ('Larvesta', 55, 85, 55),
            ('Volcarona', 85, 60, 65),
            ('Cobalion', 91, 90, 129),
            ('Terrakion', 91, 129, 90),
            ('Virizion', 91, 90, 72),
            ('Tornadus', 79, 115, 70),
            ('Thundurus', 79, 115, 70),
            ('Reshiram', 100, 120, 100),
            ('Zekrom', 100, 150, 120),
            ('Landorus', 89, 125, 90),
            ('Kyurem', 125, 130, 90),
            ('Keldeo', 91, 72, 90))


def get_name(pokemon_tuple):
    return pokemon_tuple[0]


def get_attack(pokemon_tuple):
    return pokemon_tuple[1]


def get_defend(pokemon_tuple):
    return pokemon_tuple[2]


def get_health(pokemon_tuple):
    return pokemon_tuple[3]


def get_overall(pokemon_tuple):
    return pokemon_tuple[1] + pokemon_tuple[2] + pokemon_tuple[3]


def on_sort_by_overall():
    sorted_pokemons = sorted(pokemons, key=get_overall, reverse=True)
    list_sort_by_overall.delete(0, 'end')
    for pokemon in sorted_pokemons:
        list_sort_by_overall.insert(tkinter.END, f'{get_name(pokemon)} Overall: {get_overall(pokemon)}')


def on_sort_by_attack():
    sorted_pokemons = sorted(pokemons, key=get_attack, reverse=True)
    list_sort_by_attack.delete(0, 'end')
    for pokemon in sorted_pokemons:
        list_sort_by_attack.insert(tkinter.END, f'{get_name(pokemon)} Attack: {get_attack(pokemon)}')


def on_sort_by_defense():
    sorted_pokemons = sorted(pokemons, key=get_defend, reverse=True)
    list_sort_by_defend.delete(0, 'end')
    for pokemon in sorted_pokemons:
        list_sort_by_defend.insert(tkinter.END, f'{get_name(pokemon)} Defend: {get_defend(pokemon)}')


def on_sort_by_health():
    sorted_pokemons = sorted(pokemons, key=get_health, reverse=True)
    list_sort_by_health.delete(0, 'end')
    for pokemon in sorted_pokemons:
        list_sort_by_health.insert(tkinter.END, f'{get_name(pokemon)} Health: {get_health(pokemon)}')


def on_sort_by_name():
    sorted_pokemons = sorted(pokemons, key=get_name)
    list_sort_by_name.delete(0, 'end')
    for pokemon in sorted_pokemons:
        list_sort_by_name.insert(tkinter.END, get_name(pokemon))


window = tkinter.Tk()
window.title('Pokemon ranking')
window.geometry('1200x800')
window.config(background='SlateGray2')

button_section = tkinter.Frame(window, background='SlateGray2', height=100)
button_section.pack(side='top', pady=10)

button_sort_by_name = tkinter.Button(button_section, text='Sort by Name', height=2)
button_sort_by_name.pack(side='left', padx=10)
button_sort_by_name['command'] = on_sort_by_name

button_sort_by_attack = tkinter.Button(button_section, text='Sort by Attack', height=2)
button_sort_by_attack.pack(side='left', padx=10)
button_sort_by_attack['command'] = on_sort_by_attack

button_sort_by_defend = tkinter.Button(button_section, text='Sort by Defend', height=2)
button_sort_by_defend.pack(side='left', padx=10)
button_sort_by_defend['command'] = on_sort_by_defense

button_sort_by_health = tkinter.Button(button_section, text='Sort by Health', height=2)
button_sort_by_health.pack(side='left', padx=10)
button_sort_by_health['command'] = on_sort_by_health

button_sort_by_overall = tkinter.Button(button_section, text='Sort by Overall', height=2)
button_sort_by_overall.pack(side='left', padx=10)
button_sort_by_overall['command'] = on_sort_by_overall

sort_section = tkinter.Frame(window, background='SlateGray2')
sort_section.pack(side='bottom', fill='both', expand=True, padx=10, pady=5)

list_origin = tkinter.Listbox(sort_section)
list_origin.pack(side='left', fill='both', expand=True, padx=5)

list_sort_by_name = tkinter.Listbox(sort_section, width=20)
list_sort_by_name.pack(side='left', fill='y', padx=5)

list_sort_by_attack = tkinter.Listbox(sort_section, width=20)
list_sort_by_attack.pack(side='left', fill='y', padx=5)

list_sort_by_defend = tkinter.Listbox(sort_section, width=20)
list_sort_by_defend.pack(side='left', fill='y', padx=5)

list_sort_by_health = tkinter.Listbox(sort_section, width=20)
list_sort_by_health.pack(side='left', fill='y', padx=5)

list_sort_by_overall = tkinter.Listbox(sort_section, width=20)
list_sort_by_overall.pack(side='left', fill='y', padx=5)

for pokemon in pokemons:
    list_origin.insert(tkinter.END, f'{get_name(pokemon)} Attact: {get_attack(pokemon)} Defend: {get_defend(pokemon)} Health: {get_health(pokemon)}')

tkinter.mainloop()