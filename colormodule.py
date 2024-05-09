def coloredobject(video_path,cls,color_name,cnfd):
    import pandas as pd
    #from sklearn.cluster import KMeans
    import numpy as np
    
    def timeformat(seconds):

        hr=int(seconds/3600)
        r=seconds-(hr*3600)
        min=int(r/60)
        sec=r%60
        time=str(hr)+':'+str(min)+':'+str(sec)
        return (time)
    
    base_colors = {
    "Air Force Blue (Raf)": "Blue",
    "Air Force Blue (Usaf)": "Blue",
    "Air Superiority Blue": "Blue",
    "Alabama Crimson": "Red",
    "Alice Blue": "Light Blue",
    "Alizarin Crimson": "Red",
    "Alloy Orange": "Orange",
    "Almond": "Beige",
    "Amaranth": "Red",
    "Amber": "Gold",
    "Amber (Sae/Ece)": "Gold",
    "American Rose": "Pink",
    "Amethyst": "Violet",
    "Android Green": "Green",
    "Anti-Flash White": "White",
    "Antique Brass": "Gold",
    "Antique Fuchsia": "Pink",
    "Antique Ruby": "Red",
    "Antique White": "White",
    "Ao (English)": "Blue",  # Assuming it refers to a shade of blue
    "Apple Green": "Green",
    "Apricot": "Orange",
    "Aqua": "Blue",
    "Aquamarine": "Blue",
    "Army Green": "Green",
    "Arsenic": "Grey",  # Arsenic can have a metallic sheen
    "Arylide Yellow": "Yellow",
    "Ash Grey": "Grey",
    "Asparagus": "Green",
    "Atomic Tangerine": "Orange",
    "Auburn": "Brown",
    "Aureolin": "Yellow",
    "Aurometalsaurus": "Grey",  # Assuming it's a metallic grey
    "Avocado": "Green",
    "Azure": "Blue",
    "Azure Mist/Web": "Blue",
    "Baby Blue": "Blue",
    "Baby Blue Eyes": "Blue",
    "Baby Pink": "Pink",
    "Ball Blue": "Blue",
    "Banana Mania": "Yellow",
    "Banana Yellow": "Yellow",
    "Barn Red": "Red",
    "Battleship Grey": "Grey",
    "Bazaar": "Brown",  # Can also be a mix of colors depending on context
    "Beau Blue": "Blue",
    "Beaver": "Brown",
    "Beige": "Beige",
    "Big Dip O’Ruby": "Red",
    "Bisque": "Beige",
    "Bistre": "Brown",
    "Bittersweet": "Red",  # Can also be a brownish red, keep as red here
    "Bittersweet Shimmer": "Red",  # Can also be a brownish red with shimmer, keep as red here
    "Black": "Black",
    "Black Bean": "Black",
    "Black Leather Jacket": "Black",
    "Black Olive": "Black",  # Can also be a dark green, choose black here
    "Blanched Almond": "Beige",
    "Blast-Off Bronze": "Bronze",
    "Bleu De France": "Blue",
    "Blizzard Blue": "White",  # Assuming it's a very light blue
    "Blond": "Beige",  # Can also be light brown, choose beige here
    "Blue": "Blue",
    "Blue Bell": "Blue",  # Can be Light Blue, keep as Blue here
    "Blue (Crayola)": "Blue",
    "Blue Gray": "Grey",  # Can also be a blueish grey, choose grey here
    "Blue-Green": "Blue",  # Choose based on the dominant color, unclear here, omit
    "Blue (Munsell)": "Blue",
    "Blue (Ncs)": "Blue",
    "Blue (Pigment)": "Blue",
    "Blue (Ryb)": "Blue",
    "Blue Sapphire": "Blue",
    "Blue-Violet": "Violet",
    "Blush": "Pink",
    "Bole": "Brown",
    "Bondi Blue": "Blue",
    "Bone": "Beige",
    "Boston University Red": "Red",
    "Bottle Green": "Green",
    "Boysenberry": "Purple",
    "Brandeis Blue": "Blue",
    "Brass": "Gold",
    "Brick Red": "Red",
    "Bright Cerulean": "Blue",
    "Bright Green": "Green",
    "Bright Lavender": "Purple",
    "Bright Maroon": "Red",
    "Bright Pink": "Pink",
    "Bright Turquoise": "Blue" or "Green",  # Omit due to ambiguity
    "Bright Ube": "Purple",
    "Brilliant Lavender": "Purple",
    "Brilliant Rose": "Pink",
    "Brink Pink": "Pink",
    "British Racing Green": "Green",
    "Bronze": "Bronze",
    "Brown (Traditional)": "Brown",
    "Brown (Web)": "Brown",
    "Bubble Gum": "Pink",  # Can be a light pink, choose pink here
    "Bubbles": "White",  # Assuming bubbles are transparent with a white reflection
    "Buff": "Beige",  # Assuming Buff refers to a light yellowish brown
    "Bulgarian Rose": "Red",
    "Burgundy": "Red",  # Can also be a brownish red
    "Burlywood": "Beige",
    "Burnt Orange": "Orange",
    "Burnt Sienna": "Brown",  # Reddish brown
    "Burnt Umber": "Brown",  # Dark brown with a reddish tinge
    "Byzantine": "Purple",  # Can also be a dark reddish purple
    "Byzantium": "Purple",  # Can also be a dark reddish purple (same as Byzantine)
    "Cadet": "Grey",  # Can also be a greenish grey
    "Cadet Blue": "Blue",  # Can also be a greyish blue
    "Cadet Grey": "Grey",
    "Cadmium Green": "Green",
    "Cadmium Orange": "Orange",
    "Cadmium Red": "Red",
    "Cadmium Yellow": "Yellow",
    "Café Au Lait": "Beige",  # Light brown with a hint of yellow
    "Café Noir": "Black",  # Literally translates to "black coffee"
    "Cal Poly Green": "Green",
    "Cambridge Blue": "Blue",
    "Camel": "Brown",  # Light to medium brown
    "Cameo Pink": "Pink",  # Light pink
    "Camouflage Green": "Green",  # Can vary depending on the type of camouflage
    "Canary Yellow": "Yellow",  # Bright yellow
    "Candy Apple Red": "Red",  # Bright, slightly transparent red
    "Candy Pink": "Pink",  # Bright pink
    "Capri": "Blue",  # Light shade of blue
    "Caput Mortuum": "Brown",  # Literally translates to "dead head", a reddish brown pigment
    "Cardinal": "Red",  # Deep, rich red
    "Caribbean Green": "Green",  # Can vary depending on the specific shade
    "Carmine": "Red",  # Deep, vivid red
    "Carmine (M&P)": "Red",  # Similar to Carmine
    "Carmine Pink": "Pink",  # Pinkish red
    "Carmine Red": "Red",  # Similar to Carmine
    "Carnation Pink": "Pink",  # Light pink
    "Carnelian": "Red",  # Reddish orange
    "Carolina Blue": "Blue",  # Light shade of blue
    "Carrot Orange": "Orange",  # Bright orange
    "Catalina Blue": "Blue",  # Bright, turquoise blue
    "Ceil": "Blue",  # Can refer to various shades of blue depending on context
    "Celadon": "Green",  # Pale green with a hint of blue
    "Celadon Blue": "Blue",  # Light blue with a greenish tinge
    "Celadon Green": "Green",  # Similar to Celadon
    "Celeste (Colour)": "Blue",  # Light blue
    "Celestial Blue": "Blue",  # Light to medium blue
    "Cerise": "Pink",  # Bright cherry red or pink
    "Cerise Pink": "Pink",  # Similar to Cerise
    "Cerulean": "Blue",  # Clear, bright blue
    "Cerulean Blue": "Blue",  # Similar to Cerulean
    "Cerulean Frost": "Blue",
    "Cg Blue": "Blue",
    "Cg Red": "Red",
    "Chamoisee": "Beige",  # Assuming a light tan/yellow color
    "Champagne": "Beige",  # Can also be a light yellow depending on shade
    "Charcoal": "Grey",
    "Charm Pink": "Pink",
    "Chartreuse (Traditional)": "Yellow",  # Leans more towards yellow
    "Chartreuse (Web)": "Green",  # Leans more towards green
    "Cherry": "Red",
    "Cherry Blossom Pink": "Pink",
    "Chestnut": "Brown",
    "China Pink": "Pink",
    "China Rose": "Pink",
    "Chinese Red": "Red",
    "Chocolate (Traditional)": "Brown",
    "Chocolate (Web)": "Brown",
    "Chrome Yellow": "Yellow",
    "Cinereous": "Grey",  # Ash grey
    "Cinnabar": "Red",  # Bright red with an orange hue
    "Cinnamon": "Brown",  # Can also be a reddish brown
    "Citrine": "Yellow",  # Can also be a yellowish orange
    "Classic Rose": "Pink",
    "Cobalt": "Blue",  # Deep blue
    "Cocoa Brown": "Brown",
    "Coffee": "Brown",
    "Columbia Blue": "Blue",
    "Congo Pink": "Pink",
    "Cool Black": "Black",
    "Cool Grey": "Grey",
    "Copper": "Brown",  # Can also be a reddish brown
    "Copper (Crayola)": "Orange",  # More on the orange side
    "Copper Penny": "Brown",  # Can also be a reddish brown
    "Copper Red": "Red",  # Reddish copper
    "Copper Rose": "Pink",  # Rose with a copper tint
    "Coquelicot": "Red",  # Bright poppy red
    "Coral": "Orange",  # Pinkish-orange
    "Coral Pink": "Pink",
    "Coral Red": "Red",  # Reddish coral
    "Cordovan": "Brown",  # Deep reddish brown
    "Corn": "Yellow",  # Can also be a light orange
    "Cornell Red": "Red",
    "Cornflower Blue": "Blue",
    "Cornsilk": "Beige",  # Very light yellow
    "Cosmic Latte": "Beige",  # Light creamy brown
    "Cotton Candy": "Pink",  # Light pink
    "Cream": "Beige",
    "Crimson": "Red",
    "Crimson Glory": "Red",
    "Cyan": "Blue",  # Light blue-green
    "Cyan (Process)": "Blue",  # Light blue-green
    "Daffodil": "Yellow",  # Assuming a yellow flower color
    "Dandelion": "Yellow",  # Another shade of yellow
    "Dark Blue": "Blue",
    "Dark Brown": "Brown",
    "Dark Byzantium": "Purple",  # Can also be a dark blue-ish purple
    "Dark Candy Apple Red": "Red",
    "Dark Cerulean": "Blue",
    "Dark Chestnut": "Brown",
    "Dark Coral": "Orange",  # Can also be a reddish orange
    "Dark Cyan": "Blue",  # Can also be a greenish blue depending on shade
    "Dark Electric Blue": "Blue",
    "Dark Goldenrod": "Yellow",  # Can also be a brownish yellow
    "Dark Gray": "Grey",
    "Dark Green": "Green",
    "Dark Imperial Blue": "Blue",
    "Dark Jungle Green": "Green",
    "Dark Khaki": "Beige",  # Can also be a brownish yellow
    "Dark Lava": "Grey",  # Can also be a dark red depending on shade
    "Dark Lavender": "Purple",
    "Dark Magenta": "Purple",
    "Dark Midnight Blue": "Blue",
    "Dark Olive Green": "Green",
    "Dark Orange": "Orange",
    "Dark Orchid": "Purple",
    "Dark Pastel Blue": "Blue",  # Assuming a pastel shade of blue
    "Dark Pastel Green": "Green",  # Can also be a light green
    "Dark Pastel Purple": "Purple",  # Assuming a pastel shade of purple
    "Dark Pastel Red": "Red",  # Assuming a pastel shade of red
    "Dark Pink": "Pink",
    "Dark Powder Blue": "Blue",  # Can also be a light blue depending on shade
    "Dark Raspberry": "Red",  # Can also be a purplish red
    "Dark Red": "Red",
    "Dark Salmon": "Pink",  # Can also be a light orange depending on shade
    "Dark Scarlet": "Red",
    "Dark Sea Green": "Green",  # Can also be a blueish green depending on shade
    "Dark Sienna": "Brown",
    "Dark Slate Blue": "Blue",
    "Dark Slate Gray": "Grey",
    "Dark Spring Green": "Green",
    "Dark Tan": "Beige",  # Can also be a light brown
    "Dark Tangerine": "Orange",
    "Dark Taupe": "Brown",  # Can also be a greyish brown
    "Dark Terra Cotta": "Brown",  # Can also be a reddish brown
    "Dark Turquoise": "Blue",  # Can also be a greenish blue depending on shade
    "Dark Violet": "Purple",
    "Dark Yellow": "Yellow",
    "Dartmouth Green": "Green",
    "Davy'S Grey": "Grey",
    "Debian Red": "Red",
    "Deep Carmine": "Red",
    "Deep Carmine Pink": "Pink",
    "Deep Carrot Orange": "Orange",
    "Deep Cerise": "Pink",  # Leaning towards red based on typical shades
    "Deep Champagne": "Gold",  # Can also be a beige depending on the shade
    "Deep Chestnut": "Brown",
    "Deep Coffee": "Brown",
    "Deep Fuchsia": "Pink",  # Can also be a purple depending on the shade
    "Deep Jungle Green": "Green",
    "Deep Lilac": "Purple",
    "Deep Magenta": "Purple",
    "Deep Peach": "Orange",  # Can also be a pink depending on the shade
    "Deep Pink": "Pink",
    "Deep Ruby": "Red",
    "Deep Saffron": "Gold",  # Yellow is a possibility depending on the shade
    "Deep Sky Blue": "Blue",
    "Deep Tuscan Red": "Red",
    "Denim": "Blue",  # Can also be a grey depending on the wash
    "Desert": "Brown",  # Can also be a beige, yellow, or orange depending on the specific desert
    "Desert Sand": "Beige",
    "Dim Gray": "Grey",
    "Dodger Blue": "Blue",
    "Dogwood Rose": "Pink",
    "Dollar Bill": "Green",  # Can also be a beige depending on the wear
    "Drab": "Brown",  # Can also be a grey depending on the shade
    "Duke Blue": "Blue",
    "Earth Yellow": "Yellow",
    "Ebony": "Black",
    "Ecru": "Beige",
    "Eggplant": "Purple",  # Can also be a black depending on the shade
    "Eggshell": "White",
    "Egyptian Blue": "Blue",  # Can also be a turquoise depending on the composition
    "Electric Blue": "Blue",
    "Electric Crimson": "Red",
    "Electric Cyan": "Blue",  # Depending on the shade
    "Electric Green": "Green",
    "Electric Indigo": "Indigo",
    "Electric Lavender": "Purple",
    "Electric Lime": "Green",
    "Electric Purple": "Purple",
    "Electric Ultramarine": "Blue",
    "Electric Violet": "Violet",
    "Electric Yellow": "Yellow",
    "Emerald": "Green",
    "English Lavender": "Purple",
    "Eton Blue": "Blue",
    "Fallow": "Brown",  # Can also be a beige depending on the context
    "Falu Red": "Red",
    "Fandango": "Red",  # Can also be an orange depending on the shade
    "Fashion Fuchsia": "Pink",
    "Fawn": "Beige",
    "Feldgrau": "Grey",  # Assuming it's a shade of grey
    "Fern Green": "Green",
    "Ferrari Red": "Red",
    "Field Drab": "Brown",  # Can also be a greenish brown
    "Fire Engine Red": "Red",
    "Firebrick": "Red",  # Can also be a brownish red
    "Flame": "Orange",  # Can also be red or yellow depending on shade
    "Flamingo Pink": "Pink",
    "Flavescent": "Yellow",  # Can also be a greenish yellow
    "Flax": "Beige",  # Can also be light brown
    "Floral White": "White",
    "Fluorescent Orange": "Orange",
    "Fluorescent Pink": "Pink",
    "Fluorescent Yellow": "Yellow",
    "Folly": "Red",  # Can also be a pinkish red
    "Forest Green (Traditional)": "Green",
    "Forest Green (Web)": "Green",
    "French Beige": "Beige",
    "French Blue": "Blue",
    "French Lilac": "Purple",  # Can also be a light purple
    "French Lime": "Green",  # Can also be a yellowish green
    "French Raspberry": "Pink",  # Can also be a red or purple depending on shade
    "French Rose": "Pink",
    "Fuchsia": "Pink",
    "Fuchsia (Crayola)": "Pink",
    "Fuchsia Pink": "Pink",
    "Fuchsia Rose": "Pink",
    "Fulvous": "Brown",  # Can also be a yellowish brown
    "Fuzzy Wuzzy": "Black",  # Assuming it refers to a very dark color
    "Gainsboro": "Grey",
    "Gamboge": "Yellow",
    "Ghost White": "White",
    "Ginger": "Brown",  # Can also be a yellowish brown
    "Glaucous": "Grey",  # Can also be a blueish grey or greenish grey
    "Glitter": "Silver",  # Glitter reflects the base color
    "Gold (Metallic)": "Gold",
    "Gold (Web) (Golden)": "Gold",
    "Golden Brown": "Brown",
    "Golden Poppy": "Orange",
    "Golden Yellow": "Yellow",
    "Goldenrod": "Yellow",
    "Granny Smith Apple": "Green",
    "Gray": "Grey",  # Alternate spelling of Grey
    "Gray-Asparagus": "Grey",  # Assuming it's a greyish green
    "Gray (Html/Css Gray)": "Grey",
    "Gray (X11 Gray)": "Grey",
    "Green (Color Wheel) (X11 Green)": "Green",
    "Green (Crayola)": "Green",
    "Green (Html/Css Green)": "Green",
    "Green (Munsell)": "Green",
    "Green (Ncs)": "Green",  # Assuming it refers to a shade of green
    "Green (Pigment)": "Green",
    "Green (Ryb)": "Green",
    "Green-Yellow": "Green",  # Leaning towards yellow if green is mentioned
    "Grullo": "Grey",  # Can also be a brownish grey
    "Guppie Green": "Green",
    "Halayà úBe": "Purple",  # Assuming it's a shade of purple
    "Han Blue": "Blue",
    "Han Purple": "Purple",
    "Hansa Yellow": "Yellow",
    "Harlequin": "Multicolor",  # Mix of multiple colors
    "Harvard Crimson": "Red",
    "Harvest Gold": "Gold",
    "Heart Gold": "Gold",
    "Heliotrope": "Purple",  # Can also be a violet-red
    "Hollywood Cerise": "Pink",  # Can also be a bright red
    "Honeydew": "Beige",  # Light yellow-green
    "Honolulu Blue": "Blue",
    "Hooker'S Green": "Green",
    "Hot Magenta": "Pink",  # Magenta leans towards pink
    "Hot Pink": "Pink",
    "Hunter Green": "Green",
    "Iceberg": "White",  # Assuming it's a very light color
    "Icterine": "Yellow",
    "Imperial Blue": "Blue",
    "Inchworm": "Green",
    "India Green": "Green",
    "Indian Red": "Red",
    "Indian Yellow": "Yellow",
    "Indigo": "Purple",
    "Indigo (Dye)": "Purple",
    "Indigo (Web)": "Purple",
    "International Klein Blue": "Blue",
    "International Orange (Aerospace)": "Orange",
    "International Orange (Engineering)": "Orange",
    "International Orange (Golden Gate Bridge)": "Orange",
    "Iris": "Purple",  # Can also be blue or violet depending on the flower
    "Isabelline": "Beige",  # Can also be a light brown
    "Islamic Green": "Green",
    "Ivory": "Beige",
    "Jade": "Green",  # Can also have a blueish hue
    "Jasmine": "White",  # Assuming it refers to the white flower color
    "Jasper": "Multicolor",  # Jasper can have various colors
    "Jazzberry Jam": "Purple",
    "Jet": "Black",
    "Jonquil": "Yellow",
    "June Bud": "Green",
    "Jungle Green": "Green",
    "Kelly Green": "Green",
    "Kenyan Copper": "Brown",
    "Khaki (Html/Css) (Khaki)": "Beige",  # Assuming it's a light brown shade
    "Khaki (X11) (Light Khaki)": "Beige",
    "Ku Crimson": "Red",
    "La Salle Green": "Green",
    "Languid Lavender": "Purple",  # Can also be a light pinkish purple
    "Lapis Lazuli": "Blue",  # Can have a slight violet tint
    "Laser Lemon": "Yellow",
    "Laurel Green": "Green",
    "Lava": "Orange",  # Depending on the specific shade
    "Lavender Blue": "Blue",  # Depending on the shade
    "Lavender Blush": "Pink",
    "Lavender (Floral)": "Purple",
    "Lavender Gray": "Grey",  # Can also be a light purple depending on the shade
    "Lavender Indigo": "Purple",
    "Lavender Magenta": "Purple",
    "Lavender Mist": "Blue",  # Depending on the shade
    "Lavender Pink": "Pink",
    "Lavender Purple": "Purple",
    "Lavender Rose": "Pink",
    "Lavender (Web)": "Purple",
    "Lawn Green": "Green",
    "Lemon": "Yellow",
    "Lemon Chiffon": "Yellow",
    "Lemon Lime": "Yellow",  # Depending on the dominant color
    "Licorice": "Black",
    "Light Apricot": "Orange",  # Depending on the shade
    "Light Blue": "Blue",
    "Light Brown": "Brown",
    "Light Carmine Pink": "Pink",
    "Light Coral": "Orange",  # Depending on the shade
    "Light Cornflower Blue": "Blue",
    "Light Crimson": "Red",
    "Light Cyan": "Blue",
    "Light Fuchsia Pink": "Pink",
    "Light Goldenrod Yellow": "Yellow",
    "Light Gray": "Gray",
    "Light Green": "Green",
    "Light Khaki": "Beige",
    "Light Pastel Purple": "Purple",
    "Light Pink": "Pink",
    "Light Red Ochre": "Red",  # Depending on the shade
    "Light Salmon": "Pink",
    "Light Salmon Pink": "Pink",
    "Light Sea Green": "Green",
    "Light Sky Blue": "Blue",
    "Light Slate Gray": "Grey",
    "Light Taupe": "Grey",  # Depending on the shade
    "Light Thulian Pink": "Pink",
    "Light Yellow": "Yellow",
    "Lilac": "Purple",
    "Lime (Color Wheel)": "Green",  # Assuming it refers to a shade of green
    "Lime Green": "Green",
    "Lime (Web) (X11 Green)": "Green",
    "Limerick": "Green",  # Assuming it refers to a shade of green,  could also be a mix
    "Lincoln Green": "Green",
    "Linen": "Beige",  # Can also be a light brown depending on shade
    "Lion": "Brown",  # Refers to the fur color, can be various shades
    "Little Boy Blue": "Blue",  # Assuming it refers to a shade of blue
    "Liver": "Brown",  # Can also be a dark red depending on context
    "Lust": "Red",  # Can be interpreted in various ways, red is a common association
    "Magenta": "Pink",  # Although a primary color in subtractive mixing, consider it pink here
    "Magenta (Dye)": "Pink",
    "Magenta (Process)": "Pink",
    "Magic Mint": "Green",  # Assuming it refers to a shade of green
    "Magnolia": "White",  # Refers to the flower color
    "Mahogany": "Brown",
    "Maize": "Yellow",  # Refers to the corn color
    "Majorelle Blue": "Blue",
    "Malachite": "Green",  # Refers to the mineral color, a shade of green
    "Manatee": "Grey",  # Refers to the mammal's skin color
    "Mango Tango": "Orange",  # Refers to the fruit color
    "Mantis": "Green",  # Refers to the insect's body color, can be various shades
    "Mardi Gras": "Purple",  # Often associated with purple, yellow, and green
    "Maroon (Crayola)": "Red",  # A dark shade of red
    "Maroon (Html/Css)": "Red",  # A dark shade of red
    "Maroon (X11)": "Red",  # A dark shade of red
    "Mauve": "Purple",
    "Mauve Taupe": "Brown",  # A mix of brown and purple
    "Mauvelous": "Purple",
    "Maya Blue": "Blue",  # Refers to a historical pigment, specific shade unclear
    "Meat Brown": "Brown",
    "Medium Aquamarine": "Blue",  # A shade of blue leaning towards green
    "Medium Blue": "Blue",
    "Medium Candy Apple Red": "Red",  # A bright shade of red
    "Medium Carmine": "Red",  # A deep red
    "Medium Champagne": "Beige",  # A light yellow-ish beige
    "Medium Electric Blue": "Blue",  # A bright and vivid blue
    "Medium Jungle Green": "Green",  # A dark shade of green
    "Medium Lavender Magenta": "Purple",  # A mix of lavender and magenta
    "Medium Orchid": "Purple",  # A medium shade of orchid, a pinkish purple
    "Medium Persian Blue": "Blue",  # A turquoise-like blue
    "Medium Purple": "Purple",
    "Medium Red-Violet": "Purple",  # A red shade leaning towards purple
    "Medium Ruby": "Red",  # A deep red like a ruby gemstone
    "Medium Sea Green": "Green",  # A muted green with a blueish tinge
    "Medium Slate Blue": "Blue",  # A grayish blue
    "Medium Spring Bud": "Green",  # A light and fresh green
    "Medium Spring Green": "Green",  # A medium shade of green
    "Medium Taupe": "Brown",  # A grayish brown
    "Medium Turquoise": "Turquoise",
    "Medium Tuscan Red": "Red",
    "Medium Vermilion": "Red",
    "Medium Violet-Red": "Red",  # Can also be a purplish red
    "Mellow Apricot": "Orange",
    "Mellow Yellow": "Yellow",
    "Melon": "Orange",  # Can also be a pinkish orange
    "Midnight Blue": "Blue",
    "Midnight Green (Eagle Green)": "Green",
    "Mikado Yellow": "Yellow",
    "Mint": "Green",  # Can also be a light blue depending on shade
    "Mint Cream": "Beige",  # Can also be a light green depending on shade
    "Mint Green": "Green",
    "Misty Rose": "Pink",
    "Moccasin": "Beige",
    "Mode Beige": "Beige",
    "Moonstone Blue": "Blue",  # Can also be a gray depending on shade
    "Mordant Red 19": "Red",
    "Moss Green": "Green",
    "Mountain Meadow": "Green",  # Can also be a blue depending on shade
    "Mountbatten Pink": "Pink",
    "Msu Green": "Green",
    "Mulberry": "Purple",
    "Mustard": "Yellow",  # Can also be a brownish yellow
    "Myrtle": "Green",
    "Nadeshiko Pink": "Pink",
    "Napier Green": "Green",
    "Naples Yellow": "Yellow",
    "Navajo White": "White",  # Can also be a light beige depending on shade
    "Navy Blue": "Blue",
    "Neon Carrot": "Orange",
    "Neon Fuchsia": "Pink",
    "Neon Green": "Green",
    "New York Pink": "Pink",
    "Non-Photo Blue": "Blue",
    "North Texas Green": "Green",
    "Ocean Boat Blue": "Blue",
    "Ochre": "Yellow",  # Can also be a brown depending on shade
    "Office Green": "Green",
    "Old Gold": "Gold",
    "Old Lace": "Beige",
    "Old Lavender": "Purple",  # Can also be a light gray depending on shade
    "Old Mauve": "Purple",  # Can also be a brownish purple
    "Old Rose": "Pink",
    "Olive": "Green",
    "Olive Drab #7": "Green",
    "Olive Drab (Web) (Olive Drab #3)": "Green",
    "Olivine": "Green",  # Can also be a brownish green
    "Onyx": "Black",
    "Opera Mauve": "Purple",
    "Orange (Color Wheel)": "Orange",
    "Orange Peel": "Orange",  # Assuming it's a light shade of orange
    "Orange-Red": "Orange",  # Leans more towards red than pure orange
    "Orange (Ryb)": "Orange",
    "Orange (Web Color)": "Orange",
    "Orchid": "Purple",  # Can vary in shade, but often leans towards purple
    "Otter Brown": "Brown",
    "Ou Crimson Red": "Red",
    "Outer Space": "Black",  # Assuming it refers to a very dark blue or black
    "Outrageous Orange": "Orange",
    "Oxford Blue": "Blue",  # A dark shade of blue
    "Pakistan Green": "Green",
    "Palatinate Blue": "Blue",
    "Palatinate Purple": "Purple",
    "Pale Aqua": "Blue",  # Light shade of aqua (mix of blue and green)
    "Pale Blue": "Blue",
    "Pale Brown": "Beige",  # Assuming it's a light shade of brown
    "Pale Carmine": "Pink",  # Light shade of carmine (reddish pink)
    "Pale Cerulean": "Blue",  # Light shade of cerulean (bright blue)
    "Pale Chestnut": "Beige",  # Assuming it's a light shade of chestnut (brownish red)
    "Pale Copper": "Orange",  # Light shade of copper (orange with a metallic sheen)
    "Pale Cornflower Blue": "Blue",  # Light shade of cornflower blue
    "Pale Gold": "Yellow",  # Light shade of gold
    "Pale Goldenrod": "Yellow",  # Light shade of goldenrod (yellowish brown)
    "Pale Green": "Green",
    "Pale Lavender": "Purple",  # Light shade of lavender
    "Pale Magenta": "Pink",  # Light shade of magenta (pinkish purple)
    "Pale Pink": "Pink",
    "Pale Plum": "Purple",  # Light shade of plum (purplish red)
    "Pale Red-Violet": "Pink",  # Light shade of red-violet (leans more towards pink)
    "Pale Robin Egg Blue": "Blue",  # Light shade of robin egg blue
    "Pale Silver": "Grey",  # Light shade of silver
    "Pale Spring Bud": "Green",  # Light shade of spring bud (greenish yellow)
    "Pale Taupe": "Beige",  # Light shade of taupe (greyish brown)
    "Pale Violet-Red": "Pink",  # Light shade of violet-red (leans more towards pink)
    "Pansy Purple": "Purple",
    "Papaya Whip": "Beige",  # Light shade of papaya whip (pale orange-pink)
    "Paris Green": "Green",  # A specific shade of green
    "Pastel Blue": "Blue",
    "Pastel Brown": "Beige",  # Pastel browns are typically light shades
    "Pastel Gray": "Grey",  # Pastel grays are typically light shades
    "Pastel Green": "Green",
    "Pastel Magenta": "Pink",  # Pastel magentas are typically light shades with more pink
    "Pastel Orange": "Orange",
    "Pastel Pink": "Pink",
    "Pastel Purple": "Purple",
    "Pastel Red": "Pink",  # Pastel reds are typically light shades with more pink
    "Pastel Violet": "Purple",
    "Pastel Yellow": "Yellow",
    "Patriarch": "Blue",  # Can vary in shade, but often leans towards blue
    "Payne'S Grey": "Grey",
    "Peach": "Pink",
    "Peach (Crayola)": "Pink",
    "Peach-Orange": "Orange",
    "Peach Puff": "Beige",
    "Peach-Yellow": "Yellow",
    "Pear": "Green",  # Can also be a brownish yellow depending on the shade
    "Pearl": "White",  # Can also have a slight grey or pink tint
    "Pearl Aqua": "Blue",  # Can also be a light turquoise depending on the shade
    "Pearly Purple": "Purple",  # Can also be a light grey with a purple tint
    "Peridot": "Green",  # Can also be a yellowish green
    "Periwinkle": "Blue",  # Can also be a light purple depending on the shade
    "Persian Blue": "Blue",
    "Persian Green": "Green",
    "Persian Indigo": "P",
    "Persian Orange": "Orange",
    "Persian Pink": "Pink",
    "Persian Plum": "Purple",
    "Persian Red": "Red",
    "Persian Rose": "Pink",
    "Persimmon": "Orange",  # Can also be a brownish orange depending on the shade
    "Peru": "Brown",
    "Phlox": "Pink",  # Can also be a purple depending on the shade
    "Phthalo Blue": "Blue",
    "Phthalo Green": "Green",
    "Piggy Pink": "Pink",
    "Pine Green": "Green",
    "Pink": "Pink",
    "Pink Lace": "Pink",
    "Pink-Orange": "Orange",
    "Pink Pearl": "Pink",
    "Pink Sherbet": "Pink",
    "Pistachio": "Green",  # Can also be a yellowish green depending on the shade
    "Platinum": "Grey",
    "Plum (Traditional)": "Purple",
    "Plum (Web)": "Purple",
    "Portland Orange": "Orange",
    "Powder Blue (Web)": "Blue",
    "Princeton Orange": "Orange",
    "Prune": "Purple",  # Can also be a brownish purple depending on the shade
    "Prussian Blue": "Blue",
    "Psychedelic Purple": "Purple",
    "Puce": "Brown",  # Can also be a reddish brown depending on the shade
    "Pumpkin": "Orange",
    "Purple Heart": "Purple",
    "Purple (Html/Css)": "Purple",
    "Purple Mountain Majesty": "Purple",
    "Purple (Munsell)": "Purple",
    "Purple Pizzazz": "Purple",
    "Purple Taupe": "Grey",  # Can also have a purple tint
    "Purple (X11)": "Purple",
  "Quartz": "White",  # Assuming it's a clear or milky white quartz
  "Rackley": "Unknown",  # No clear base color match
  "Radical Red": "Red",
  "Rajah": "Brown",  # Can also be a reddish brown
  "Raspberry": "Red",  # Can also be a purplish red
  "Raspberry Glace": "Red",  # Can also be a purplish red with a sheen
  "Raspberry Pink": "Pink",
  "Raspberry Rose": "Pink",  # Can also be a reddish pink
  "Raw Umber": "Brown",
  "Razzle Dazzle Rose": "Pink",  # Can also be a reddish pink
  "Razzmatazz": "Pink",  # Can be pink or a mix of other colors depending on context
  "Red": "Red",
  "Red-Brown": "Brown",
  "Red Devil": "Red",
  "Red (Munsell)": "Red",
  "Red (Ncs)": "Red",
  "Red-Orange": "Orange",
  "Red (Pigment)": "Red",
  "Red (Ryb)": "Red",
  "Red-Violet": "Violet",
  "Redwood": "Brown",
  "Regalia": "Purple",  # Can also be a blueish purple
  "Resolution Blue": "Blue",
  "Rich Black": "Black",
  "Rich Brilliant Lavender": "Purple",
  "Rich Carmine": "Red",
  "Rich Electric Blue": "Blue",
  "Rich Lavender": "Purple",
  "Rich Lilac": "Purple",
  "Rich Maroon": "Red",  # Can also be a brownish red
  "Rifle Green": "Green",
  "Robin Egg Blue": "Blue",
  "Rose": "Pink",
  "Rose Bonbon": "Pink",
  "Rose Ebony": "Black",  # Assuming it's a very dark brown or black with a reddish tint
  "Rose Gold": "Pink",  # Can also be a metallic pink with gold sheen
  "Rose Madder": "Red",
  "Rose Pink": "Pink",
  "Rose Quartz": "Pink",
  "Rose Taupe": "Beige",  # Can also be a brownish pink
  "Rose Vale": "Pink",  # Can also be a reddish pink
  "Rosewood": "Brown",
  "Rosso Corsa": "Red",
  "Rosy Brown": "Brown",
  "Royal Azure": "Blue",
  "Royal Blue (Traditional)": "Blue",
  "Royal Blue (Web)": "Blue",
  "Royal Fuchsia": "Purple",
  "Royal Purple": "Purple",
  "Royal Yellow": "Yellow",
    "Rubine Red": "Red",
    "Ruby": "Red",
    "Ruby Red": "Red",
    "Ruddy": "Red",  # Can also be brownish red
    "Ruddy Brown": "Brown",
    "Ruddy Pink": "Pink",
    "Rufous": "Brown",  # Can also be reddish brown
    "Russet": "Brown",  # Can also be orange or reddish brown
    "Rust": "Brown",
    "Rusty Red": "Red",
    "Sacramento State Green": "Green",
    "Saddle Brown": "Brown",
    "Safety Orange (Blaze Orange)": "Orange",
    "Saffron": "Yellow",  # Can also be orange depending on shade
    "Salmon": "Pink",  # Can also be orange depending on shade
    "Salmon Pink": "Pink",
    "Sand": "Beige",
    "Sand Dune": "Beige",
    "Sandstorm": "Brown",  # Can also be a beige or light brown
    "Sandy Brown": "Brown",
    "Sandy Taupe": "Beige",  # Can also be brown depending on shade
    "Sangria": "Red",  # Can also be purple depending on shade
    "Sap Green": "Green",
    "Sapphire": "Blue",
    "Sapphire Blue": "Blue",
    "Satin Sheen Gold": "Gold",
    "Scarlet": "Red",
    "Scarlet (Crayola)": "Red",
    "School Bus Yellow": "Yellow",
    "Screamin' Green": "Green",
    "Sea Blue": "Blue",
    "Sea Green": "Green",  # Can also be blue or teal depending on shade
    "Seal Brown": "Brown",
    "Seashell": "Beige",
    "Selective Yellow": "Yellow",
    "Sepia": "Brown",
    "Shadow": "Black",  # Can also be grey depending on context
    "Shamrock Green": "Green",
    "Shocking Pink": "Pink",
    "Shocking Pink (Crayola)": "Pink",
    "Sienna": "Brown",
    "Silver": "Silver",
    "Sinopia": "Red",  # Can also be brown depending on shade
    "Skobeloff": "Blue",  # Can also be a green or teal depending on shade
    "Sky Blue": "Blue",
    "Sky Magenta": "Pink",  # Can also be purple depending on shade
    "Slate Blue": "Blue",
    "Slate Gray": "Grey",
    "Smalt (Dark Powder Blue)": "Blue",
    "Smokey Topaz": "Brown",
    "Smoky Black": "Black",  # Smoky black can appear almost black
    "Snow": "White",
    "Spiro Disco Ball": "Silver",  # Assuming it's a reflective, metallic color
    "Spring Bud": "Green",  # Likely a light or yellowish green
    "Spring Green": "Green",
    "St. Patrick'S Blue": "Green",  # Likely a shade of green associated with St. Patrick's Day
    "Steel Blue": "Blue",  # Steel can have a blueish tint
    "Stil De Grain Yellow": "Yellow",  # Assuming it refers to a type of yellow used in art
    "Stizza": "Brown",  # Can be a dark reddish brown
    "Stormcloud": "Grey",  # Usually refers to a dark grey color
    "Straw": "Yellow",  # Straw has a light yellow color
    "Sunglow": "Orange",  # Likely a bright or yellowish orange
    "Sunset": "Orange",  # Colors in sunsets can vary, but orange is common
    "Tan": "Beige",  # Tan is a light brown or yellowish brown
    "Tangelo": "Orange",  # A citrus fruit with an orange color
    "Tangerine": "Orange",
    "Tangerine Yellow": "Orange",  # Likely on the yellow side of orange
    "Tango Pink": "Pink",  # Likely a bright or vibrant pink
    "Taupe": "Grey",  # Taupe can be a greyish brown
    "Taupe Gray": "Grey",
    "Tea Green": "Green",  # Likely a light or yellowish green for tea
    "Tea Rose (Orange)": "Orange",  # Tea rose can have orange tones
    "Tea Rose (Rose)": "Pink",  # Tea rose can also have pink tones
    "Teal": "Blue",  # Teal is a mix of blue and green, choose based on context
    "Teal Blue": "Blue",  # Leaning more towards blue in the teal spectrum
    "Teal Green": "Green",  # Leaning more towards green in the teal spectrum
    "Telemagenta": "Pink",  # A very bright magenta, can appear pinkish or purplish
    "Tenné (Tawny)": "Brown",  # Tawny refers to a brownish yellow color
    "Terra Cotta": "Brown",  # Terra cotta is a reddish brown earthenware color
    "Thistle": "Purple",  # A light greyish purple color
    "Thulian Pink": "Pink",
    "Tickle Me Pink": "Pink",  # Likely a bright or playful pink
    "Tiffany Blue": "Blue",  # A specific shade of light blue associated with Tiffany & Co.
    "Tiger's Eye": "Brown",  # Tiger's eye has a golden brown chatoyancy
    "Timberwolf": "Grey",  # Likely a dark or greyish brown
    "Titanium Yellow": "Yellow",  # A specific shade of yellow used in pigments
    "Tomato": "Red",  # A deep red color like a ripe tomato
    "Toolbox": "Grey" ,  # Can vary depending on the toolbox material
    "Topaz": "Yellow",  # Topaz can be yellow, orange, or even blueish
    "Tractor Red": "Red",  # Likely a bright or bold red used on tractors
    "Trolley Grey": "Grey",  # A greyish color commonly used on trolleys
    "Tropical Rain Forest": "Green",  # Can be a variety of greens representing the rainforest
    "True Blue": "Blue",  # A pure or perfect blue
    "Tufts Blue": "Blue",  # Specific shade of blue associated with Tufts University
    "Tumbleweed": "Tan",  # Tumbleweeds are a light brown or tan color
    "Turkish Rose": "Pink",  # A specific shade of pink associated with Turkish delight
    "Turquoise": "Blue",  # A mix of blue and green, choose based on context
    "Turquoise Blue": "Blue",  # Leaning more towards blue in the turquoise spectrum
    "Turquoise Green": "Green",  # Leaning more towards green in the turquoise spectrum
    "Tuscan Red": "Red",
    "Twilight Lavender": "Purple",  # Assuming it's a light or pinkish purple
    "Tyrian Purple": "Purple",
    "Ua Blue": "Blue",  # Assuming Ua refers to a university or organization
    "Ua Red": "Red",  # Assuming Ua refers to a university or organization
    "Ube": "Purple",  # Ube is a type of purple yam
    "Ucla Blue": "Blue",  # Assuming UCLA refers to the university
    "Ucla Gold": "Gold",  # Assuming UCLA refers to the university
    "Ufo Green": "Green",  # Can be a light or bright green depending on context
    "Ultra Pink": "Pink",
    "Ultramarine": "Blue",  # Can also be a violet or purple depending on shade
    "Ultramarine Blue": "Blue",
    "Umber": "Brown",  # Umber can be a reddish brown or yellowish brown
    "Unbleached Silk": "White",  # Assuming it's a very light color close to white
    "United Nations Blue": "Blue",  # Assuming it refers to the specific shade
    "University Of California Gold": "Gold",  # Assuming California refers to the university
    "Unmellow Yellow": "Yellow",  # Can be a bright or dark yellow depending on context
    "Up Forest Green": "Green",  # Assuming Up refers to a brand or specific shade
    "Up Maroon": "Red",  # Assuming Up refers to a brand or specific shade
    "Upsdell Red": "Red",  # Assuming Upsdell refers to a brand or specific shade
    "Urobilin": "Yellow",  # Can be a brownish yellow depending on context
    "Usafa Blue": "Blue",  # Assuming Usafa refers to the US Air Force Academy
    "Usc Cardinal": "Red",  # Assuming USC refers to the university and Cardinal is their color
    "Usc Gold": "Gold",  # Assuming USC refers to the university
    "Utah Crimson": "Red",  # Assuming Utah refers to the university
    "Vanilla": "Beige",  # Vanilla is a light yellowish color
    "Vegas Gold": "Gold",  # Assuming Vegas refers to a brand or specific shade
    "Venetian Red": "Red",  # Venetian Red is a reddish-brown
    "Verdigris": "Green",  # Verdigris can be a blue-green or turquoise depending on shade
    "Vermilion (Cinnabar)": "Red",  # Vermilion is a bright red
    "Vermilion (Plochere)": "Red",  # Vermilion is a bright red
    "Veronica": "Violet",  # Veronica is a type of flower with various purple shades
    "Violet": "Violet",
    "Violet-Blue": "Violet",
    "Violet (Color Wheel)": "Violet",
    "Violet (Ryb)": "Violet",
    "Violet (Web)": "Violet",
    "Viridian": "Green",  # Viridian is a blue-green color
    "Vivid Auburn": "Brown",  # Vivid Auburn is a reddish brown
    "Vivid Burgundy": "Red",  # Burgundy is a dark red
    "Vivid Cerise": "Pink",  # Cerise is a bright pink
    "Vivid Tangerine": "Orange",  # Vivid Tangerine is a bright orange
    "Vivid Violet": "Violet",
    "Warm Black": "Black",  # Warm black can have a slight brown tint
    "Waterspout": "Grey",  # Assuming it refers to the color of a waterspout
    "Wenge": "Black",  # Wenge wood is a very dark brown, close to black
    "Wheat": "Beige",  # Wheat is a light yellowish brown
    "White": "White",
    "White Smoke": "White",  # White smoke is a very light grey, close to white
    "Wild Blue Yonder": "Blue",  # Can be a bright or light blue depending on context
    "Wild Strawberry": "Red",
    "Wild Watermelon": "Pink",  # Can be a pinkish red depending on shade
    "Wine": "Red",  # Can vary in shade
    "Wine Dregs": "Brown",  # Can be a brownish red depending on shade
    "Wisteria": "Violet",
    "Wood Brown": "Brown",
    "Xanadu": "Blue",  # Can be a light blue depending on shade
    "Yale Blue": "Blue",
    "Yellow": "Yellow",
    "Yellow-Green": "Yellow",  # Depending on the dominant color
    "Yellow (Munsell)": "Yellow",
    "Yellow (Ncs)": "Yellow",
    "Yellow Orange": "Orange",
    "Yellow (Process)": "Yellow",
    "Yellow (Ryb)": "Yellow",
    "Zaffre": "Blue",  # Can be a dark blue depending on shade
    "Zinnwaldite Brown": "Brown",
    }
    ################################################
    def get_name_csv(csv_color):
        return base_colors[csv_color]

    
        # Reading csv file with pandas and giving names to each column
    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv('colors.csv', names=index, header=None)
    #####################################################
    def get_color_name(R, G, B):
          minimum = 10000
          for i in range(len(csv)):
             d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
             if d <= minimum:
                 minimum = d
                 cname = csv.loc[i, "color_name"]
          return cname

    #####################################################

    '''
    ######################################################
    # Step 1: Load the CSV file
    data = pd.read_csv('colors1.csv')
    
    # Step 2: Extract BGR values and convert to numpy array
    bgr_values = data[['B', 'G', 'R']].values
    
    # Step 3: Apply K-means clustering
    num_clusters = 15  # You can adjust this parameter
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    cluster_labels = kmeans.fit_predict(bgr_values)
    
    # Step 4: Create a dictionary to store cluster colors
    cluster_dict = {}
    ########################################################
    # Step 5: Analyze clusters and assign labels
    for cluster_id in range(num_clusters):
        cluster_indices = np.where(cluster_labels == cluster_id)[0]
        cluster_colors = data.iloc[cluster_indices]['ColorName'].tolist()
        cluster_dict[cluster_id] = cluster_colors
    
    # Step 6: Print the dictionary
    #########################################################
    for key, value in cluster_dict.items():
        print("Key:", key)
        print("Value:", value)
    
    my_dict=cluster_dict.copy()
    
    
    key_changes = {0: 'Violet', 1: 'Blue', 2: '', 3: 'Blue Gray', 4: 'Red', 5: 'Blue', 6: 'white', 7: 'Blue Green', 8: 'Brown', 9: 'Green', 10: 'Orange', 11: 'Red', 12: 'Black', 13: 'Pink', 14: 'Yellow'}
    
    # Create a new dictionary to store the modified key-value pairs
    new_dict = {}
    ############################################################
    # Apply the changes
    for old_key, new_key in key_changes.items():
        if old_key in my_dict:
            value = my_dict.pop(old_key)
            new_dict[new_key] = value
    
    # Add remaining key-value pairs not affected by the changes
    new_dict.update(my_dict)
    '''    
    #######################################################333
    import cv2
    from ultralytics import YOLO
    
    # Load the YOLOv8 model
    model = YOLO('yolov8n.pt')
    frame_no=0
    # Open the video file
    
    cap = cv2.VideoCapture(video_path)
    
    total_frames= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)
    
    def find_key_from_value(my_dict, search_string):
        for key, value_list in my_dict.items():
            if search_string in value_list:
                return key
        return None
    
    

    lsfr=-4
    fr = -1
    lists=[]
    instance=[]
    lastinst=[]
    while cap.isOpened():
        frame_no+=1
        # Read a frame from the video
        success, frame = cap.read()
        if not success:
            break
        #frame_no=int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    
        """if frame_no ==25:
            break"""
        if frame_no%3==0:
            if success : # and frame_no%2!=0 :
                # Run YOLOv8 inference on the frame
                cls=[2]
                results = model(frame,classes=cls,conf=cnfd)
        
                if not results[0]  :
                    continue
        
                for r in results:
                    xyxy=r.boxes.xyxy.tolist()
        
                image=frame.copy()
        
                
        
                for x1,y1,x2,y2 in xyxy:
                    x1=int(x1)
                    x2=int(x2)
                    y1=int(y1)
                    y2=int(y2)
                    roi = image[y1:y2, x1:x2]
                    # Split the ROI into its color channels (BGR)
                    b, g, r = cv2.split(roi)
        
                    # Calculate the average color values for each channel
                    average_b = b.mean()
                    average_g = g.mean()
                    average_r = r.mean()
        
        
                    b, g, r = average_b,average_g,average_r
                    b = int(b)
                    g = int(g)
                    r = int(r)
        
                    text = get_color_name(r, g, b)
        
                    color=get_name_csv(text)
        
                    #print('Color Name : ',color)
                    annotated_frame = results[0].plot()
                    '''while True:
                        cv2.imshow("image",annotated_frame)
                        # Break the loop when user hits 'esc' key
                        if cv2.waitKey(20) & 0xFF == 27:
                            break'''

                    color=color.lower()    
                    if color in color_name:
                        for r in results:
                            if any(elem in cls for elem in r.boxes.cls.tolist()):
                                if(frame_no-lsfr>60):
                                      lists.append(instance)
                                      lastinst=instance
                                      instance=[]
                                instance.append(round(frame_no/30))
                                print(int(frame_no/30))
                                lsfr=frame_no
                    print(frame_no,"printing color",color,)
                    
                    
                          
        
        

    x=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(x)
    cap.release()    
    cv2.destroyAllWindows()
    lists.append(instance)
    output_list=[]
    for i in lists:
        if(len(i))>0:
            finalframe=len(i)-1
            output_list.append('from : '+timeformat(i[0])+' to '+timeformat(i[finalframe]))
    print(lists)

    return(output_list)
