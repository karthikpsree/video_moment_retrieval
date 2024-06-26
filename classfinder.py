def getclass(objects):
    coco=['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic', 'hydrant', 'stop sign', 'meter',              'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase',              'frisbee', 'skis','snowboard', 'ball', 'kite', 'bat', 'glove', 'skateboard', 'surfboard', 'racket', 'bottle', 'cup','fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot', 'pizza', 'donut', 'cake', 'chair', 'couch','plant', 'bed', 'table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'phone', 'microwave', 'oven', 'toaster', 'sink','refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy', 'hair drier', 'toothbrush','glass']
    
    
    coco_dict = {
  "person": ["man", "woman", "child", "adult", "senior", "athlete", "tourist", "worker", "passenger"],
  "bicycle": ["bike", "mountain bike", "bmx", "cruiser", "tandem", "recumbent"],
  "car": ["sedan", "SUV", "coupe", "hatchback", "wagon", "convertible", "van","vehicle"],
  "motorcycle": ["scooter", "cruiser", "sportbike", "touring", "bike","vehicle"],
  "airplane": ["plane", "jet", "helicopter"],
  "bus": ["double-decker","vehicle"],
  "train": [ "subway", "locomotive"],
  "truck": ["pickup","vehicle"],
  "boat": ["sailboat", "motorboat", "rowboat", "kayak", "canoe", "ferry", "tugboat", "yacht"],
  "traffic": ["traffic","signal"],
  "hydrant": ["hydrant"],
  "sign": ["signal", "sign"],
  "meter": ["parking", "meter", "station"],
  "bench": ["park"],
  "bird": ["sparrow","pigeon", "robin", "hawk", "eagle", "owl", "parrot", "penguin", "ostrich"],
  "cat": [ "kitten", "tabby", "Siamese", "Persian", "Maine Coon", "Sphynx"],
  "dog": ["puppy", "Labrador", "Retriever", "Shepherd", "Beagle", "Poodle", "Bulldog", "Chihuahua"],
  "horse": ["stallion", "mare", "colt", "foal", "Arabian", "thoroughbred", "Clydesdale", "mustang"],
  "sheep": ["flock", "ram", "ewe", "lamb", "Merino", "wool", "pasture"],
  "cow": ["bull", "calf", "herd", "dairy", "beef", "cattle", "Angus", "Holstein"],
  "elephant": ["tusk", "trunk", "savannah", "herd"],
  "bear": ["grizzly", "polar", "cub", "forest", "mountain"],
  "zebra": ["stripes", "herd", "plains", "Africa"],
  "giraffe": ["neck", "mammal", "savanna", "Africa"],
  "backpack": ["rucksack", "knapsack", "daypack", "school bag"],
  "umbrella": ["shelter", "canopy", "rain", "sun", "fold-up", "compact"],
  "handbag": ["purse", "tote bag", "satchel", "clutch", "bag"],
  "tie": ["necktie", "formal wear", "attire", "patterned", "striped", "solid"],
  "suitcase": ["luggage", "travel", "duffel", "carry-on","rolling"],
  "frisbee": ["flying", "disc", "plastic", "catch",],
  "skis": ["snow ","slalom"],
  "snowboard": [ "snowboarding", "sport"],
  "ball": ["ball"],
  "kite": ["flown", "wind","toy", "tethered"],
  "bat": ["bat", "wooden", "baseball"],
  "glove": ["glove", "mitt", "baseball","equipment"],
  "skateboard": ["board", "skate deck", "streetwear"],
  "surfboard": ["board", "wave riding board", "surfing","equipment"],
  "racket": ["racket", "racquet", "tennis"],
  "bottle": ["container", "beverage", "plastic"],
  "glass": ["glass", "drink",],
  "cup": ["drink", "mug", "beverage","container"],
  "fork": ["utensil", "eat","utensil", "flatware"],
  "knife": ["utensil", "cut", "blade"],
  "spoon": ["utensil", "eat" ,"utensil", "flatware"],
  "bowl": ["dish", "serve", "round","container"],
  "banana": ["fruit", "tropical"],
  "apple": ["fruit", "round"],
  "sandwich": ["food", "bread","filling", "lunch"],
  "orange": ["fruit", "citrus", "round"],
  "broccoli": ["vegetable", "green", "floret"],
  "carrot": ["vegetable", "orange vegetable", "root vegetable"],
  "pizza": ["food", "Italian", "sliced","pie"],
  "donut": ["pastry", "sweet pastry", "doughnut"],
  "cake": ["pastry", "dessert", "baked good"],
  "chair": ["seating", "furniture", "single seat"],
  "couch": ["sofa", "seating", "furniture", "multiple seat"],
  "potted plant": ["plant", "houseplant", "container plant"],
  "bed": ["furniture", "sleeping furniture", "mattress"],
  "table": ["table", "furniture", "eating surface"],
  "toilet": ["bathroom", "sanitary", "waste"],
  "tv": ["television", "entertainment device", "screen"],
  "laptop": ["computer", "portable computer", "notebook","computer"],
  "mouse": ["computer accessory", "pointing device"],
  "remote": ["remote control", "electronic device", "channel changer"],
  "keyboard": ["computer accessory", "input device", "typing"],
  "phone": ["mobile","cell", "smartphone", "communication" ,"device"],
  "microwave": ["appliance", "appliance", "heating","device"],
  "oven": ["appliance", "kitchen","appliance", "baking","cooking"],
  "toaster": ["appliance", "kitchen","appliance", "browning"],
  "sink": ["plumbing", "washing", "basin"],
  "refrigerator": ["appliance", "kitchen","appliance", "cooling"],
  "book": ["reading","material", "printed", "pages"],
  "clock": ["timekeeping","device", "wristwatch"],
  "vase": ["container", "flower", "holder"],
  "scissors": ["cutting", "handheld" ,"tool"],
  "teddy": ["stuffed" "animal", "plush","toy"],
  "drier": ["hairdryer", "tool", "electric", "appliance"],
  "toothbrush": ["dental" ,"hygiene", "cleaning"]
}
    cls=[]
    for i in objects:
        if i in coco:
            cls.append(coco.index(i))
        
        else:
            for key in coco_dict:
                if i in coco_dict[key]:
                    cls.append(coco.index(key))
    return cls
            