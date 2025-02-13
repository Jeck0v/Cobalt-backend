from pymongo import MongoClient

client = MongoClient(
    host="mongo",
    port=27017,
    username="cobaltdb",
    password="-)i8N~x4r9cVX8"
)

db = client.cobalt_db


def initialize_database():
    """
    Init bdd
    """
    required_collections = ['users', 'products', 'orders']
    existing_collections = db.list_collection_names()
    for collection in required_collections:
        if collection not in existing_collections:
            db.create_collection(collection)
            print(f"Collection '{collection}' créée.")

    if db.products.count_documents({}) == 0:
        products = [
            {
                "id": "1",
                "titre": "Timeless Style Leather Bracelet",
                "description": "Step into timeless style with this genuine leather bracelet, crafted for the modern man who values both durability and sophistication. Made from premium leather, its rich texture and earthy tones make it a versatile accessory for any occasion. Whether you're dressing up for a formal event or keeping it casual for a weekend outing, this bracelet adds a touch of rugged elegance to your look. Perfect for men who appreciate craftsmanship and understated luxury, this piece is more than an accessory—it's a statement. Elevate your style with a bracelet that combines comfort, quality, and timeless appeal.",
                "prix": 48.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "2",
                "titre": "Vintage Watch",
                "description": "Travel back in time with this elegant and retro leather watch, a masterpiece of vintage-inspired design. Featuring a rich brown leather strap and a meticulously crafted dial, this watch exudes old-world charm while offering modern functionality. Ideal for the sophisticated gentleman who values both style and substance, it’s the perfect companion for business meetings, casual outings, or special occasions. Make every moment count with a watch that tells more than time—it tells your story.",
                "prix": 199.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "3",
                "titre": "Rafined Silver Ring",
                "description": "Make a bold yet refined statement with this 925 sterling silver ring. Its sleek, minimalist design is perfect for the modern man who values understated elegance. The cool, polished finish complements any outfit, from casual jeans and a tee to a sharp suit. A symbol of strength and sophistication, this ring is more than just an accessory—it's an expression of your individuality. Add a touch of timeless class to your everyday look with this must-have piece.",
                "prix": 187.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "4",
                "titre": "Modern Steel Necklace",
                "description": "Upgrade your style with this stainless steel necklace, a perfect blend of durability and modern design. Crafted from hypoallergenic stainless steel, it’s built to last while maintaining its sleek, polished finish. Whether you're layering it with other pieces or wearing it solo, this necklace adds a contemporary edge to any outfit. Ideal for the man who values versatility and effortless style, this piece is a wardrobe essential. Wear it confidently, knowing it’s as strong and resilient as you are.",
                "prix": 49.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "5",
                "titre": "Elegant Cobalt Pendant",
                "description": "Stand out from the crowd with this elegant cobalt pendant, a true masterpiece of color and craftsmanship. The deep, mesmerizing blue hue is set against a polished metal backdrop, creating a striking contrast that catches the eye. Perfect for adding a pop of color to your ensemble, this pendant is a bold yet sophisticated choice for the man who isn’t afraid to make a statement. Wear it as a symbol of confidence, creativity, and individuality.",
                "prix": 299.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "6",
                "titre": "Luxury Gold Hoop Earrings",
                "description": "Elevate your style with these stylish gold hoop earrings, designed for the modern man who appreciates luxury and versatility. Crafted from high-quality gold, their double-row design adds a touch of opulence to any look. Whether you're dressing up for a special occasion or keeping it casual, these earrings are the perfect way to express your confidence and sophistication. A timeless piece that speaks volumes without saying a word.",
                "prix": 279.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "7",
                "titre": "Brown Leather Bracelet",
                "description": "Embrace rugged elegance with this brown leather bracelet, a perfect blend of style and durability. Made from genuine leather, its rich, earthy tones and textured finish make it a versatile accessory for any outfit. Whether you're pairing it with a casual look or adding it to a more polished ensemble, this bracelet is a subtle yet impactful way to express your personal style. For the man who values authenticity and timeless design.",
                "prix": 29.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "8",
                "titre": "Elegant Watch",
                "description": "Rediscover the charm of yesteryear with this elegant and retro leather watch. Its vintage-inspired design, complete with a rich brown leather strap and intricate dial details, makes it a standout piece for any gentleman. Perfect for those who appreciate classic style with a modern twist, this watch is more than a timepiece—it’s a conversation starter. Wear it proudly and let it reflect your refined taste.",
                "prix": 199.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "9",
                "titre": "Silver Ring",
                "description": "Add a touch of sophistication to your look with this 925 silver ring. Its sleek, polished design is perfect for the modern man who values simplicity and elegance. Whether you're wearing it daily or for special occasions, this ring is a timeless piece that complements any outfit. A symbol of strength and refinement, it’s the perfect way to express your individuality. Make it yours and let it become a part of your signature style.",
                "prix": 49.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "10",
                "titre": "Polished Steel Necklace",
                "description": "Add a modern edge to your look with this stainless steel necklace, a perfect blend of durability and style. Its sleek, polished finish and hypoallergenic material make it a versatile piece for any occasion. Whether you're layering it with other necklaces or wearing it solo, this necklace is a must-have for the contemporary man. For those who value both strength and sophistication, this piece is a true wardrobe essential.",
                "prix": 49.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "11",
                "titre": "Deep Blue Cobalt Pendant",
                "description": "Make a bold statement with this elegant cobalt pendant, a stunning blend of color and craftsmanship. Its deep blue hue and polished metal setting create a striking contrast that’s sure to turn heads. Perfect for adding a pop of color to your outfit, this pendant is a bold yet sophisticated choice for the man who loves to stand out. Wear it as a symbol of confidence and creativity.",
                "prix": 299.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "12",
                "titre": "Casual Gold Hoop Earrings",
                "description": "Channel effortless style with these gold hoop earrings, crafted for the man who appreciates luxury and versatility. Their double-row design and high-quality gold finish make them a luxurious addition to any outfit. Whether you're dressing up for a special occasion or keeping it casual, these earrings are the perfect way to elevate your style. A timeless piece that exudes confidence and sophistication.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "13",
                "titre": "Glamour Gold Hoop Earrings",
                "description": "Add a touch of glamour to your look with these gold hoop earrings, designed for the modern man who values timeless elegance. Their high-quality gold finish and double-row design make them a versatile accessory for any occasion. Whether you're dressing up or keeping it casual, these earrings are the perfect way to express your confidence and style. Wear them proudly and let them speak for themselves.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "14",
                "titre": "Luxury Leather Bracelet",
                "description": "Indulge in the ultimate accessory with this luxury leather bracelet, crafted for the man who values quality and style. Made from premium leather, its rich texture and elegant design make it a standout piece for any occasion. Whether you're dressing up or keeping it casual, this bracelet adds a touch of sophistication to your look. For the man who appreciates the finer things in life, this piece is a must-have.",
                "prix": 89.99,
                "quantite": 30,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "15",
                "titre": "Watch For Modern Gentleman",
                "description": "Step back in time with this elegant and retro leather watch, a timeless piece for the modern gentleman. Its vintage-inspired design and rich brown leather strap make it the perfect accessory for any occasion. Whether you're at a business meeting or a casual gathering, this watch is the ultimate statement piece. For the man who values classic style with a modern twist, this watch is a true investment.",
                "prix": 69.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "16",
                "titre": "Minimalist Silver Ring",
                "description": "Make a bold yet refined statement with this 925 sterling silver ring. Its sleek, minimalist design is perfect for the modern man who values understated elegance. The cool, polished finish complements any outfit, from casual jeans and a tee to a sharp suit. A symbol of strength and sophistication, this ring is more than just an accessory—it's an expression of your individuality. Add a touch of timeless class to your everyday look with this must-have piece.",
                "prix": 79.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "17",
                "titre": "Modern Steel Necklace",
                "description": "Upgrade your style with this stainless steel necklace, a perfect blend of durability and modern design. Crafted from hypoallergenic stainless steel, it’s built to last while maintaining its sleek, polished finish. Whether you're layering it with other pieces or wearing it solo, this necklace adds a contemporary edge to any outfit. Ideal for the man who values versatility and effortless style, this piece is a wardrobe essential. Wear it confidently, knowing it’s as strong and resilient as you are.",
                "prix": 99.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "18",
                "titre": "Elegant Cobalt Pendant",
                "description": "Stand out from the crowd with this elegant cobalt pendant, a true masterpiece of color and craftsmanship. The deep, mesmerizing blue hue is set against a polished metal backdrop, creating a striking contrast that catches the eye. Perfect for adding a pop of color to your ensemble, this pendant is a bold yet sophisticated choice for the man who isn’t afraid to make a statement. Wear it as a symbol of confidence, creativity, and individuality.",
                "prix": 189.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "19",
                "titre": "Special Gold Hoop Earrings",
                "description": "Elevate your style with these stylish gold hoop earrings, designed for the modern man who appreciates luxury and versatility. Crafted from high-quality gold, their double-row design adds a touch of opulence to any look. Whether you're dressing up for a special occasion or keeping it casual, these earrings are the perfect way to express your confidence and sophistication. A timeless piece that speaks volumes without saying a word.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "20",
                "titre": "Stainless Steel Necklace",
                "description": "Add a modern edge to your look with this stainless steel necklace, a perfect blend of durability and style. Its sleek, polished finish and hypoallergenic material make it a versatile piece for any occasion. Whether you're layering it with other necklaces or wearing it solo, this necklace is a must-have for the contemporary man. For those who value both strength and sophistication, this piece is a true wardrobe essential.",
                "prix": 210.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "21",
                "titre": "Deep Blue Cobalt Pendant",
                "description": "Make a bold statement with this elegant cobalt pendant, a stunning blend of color and craftsmanship. Its deep blue hue and polished metal setting create a striking contrast that’s sure to turn heads. Perfect for adding a pop of color to your outfit, this pendant is a bold yet sophisticated choice for the man who loves to stand out. Wear it as a symbol of confidence and creativity.",
                "prix": 430.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "22",
                "titre": "Polished Cobalt Pendant",
                "description": "Add a touch of sophistication to your look with this cobalt pendant. Its deep blue hue and polished metal setting make it a standout piece for any occasion. Whether you're dressing up or keeping it casual, this pendant is the perfect way to elevate your style. A symbol of confidence and individuality, it’s a must-have for the modern man.",
                "prix": 245.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "23",
                "titre": "Retro Watch",
                "description": "Rediscover the charm of yesteryear with this elegant and retro leather watch. Its vintage-inspired design and rich brown leather strap make it a timeless piece for any gentleman. Perfect for those who appreciate classic style with a modern twist, this watch is more than a timepiece—it’s a conversation starter. Wear it proudly and let it reflect your refined taste.",
                "prix": 185.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "24",
                "titre": "Elegant Watch",
                "description": "Step back in time with this elegant and retro leather watch, a timeless piece for the modern gentleman. Its vintage-inspired design and rich brown leather strap make it the perfect accessory for any occasion. Whether you're at a business meeting or a casual gathering, this watch is the ultimate statement piece. For the man who values classic style with a modern twist, this watch is a true investment.",
                "prix": 99.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "25",
                "titre": "Limited Edition Luxury Watch",
                "description": "Unveil the essence of luxury with this limited-edition elegant and retro leather watch. Designed for the discerning gentleman, it features a premium brown leather strap, a scratch-resistant sapphire crystal face, and a meticulously crafted dial that pays homage to classic watchmaking. This isn’t just a watch—it’s a legacy. With only a few pieces available, exclusivity is guaranteed. Whether you're dressing for a black-tie event or a casual evening out, this watch is the perfect companion for the man who demands nothing but the best. Elevate your style and own a piece of history.",
                "prix": 599.99,
                "quantite": 13,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "26",
                "titre": "Vintage Edition  Watch",
                "description": "Elevate your style with this elegant and retro leather watch, a masterpiece of vintage-inspired design. This is a Vintage Edition. Its rich brown leather strap and intricate dial details make it a standout piece for any occasion. Perfect for the sophisticated gentleman who values both style and substance, this watch is more than a timepiece—it’s a statement. Wear it proudly and let it reflect your refined taste.",
                "prix": 499.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "27",
                "titre": "Elegant Watch",
                "description": "Make a statement with this elegant and retro leather watch, a timeless piece for the modern gentleman. Its vintage-inspired design and rich brown leather strap make it the perfect accessory for any occasion. Whether you're at a business meeting or a casual gathering, this watch is the ultimate statement piece. For the man who values classic style with a modern twist, this watch is a true investment.",
                "prix": 599.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "28",
                "titre": "Silver Ring",
                "description": "Add a touch of sophistication to your look with this 925 silver ring. Its sleek, polished design is perfect for the modern man who values simplicity and elegance. Whether you're wearing it daily or for special occasions, this ring is a timeless piece that complements any outfit. A symbol of strength and refinement, it’s the perfect way to express your individuality. Make it yours and let it become a part of your signature style.",
                "prix": 449.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "29",
                "titre": "Silver Ring",
                "description": "Make a bold yet refined statement with this 925 sterling silver ring. Its sleek, minimalist design is perfect for the modern man who values understated elegance. The cool, polished finish complements any outfit, from casual jeans and a tee to a sharp suit. A symbol of strength and sophistication, this ring is more than just an accessory—it's an expression of your individuality. Add a touch of timeless class to your everyday look with this must-have piece.",
                "prix": 129.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
        ]
        db.products.insert_many(products)
        print("Données de test pour 'products' insérées.")

    if db.users.count_documents({}) == 0:
        users = [
            {
                "firstname": "John",
                "name": "Doe",
                "password": "password123",
                "email": "john.doe@example.com"
            },
            {
                "firstname": "Jane",
                "name": "Doe",
                "password": "pas88opfi3",
                "email": "jane.doe@example.com"
            },
            {
                "firstname": "Marcus",
                "name": "Lovis",
                "password": "9:W5fx!E83iCf)",
                "email": "marcus.lovis@example.com"
            },
        ]
        db.users.insert_many(users)
        print("Données de test pour 'users' insérées.")


initialize_database()