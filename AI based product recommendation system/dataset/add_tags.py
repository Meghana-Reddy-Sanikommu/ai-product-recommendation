import pandas as pd

df = pd.read_csv("dataset/products.csv")

tags = {
    "iPhone 14": "Premium Camera Smartphone",
    "iPhone 15": "Premium Camera Smartphone",
    "Samsung Galaxy S23": "Premium Android 5G",
    "Samsung Galaxy S24": "Premium Android 5G",
    "Redmi Note 13": "Budget Battery Smartphone",
    "Redmi Note 14": "Budget Battery Smartphone",
    "OnePlus 12": "Performance FastCharging Smartphone",
    "Realme GT": "Gaming Performance Smartphone",

    "Dell Inspiron Laptop": "Student Office",
    "Dell Vostro Laptop": "Business Office",
    "HP Pavilion Laptop": "Office Productivity",
    "HP Victus Laptop": "Gaming Performance",
    "Lenovo IdeaPad": "Student Everyday",
    "Lenovo ThinkPad": "Business Professional",
    "Asus VivoBook": "Student Lightweight",
    "Asus ROG Laptop": "Gaming RTX HighPerformance",

    "Sony Bravia TV": "SmartTV 4K",
    "Sony OLED TV": "OLED Premium PictureQuality",
    "Samsung Smart TV": "SmartTV 4K",
    "Samsung QLED TV": "QLED Premium PictureQuality",
    "LG Smart TV": "SmartTV Budget",
    "LG OLED TV": "OLED Premium PictureQuality",

    "LG Refrigerator": "Family DoubleDoor",
    "LG Smart Refrigerator": "Smart EnergySaving",
    "Whirlpool Refrigerator": "EnergySaving Family",
    "Samsung Refrigerator": "FrostFree Family",

    "Floral Kurti": "Casual Traditional",
    "Designer Kurti": "Party Traditional",
    "Printed Kurti": "Casual Fashion",
    "Anarkali Kurti": "Traditional Wedding",

    "Men Casual Shirt": "Casual Cotton",
    "Formal Shirt": "Office Formal",
    "Men T Shirt": "Casual Everyday",
    "Men Jeans": "Casual Denim",

    "Kids T Shirt": "Casual Comfortable",
    "Kids Dress": "Casual Fashion",

    "Titan Watch": "Premium Analog",
    "Fastrack Watch": "Fashion Youth",
    "Casio Watch": "Digital Sports",

    "Boat Headphones": "Budget Wireless",
    "JBL Headphones": "Premium Audio",
    "Sony Headphones": "Premium NoiseCancellation",

    "Samsung Galaxy A55": "MidRange 5G Smartphone",
    "Samsung Galaxy M35": "Budget Battery Smartphone",
    "OnePlus Nord 4": "MidRange FastCharging Smartphone",
    "OnePlus Nord CE 4": "Budget FastCharging Smartphone",
    "Nothing Phone 2": "Premium Design Smartphone",
    "Nothing Phone 2a": "Budget Design Smartphone",
    "Vivo V30": "Camera Smartphone",
    "Oppo Reno 12": "Camera Premium Smartphone",
    "Motorola Edge 50": "CleanAndroid Performance",
    "iQOO Neo 9 Pro": "Gaming HighPerformance",
    "Poco X6 Pro": "Gaming Budget Smartphone",
    "Google Pixel 8": "AI Camera Premium",

    "Acer Aspire 5": "Student Productivity",
    "Acer Nitro 5": "Gaming RTX",
    "MSI Thin 15": "Gaming RTX",
    "MSI Katana 15": "Gaming RTX HighPerformance",
    "Dell XPS 13": "Premium Ultrabook",
    "HP Envy Laptop": "Premium Productivity",
    "Lenovo Legion 5": "Gaming RTX",
    "Asus ZenBook": "Premium Lightweight",
    "MacBook Air M2": "Premium Productivity",
    "MacBook Air M3": "Premium Productivity",

    "TCL Smart TV": "SmartTV Budget",
    "TCL QLED TV": "QLED Premium PictureQuality",
    "Panasonic Smart TV": "SmartTV 4K",
    "Panasonic OLED TV": "OLED Premium PictureQuality",
    "Mi Smart TV X": "Budget SmartTV",
    "OnePlus Smart TV": "SmartTV Android",
    "Vu Masterpiece TV": "QLED Premium",
    "Hisense Smart TV": "Budget SmartTV",

    "Godrej Refrigerator": "Family DoubleDoor",
    "Godrej Smart Refrigerator": "Smart EnergySaving",
    "Haier Refrigerator": "EnergySaving Family",
    "Haier Smart Refrigerator": "Smart Convertible",
    "Panasonic Refrigerator": "FrostFree Family",
    "Bosch Refrigerator": "Premium EnergySaving",
    "Samsung Family Hub Refrigerator": "Smart Premium Family",
    "LG InstaView Refrigerator": "Smart Premium Family",

    "Checked Shirt": "Casual Fashion",
    "Slim Fit Shirt": "Office Premium",
    "Polo T Shirt": "Casual Premium",
    "Black Jeans": "Casual Denim",
    "Cargo Pants": "Casual Outdoor",
    "Denim Jacket": "Fashion Casual",

    "Cotton Kurti": "Casual Comfortable",
    "Party Wear Kurti": "Party Fashion",
    "Ethnic Kurti": "Traditional Ethnic",
    "Straight Kurti": "Office Casual",
    "Printed Dress": "Casual Fashion",
    "Women Jeans": "Casual Western",

    "Kids Hoodie": "Winter Casual",
    "Kids Jeans": "Casual Denim",
    "Kids Jacket": "Winter Warm",
    "Kids Shorts": "Casual Cotton",

    "Timex Watch": "Classic Analog",
    "Fossil Watch": "Premium Fashion",
    "Sonata Watch": "Budget Analog",
    "Titan Edge Watch": "Premium Slim",
    "G Shock Watch": "Sports Rugged",

    "Noise Headphones": "Wireless Budget",
    "Realme Headphones": "Budget Wireless",
    "Skullcandy Headphones": "Bass Audio",
    "Sennheiser Headphones": "Premium StudioAudio",
    "Boat Rockerz 550": "Wireless Bass"
}

df["Tags"] = df["Product_Name"].map(tags)

df.to_csv("dataset/products.csv", index=False)

print("Tags added successfully!")