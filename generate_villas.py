#!/usr/bin/env python3
"""Generate 16 individual SEO-optimized villa pages for seaviewhomes.com"""

import os
import json
import html as html_lib

OUTPUT_DIR = "/Users/macai/.openclaw/workspace/seaview-homes-site/villas"
SITE_URL = "https://seaviewhomes.com"
IMG_BASE = "assets/img/villas"

villas = [
    {
        "slug": "villa-splendore",
        "name": "Villa Splendore",
        "image": "villa-splendore.jpg",
        "rooms": 3, "baths": "2.5", "sleeps": 6,
        "type": "Oceanview Maria Bluff Villa",
        "short_desc": "Renovated 3-bedroom Maria Bluff villa with western ocean views, year-round sunsets, private pool, and hot tub.",
        "description": "Villa Splendore was renovated in 2016 with new furniture throughout, appliances, electronics, kitchen appliances, countertops, fans, and more. Located on the ocean side of Maria Bluff, Villa Splendore has fabulous western exposure from 375 feet above the ocean, ensuring sunsets all year long with great views of St. Thomas, St. Croix, the southern cays, Pillsbury Sound, and the northern cays. Surrounded by lush tropical landscaping, you experience complete privacy while still enjoying the convenience of being near town. Splendore has two identical king suites with A/C and large baths with stunning garden showers. There is also an air-conditioned cupola den/bedroom with spiral staircase access and a king bed or two twins, plus a half bath on the main level. The great room, kitchen, and all bedrooms have split air conditioning, a modern entertainment system with WiFi, stereo, DVD, cable, and TVs in the bedrooms and great room. The villa offers a lovely interior dining area and gourmet kitchen, all with panoramic ocean views. Outside, there is an outdoor dining deck with a Weber grill, plenty of shaded and sunny lounging space, and a 10' x 30' pool with a charming fountain that appears to flow from the hot tub. Splendore is a convenient haven for your St. John vacation, just 9 minutes from town and 12-15 minutes from the North Shore beaches.",
        "amenities": ["Near the ocean", "Ocean view", "Water view", "Swimming pool", "Heated private pool", "Hot tub", "Air conditioning", "Internet", "Wireless Internet", "TV", "Satellite or cable", "Stereo", "DVD player", "Books", "Video library", "Washer and dryer", "Parking", "No smoking", "Telephone", "Linens provided", "Towels provided", "Iron and board", "Hair dryer", "Living room", "Dishwasher", "Refrigerator", "Stove", "Oven", "Microwave", "Weber grill", "Coffee maker", "Toaster", "Pantry items", "Dishes and utensils", "Dining area", "Balcony", "Deck / patio", "Exterior lighting"]
    },
    {
        "slug": "surfside",
        "name": "Surfside",
        "image": "villa-photos/surfside/surfside1.jpg",
        "rooms": 3, "baths": 3, "sleeps": 6,
        "type": "Oceanfront Family Villa",
        "short_desc": "3-bedroom oceanfront villa perfect for families, with pool and easy beach access in St. John, USVI.",
        "description": "Surfside is a welcoming 3-bedroom oceanfront villa designed with families in mind. Located on St. John's beautiful north shore, this villa offers easy access to some of the Caribbean's most celebrated beaches including Trunk Bay, Cinnamon Bay, and Maho Bay. The spacious living area opens to a large pool deck with panoramic ocean views, making it easy to keep an eye on the kids while relaxing in comfort. Each bedroom is air-conditioned with its own bathroom, ensuring privacy for everyone. The fully equipped kitchen makes meal prep a breeze, and the outdoor grill is perfect for evening barbecues. Surfside combines the comforts of home with the beauty of a St. John oceanfront location. Surfside is located at Reef Bay with a waterfront setting, a 21 x 12 pool, hot tub, air-conditioned bedrooms, and a 15-18 minute drive to Cruz Bay.",
        "amenities": ["2 Kings", "1 Queen", "Property Location: Reef Bay", "Proximity: Waterfront", "Property Size: 2600 sq ft", "Year Property Complete: 2002", "Beach: Reef Bay", "Pool: Yes", "Pool Dimensions: 21 x 12 x 4 - 5 ft deep", "Hot Tub: Yes", "Air Conditioning: Yes, bedrooms only", "Children: Welcome", "Wifi: Yes", "Cable TV", "DVD Player", "Stereo with CD", "Toaster", "Coffeemaker", "Blender", "Safe for Valuables", "BBQ Gas Grill", "Washer & Dryer", "Beach Chairs", "Beach Towels", "Beach Cooler", "Iron & Ironing Board", "Hairdryer", "Linens & Bath Towels"]
    },
    {
        "slug": "seaside-breeze",
        "name": "Seaside Breeze",
        "image": "villa-photos/seaside-breeze/1.jpg",
        "rooms": 4, "baths": 3, "sleeps": 8,
        "type": "Beachfront Villa in Coral Bay",
        "short_desc": "Beachfront 4-bedroom villa in Coral Bay with pool, expansive decks, A/C bedrooms, and direct access to the Caribbean.",
        "description": "Seaside Breeze is a spacious beachfront villa in Coral Bay with 3700 sq/ft of interior space and 1740 sq/ft of exterior decks. It comfortably accommodates 8 guests in 4 air-conditioned bedrooms with 3 baths. Floor to ceiling windows, coral stone floors, an open floor plan, cedar woodwork, and a Bluetooth audio system with 8 zoned speakers create a cheerful and easy living space. Seaside Breeze sits just steps from a sandy beach and the clear Caribbean water where guests can swim, snorkel, kayak, paddle board, or go boating from the front yard.",
        "amenities": ["Beachfront", "Private pool", "Full kitchen", "Air conditioning", "WiFi", "4 A/C bedrooms", "Parking", "Expansive decks", "Gas BBQ grill"]
    },
    {
        "slug": "cinnamon-ridge",
        "name": "Cinnamon Ridge",
        "image": "villa-photos/cinnamon-ridge/1.jpg",
        "rooms": 5, "baths": 5, "sleeps": 10,
        "type": "Luxury Villa with Pool and Hot Tub",
        "short_desc": "HGTV's 2020 Caribbean House of the Year, Cinnamon Ridge is an elegant 5-bedroom, 5-bath St. John villa with pool, hot tub, and Caribbean views.",
        "description": "Cinnamon Ridge was chosen as HGTV's Caribbean House of the Year in 2020. The villa is an elegant 5-bedroom, 5-bath home with a pool and hot tub. The villa was completely renovated in 2019 and the results are stunning. From top to bottom, every aspect of this home was designed with a guest's comfort in mind. The home has a gated entrance, and you approach the villa from below and drive up to the parking area on the upper level. You will then follow the tropical walkway, which is beautifully accented with colorful flowers that you will enjoy as you make your way to the front entrance. Once you open your front door, you will be in awe as your eyes will be immediately drawn to the wall of glass that looks out to the ever-changing colors of the Caribbean blue seas. The centerpiece of Cinnamon Ridge is the great room, which includes your kitchen, living and dining area, all of which look out to the gorgeous views. On opposite sides of the great room are the two primary bedrooms, each with its private en-suite bathroom. There is an interior staircase down to the lower level, which includes three additional guest bedrooms and en-suite bathrooms. From every room in this home, you have the spectacular views that will take your breath away. On the far left of the home is your expansive sun deck, which includes your private pool, hot tub, covered outside seating and wet bar area with a flat screen TV. If you are someone that prefers to have a heated pool, this amenity can be added to your reservation at an additional cost of $62 per day. Be sure to mention this at the time you make your reservation so everything will be set for your arrival. If you are dreaming of a St. John getaway, make your reservations now for Cinnamon Ridge. Perfect for couples, families and everyone looking for an amazing island retreat.",
        "amenities": ["HGTV's Caribbean House of the Year 2020", "5 bedrooms", "5 bathrooms", "Private pool", "Hot tub", "Optional heated pool for $62 per day", "Gated entrance", "Caribbean views from every room", "Full kitchen", "Air conditioning", "WiFi", "Parking", "Wet bar area with flat screen TV"]
    },
    {
        "slug": "rainbow-beach-house",
        "name": "Rainbow Beach House",
        "image": "villa-photos/rainbow-beach-house/1.webp",
        "rooms": 4, "baths": 4, "sleeps": 8,
        "type": "Beachfront Villa",
        "short_desc": "Renovated 4-bedroom, 4-bath beachfront St. John home with pool, pool spa, Johnson Bay views, and direct beach access.",
        "description": "Rainbow Beach House is a beautiful 4 bedroom 4 bath beachfront home with a pool and pool spa. The home was completely renovated in 2018 and welcomes guests with a warm, inviting atmosphere. The two-level design has interior access, an open great room with kitchen, living and dining areas, screened sliding glass doors to the pool deck, two upper bedrooms, two lower bedrooms, and beach-level access for swimming and snorkeling. Guests can also rent paddle boards or kayaks during their stay. No matter what time of year you travel, you can enjoy the sounds of the surf and the relaxing beachfront atmosphere.",
        "amenities": ["Beachfront home", "4 bedrooms", "4 bathrooms", "Pool", "Pool spa", "Direct beach access", "Johnson Bay views", "Dish Satellite TV", "DVD Player", "Safe for valuables", "BBQ Gas Grill", "Washer & Dryer", "Beach chairs", "Beach towels", "Beach cooler"]
    },
    {
        "slug": "solemare",
        "name": "Solemare",
        "image": "villa-photos/solemare/1.jpg",
        "rooms": 3, "baths": "3.5", "sleeps": 8,
        "type": "Mediterranean Style Villa in Coral Bay",
        "short_desc": "Very elegant, custom built Mediterranean style villa in Coral Bay with pool, A/C, 4300 sq. ft., and parking for 2-3 jeeps.",
        "description": "Very elegant, custom built Mediterranean style villa in Coral Bay. This 3-bedroom villa is a true diamond that glitters in the hills above Coral Bay. Solemare (meaning sun and sea) was the dreamhouse of a successful Italian American who grew up in Italy and frequently vacationed in the Mediterranean islands. He fell in love with St. John and retained a renown St. John architect to custom design a classic Mediterranean style villa. He wanted a villa that would capture the romance and elegance of the villas he vacationed in on the Italian coast. With its timeless beauty and style, we think Solemare succeeds in bringing the ageless magnificence of Italy to St. John. We also think that this is a unique villa that you'll fall in love with, as intended by Corrado Bruzzo. Solemare is a large (4300 sq/ft) villa that consists of 2 buildings - a main house and a pool house - both with two levels and with a covered walkway connecting the two buildings. You park above the villa and descend a flight of stairs down to the upper deck of the main house. Mahogany French doors lead from the upper deck into the gourmet kitchen. The handsome kitchen adjoins the spacious (1000 sq/ft) and comfortable great room, which is accessorized with fascinating antiquities and hung with colorful artwork that was commissioned by one artist expressly for Solemare. Even in today's Italy, the dinner table is a place of lively conversation and relaxed dining that sometimes stretches for hours. With that idea in mind, Solemare's dining table was located in a stunning setting with a majestic view that might keep you fixated around the table for hours. There is a half bath off the great room, and a marble interior stairway leads down to the bedroom on the lower level of the main house. Exterior stairs off the upper deck also lead down to the pool, pool deck and the main house lower bedrooms. The pool house contains two large king bedrooms, both with exquisite marble and mahogany bathrooms. A covered walkway leads to the master bedroom on the upper level, while exterior stairs lead down to the pool deck and the lower bedroom of the pool house. Because this is Solemare, the master bedroom and the main house bedroom both have solarium showers so you can shower with the sun (and the stars).",
        "amenities": ["TV with Blu Ray DVD for watching movies", "Toaster", "Blender", "Coffeemaker", "Washer & Dryer", "Safe for Valuable", "BBQ Gas Grill", "Beach Chairs", "Beach Towels", "Beach Cooler", "Iron & Ironing Board", "Hairdryer", "Linens & Bath Towels", "Beds: 3", "Bed Description: 3 Kings", "Bathrooms: 3.5", "Pool: Yes", "Air Conditioning: Yes, Living area & 3 bedrooms - Pagoda does not have a/c", "Hot Tub: No", "Children: Welcome", "Wifi: Yes", "Ipod Connectivity: Yes"]
    },
    {
        "slug": "mystical-mermaid",
        "name": "Mystical Mermaid",
        "image": "mystical-mermaid.jpg",
        "rooms": 2, "baths": 2, "sleeps": 4,
        "type": "Luxury Stone Villa",
        "short_desc": "Unique luxury stone villa close to beaches with whimsical decor and mountain views in St. John.",
        "description": "Welcome home to Mystical Mermaid, a consistently 5-star rated villa close to St. John's world-famous beaches. This luxury stone villa has been tastefully updated in today's Caribbean colours and finished to the highest standards, with two interior bedrooms, two baths, and a salt water pool and hot tub looking out to mountain views. The owner's suite has a king bed, A/C, satellite TV and a large ensuite bathroom; the second bedroom has two twin beds that convert to a king, A/C and its own ensuite. The open floor plan takes in the kitchen, living and dining rooms — the kitchen fully equipped with top-end appliances, cookware, glassware and dishes, the dining room seating six, and the living room comfortably seating six with A/C, an entertainment centre and WiFi. The pool veranda opens off the living room, dining room and owner's suite, with ample outdoor seating around the pool and its mermaid fountain. The villa is surrounded by lush gardens and Bismarckia palms, with a pillared stone entry and a large flat turnaround car park for several jeeps.",
        "amenities": ["Salt water pool & hot tub", "Mountain views", "Lush gardens", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Outdoor deck"]
    },
    {
        "slug": "island-rider",
        "name": "Island Rider",
        "image": "villa-photos/island-rider/Rider1.jpg",
        "rooms": 4, "baths": 6, "sleeps": 8,
        "type": "Point Rendezvous Villa",
        "short_desc": "Fully renovated 4-bedroom Point Rendezvous villa with verandas, solar heated pool and spa, and views over Klein Bay.",
        "description": "Located in the exclusive enclave of Point Rendezvous on the south shore of St. John, Island Rider is a fully renovated villa that sits upon the open breezy hillside above Klein Bay. Island Rider's sprawling verandas overlook the gentle curves of Rendezvous Bay and Ditliff Point. This beautifully appointed four bedroom home holds all of the charm of the old St. John with beautiful stone work while providing all of the modern amenities one could expect in a luxury home including a fabulous solar heated pool and spa. This villa sets the standards in modern vacation accommodations with a state of the art gourmet kitchen and open dining room for entertaining, as well as a separate media room to relax in for a night of watching movies. The spacious open plan living area opens to spectacular views south on one side and an expansive covered patio for grilling in back. There are four distinct outdoor seating areas that accommodate 8 guests for meals: The Veranda, Courtyard, Pool Deck and Lower Spa Deck. Designed to be the ultimate personal retreat, Island Rider is the perfect getaway for friends or families with adult children. Located just five minutes from Cruz Bay, it has convenient access to town and the North Shore beaches but still provides the seclusion you want for your island getaway. Island Rider will offer you a vacation you will never forget.",
        "amenities": ["Point Rendezvous hillside location", "Sprawling verandas", "Solar heated pool and spa", "Gourmet kitchen", "Separate media room", "Four outdoor seating areas", "Internet access", "Cable/Dish TV", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Beach bag", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker"]
    },
    {
        "slug": "mango-bay",
        "name": "Mango Bay",
        "image": "villa-photos/mango-bay/mango1.jpg",
        "rooms": 4, "baths": "4.5", "sleeps": 8,
        "type": "Luxury Villa with BVI Views",
        "short_desc": "4-bedroom, 4.5-bath Catherineberg villa with four king suites, expansive decks, pool, Sonos sound, and unforgettable British Virgin Islands views.",
        "description": "The view from Mango Bay across to the British Virgin Islands will steal your breath away. Whether you're taking it all in from the sundeck, the pool, the bedrooms, the great room, or even the outdoor showers, you will remember it for the rest of your life. Mango Bay offers the ultimate in-island luxury, with four king-bedroom suites, expansive decks, and an open floor-plan living/dining area. The kitchen is well-equipped, and the sumptuously furnished great room is perfect for a relaxing evening. Mango Bay is ideally located in the center of St. John, with Cruz Bay, Coral Bay, and the North Shore beaches just a few minutes down the road.",
        "amenities": ["Neighborhood: Catherineberg", "4 king suites", "4.5 baths", "Pool: 18' x 12'", "Portable A/C units in bedrooms", "Gated driveway", "Sonos Sound System", "Gas grill", "Washer and dryer", "Coffee maker"]
    },
    {
        "slug": "vista-caribe",
        "name": "Vista Caribe",
        "image": "villa-photos/vista-caribe/1.webp",
        "rooms": 4, "baths": 4, "sleeps": 8,
        "type": "Great Cruz Bay Panoramic Villa",
        "short_desc": "Luxury 4-bedroom Vista Caribe villa above Great Cruz Bay with sweeping decks, plush outdoor living spaces, and incomparable Caribbean views.",
        "description": "One sunset seen from the sweeping decks of Vista Caribe and you’ll be head over heels. This luxurious island home is the ideal choice if you’re a fan of privacy, comfort, and incomparable Caribbean vistas. In addition to a beautifully appointed great room, expansive modern kitchen, and a laundry list of modern amenities, the villa offers a stunning pool area and an array of plush outdoor living spaces. Three richly furnished bedroom suites are attached to the main house, and a fourth sits detached and includes a kitchenette and seating area. Vista Caribe is nestled high above Great Cruz Bay in the Virgin Grand Estates, a prestigious residential enclave envied for its gorgeous island breezes and its convenient central location. Just a few minutes of driving and you’ll be enjoying the laid-back bustle of Cruz Bay or the breathtakingly beautiful North Shore beaches.",
        "amenities": ["Air Conditioning", "Clothes Dryer", "Hair Dryer", "IPod ready", "Internet", "Linens Provided", "Towels Provided", "Internet access", "Cable/Dish TV", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Beach bag", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker"]
    },
    {
        "slug": "reef-break-vista",
        "name": "Reef Break Vista",
        "image": "villa-photos/reef-break-vista/1.webp",
        "header_image": "villa-photos/reef-break-vista/header-telegram-4197.jpg",
        "rooms": 4, "baths": 3, "sleeps": 10,
        "type": "Waterfront Pool Home",
        "short_desc": "Attractive 4-bedroom, 3-bath Caribbean-style home with private pool, connecting decks, and Ram's Head sunrise views.",
        "gallery": [
            "villa-photos/reef-break-vista/1.webp",
            "villa-photos/reef-break-vista/2.webp",
            "villa-photos/reef-break-vista/3.webp",
            "villa-photos/reef-break-vista/4.webp",
            "villa-photos/reef-break-vista/5.webp",
        ],
        "description": "Reef Break Vista is an attractive 4 bedroom 3 bath home with a private pool. This newly refurnished home has a casual Caribbean feel to it, which will welcome you the minute your walk through the front door. The home consists of 3 buildings, which are attached by connecting decks. The center building of the home is the main living area, which includes the open floor plan living, kitchen and dining area. Located to the left is the left cabana bedroom and attached bath. Off to the right of the main living area is your second cabana bedroom with attached bath. From the main level there is a staircase down to the pool and sun deck, and then a few more stairs down there is the lower sun deck and additional two bedrooms, which are connected by a Jack & Jill bathroom. No matter where you are standing, you are sure to enjoy the tropical breezes and breathtaking views of azure blue seas and green hillsides. If you are an early riser, you can wake up to the beautiful sunrise as it appears over Ram's Head in the distant horizon. If you are looking for a well priced home with an inviting tropical atmosphere, you have found it with Reef Break Vista. Perfect for families, couples and everyone looking for a casual Caribbean retreat.",
        "amenities": ["Internet access", "Cable/Dish TV", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Beach bag", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker", "A/C: Full", "Pool", "Linen service: Please call to arrange", "Whole-house Generator"],
        "reviews": [
            {
                "title": "AMAZING Property!!!",
                "body": "Fantastic - love the house and the view, especially at sunset, can't be beat.",
                "reviewer": "Whitney R.",
            },
            {
                "title": "Amazing view",
                "body": "We had the most amazing stay. Couldn't beat the pool and views. We came with both adults and kids and everyone had a great time. We can't wait to book again.",
                "reviewer": "Jeff M.",
            },
        ]
    },
    {
        "slug": "sea-forever",
        "name": "Sea Forever",
        "image": "sea-forever.jpg",
        "rooms": 5, "baths": "5.5", "sleeps": 10,
        "type": "Southwestern Shore Villa",
        "short_desc": "Completely re-built 5-bedroom St. John villa above the southwestern shore with panoramic views, pool, hot tub deck, outdoor audio, and full wireless coverage.",
        "description": "This villa's name has layers of meaning - not only can you see forever from its vantage point above St. John's southwestern shore, but you could also, happily, spend forever gazing at that incomparable panorama. Completely re-built and luxuriously appointed, Sea Forever has five one-bedroom suites, a gorgeous open-floor plan great room with a unique dining area, a free-form pool, a large hot tub on a separate large deck with a built-in grill station, and a pool side patio and wet bar area. Sea Forever has state of the art internet connectivity with complete wireless coverage throughout the villa. A full outdoor audio system, also covering the great room and master bedroom suite, handles your streaming music and completes the ambience. And no matter where in the house you are, you can always see that view. Sea Forever has plenty of parking area and is a quick drive to Cruz Bay's shops, restaurants, and bars, and not much further to the North Shore's glorious white sand beaches. Some come to St. John and spend as much time on the beaches and trails as possible. Others take it slow, spending their days floating in the pool and lounging in the sun. Whatever your vacation game plan, Sea Forever is an excellent place to start.",
        "description_paragraphs": [
            "This villa's name has layers of meaning - not only can you see forever from its vantage point above St. John's southwestern shore, but you could also, happily, spend forever gazing at that incomparable panorama. Completely re-built and luxuriously appointed, Sea Forever has five one-bedroom suites, a gorgeous open-floor plan great room with a unique dining area, a free-form pool, a large hot tub on a separate large deck with a built-in grill station, and a pool side patio and wet bar area. Sea Forever has state of the art internet connectivity with complete wireless coverage throughout the villa. A full outdoor audio system, also covering the great room and master bedroom suite, handles your streaming music and completes the ambience. And no matter where in the house you are, you can always see that view.",
            "Sea Forever has plenty of parking area and is a quick drive to Cruz Bay's shops, restaurants, and bars, and not much further to the North Shore's glorious white sand beaches. Some come to St. John and spend as much time on the beaches and trails as possible. Others take it slow, spending their days floating in the pool and lounging in the sun. Whatever your vacation game plan, Sea Forever is an excellent place to start.",
        ],
        "amenities": ["Internet access", "Cable/Dish TV", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Beach bag", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker", "A/C: Full", "Pool", "Linen service: Please call to arrange", "Hot tub", "Outdoor audio system", "Smart TVs in every room", "Whole-house generator"],
        "amenities_layout": "panel",
        "amenities_title": "Standard Amenities",
        "rates": {
            "modal_id": "rates-modal-sea-forever",
            "title": "Sea Forever Rates",
            "rows": [
                ("Winter 2024", "Jan 4th 2024 to Apr 14th 2024", ["2 per. $13,000 per week (USD)", "3-4 per. $13,500 per week (USD)", "5-6 per. $14,000 per week (USD)", "7-8 per. $14,500 per week (USD)", "9-10 per. $15,000 per week (USD)"]),
                ("Summer 2024", "Apr 15th 2024 to Dec 16th 2024", ["2 per. $10,000 per week (USD)", "3-4 per. $10,500 per week (USD)", "5-6 per. $11,000 per week (USD)", "7-8 per. $11,500 per week (USD)", "9-10 per. $12,000 per week (USD)"]),
                ("Winter 2025", "Jan 7th 2025 to Apr 13th 2025", ["2 per. $13,000 per week (USD)", "3-4 per. $13,500 per week (USD)", "5-6 per. $14,000 per week (USD)", "7-8 per. $14,500 per week (USD)", "9-10 per. $15,000 per week (USD)"]),
                ("Thanksgiving", "Nov 23rd 2024 to Nov 30th 2024", ["$14,500 per week (USD)"]),
                ("Christmas/New Years", "Dec 17th 2024 to Jan 6th 2025", ["$21,000 per week (USD)"]),
            ],
            "notes": ["Please note: Add 10% to Thanksgiving and President's Weeks."],
        },
        "reviews": [
            {
                "title": "Spectacular!",
                "body": "I have been visiting the island since 2000. This villa is truly spectacular! The best views! Such a thoughtful layout and attention to detail. Proud to show the island I love to friends from home.",
                "reviewer": "Sarah, Jay, Amelia & Alexander",
            },
            {
                "title": "Fabulous Sunrise & Sunset Views",
                "body": "The property is well located with fabulous views of St. Thomas and the smaller islets nearby; close enough to Cruz Bay for convenience but far enough from the energy to truly relax. Mike, the maintenance staff leader, Alex the pool and spa walla, and the cleaning crew were also commendable. The great room is perfect for larger groups, the outdoor public spaces are also inviting and the kitchen is well designed and adequately equipped. The master bedroom is outstanding ..",
                "reviewer": "Pablo",
            },
        ]
    },
    {
        "slug": "rhapsody",
        "name": "Rhapsody",
        "image": "rhapsody.jpg",
        "rooms": 5, "baths": "5.5", "sleeps": 10,
        "type": "Oceanfront Luxury Villa",
        "short_desc": "Special 5-bedroom, 5.5-bath luxury villa on the western shores of St. John with an infinity pool and oceanfront setting.",
        "description": "Villa Rhapsody St. John is a beautiful and very special 5-bedroom luxury vacation villa located on the western shores of St. John, U.S. Virgin Islands. Villa Rhapsody St. John is set in magnificent tropical surroundings on the cliffs just to the north of the entrance to Great Cruz Bay Harbor facing St. Thomas. Located on a 1/2 acre lot immediately adjacent to the ocean, a 16' x 32' spectacular infinity pool and immense pool deck command center stage. The Great House, and various living pods surround the infinity pool. This magnificent 5BR/5.5 bath villa sleeps up to 10 adults, plus additional beds for an additional 2 children accommodating a total of 12 (10 adults + 2 children). In the Rhapsody Great Room is a spacious living area, dining area, well stocked kitchen, and small office area. A state-of-the-art fiber connection powers high speed WiFi internet and satellite TV throughout. An HD entertainment center and sound system with large screen HDTV is enjoyed in the Great Room living area. Whether for a romantic hideaway, or a festive special occasion, Villa Rhapsody St. John offers the spaciousness of a Caribbean estate with ultra luxury accommodations, a magnificent and romantic infinity pool and deck, a superb private setting - all floating above the turquoise Caribbean with the never ending surround sound of the ocean directly below you.",
        "description_paragraphs": [
            "Villa Rhapsody St. John is a beautiful and very special 5-bedroom luxury vacation villa located on the western shores of St. John, U.S. Virgin Islands.",
            "Villa Rhapsody St. John is set in magnificent tropical surroundings on the cliffs just to the north of the entrance to Great Cruz Bay Harbor facing St. Thomas. Located on a 1/2 acre lot immediately adjacent to the ocean, a 16' x 32' spectacular infinity pool and immense pool deck command center stage. The Great House, and various living pods surround the infinity pool.",
            "This magnificent 5BR/5.5 bath villa sleeps up to 10 adults, plus additional beds for an additional 2 children accommodating a total of 12 (10 adults + 2 children). In the Rhapsody Great Room is a spacious living area, dining area, well stocked kitchen, and small office area. A state-of-the-art fiber connection powers high speed WiFi internet and satellite TV throughout. An HD entertainment center and sound system with large screen HDTV is enjoyed in the Great Room living area.",
            "Whether for a romantic hideaway, or a festive special occasion, Villa Rhapsody St. John offers the spaciousness of a Caribbean estate with ultra luxury accommodations, a magnificent and romantic infinity pool and deck, a superb private setting - all floating above the turquoise Caribbean with the never ending surround sound of the ocean directly below you.",
        ],
        "amenities": ["Internet access", "Cable/Dish TV", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Beach bag", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker", "A/C: Full", "Pool", "Linen service: Please call to arrange", "Whole-house Generator"],
        "rates": {
            "modal_id": "rates-modal-rhapsody",
            "title": "Rhapsody Rates",
            "rows": [
                ("Winter 2024", "Jan 4, 2024 to Apr 14, 2024", ["2 per. $10,500 per week (USD)", "3-4 per. $10,500 per week (USD)", "5-6 per. $11,500 per week (USD)", "7-8 per. $12,500 per week (USD)", "9-10 per. $13,500 per week (USD)"]),
                ("Summer 2024", "Apr 15, 2024 to Dec 16, 2024", ["2 per. $7,500 per week (USD)", "3-4 per. $7,500 per week (USD)", "5-6 per. $8,500 per week (USD)", "7-8 per. $9,500 per week (USD)", "9-10 per. $10,500 per week (USD)"]),
                ("Winter 2025", "Jan 7, 2025 to Apr 13, 2025", ["2 per. $10,500 per week (USD)", "3-4 per. $10,500 per week (USD)", "5-6 per. $11,500 per week (USD)", "7-8 per. $12,500 per week (USD)", "9-10 per. $13,500 per week (USD)"]),
                ("Thanksgiving", "Nov 23, 2024 to Nov 30, 2024", ["$10,500 per week (USD)"]),
                ("Christmas/New Years", "Dec 17, 2024 to Jan 6, 2025", ["$16,000 per week (USD)"]),
            ],
            "notes": ["Please note: Add 10% to Thanksgiving and President's Weeks."],
        },
        "reviews": [
            {
                "title": "AMAZING Property!!!",
                "body": "Fantastic - love the house and the view, especially at sunset, can't be beat.",
                "reviewer": "Whitney R.",
            },
            {
                "title": "Amazing view",
                "body": "We had the most amazing stay. Couldn't beat the pool and views. We came with both adults and kids and everyone had a great time. We can't wait to book again.",
                "reviewer": "Jeff M.",
            },
        ]
    },
    {
        "slug": "waterfall",
        "name": "Waterfall",
        "image": "waterfall.jpg",
        "rooms": 3, "baths": "3.5", "sleeps": 6,
        "type": "Fish Bay Villa",
        "short_desc": "Destination 3-bedroom Fish Bay villa with St. Croix views, solar-heated infinity pool, spa, gym, office, and dining gazebo.",
        "description": "Waterfall is a destination villa that guests often find difficult to leave. There's the enduring lure of the gorgeous National Park beaches and beautiful views of Fish Bay and beyond - all the way to St. Croix. It's a spectacular villa with privacy and amenities galore. Sit beneath the waterfall in one of St. John's largest solar-heated, infinity edge swimming pools and feel the tranquility. After an invigorating workout in the air-conditioned gym, relax in the poolside six-person spa while you contemplate dining under the stars in the romantic dining gazebo. This is a villa that casts a spell and makes you want to never leave! Waterfall offers both indoor and outdoor lounging areas. There are flat screen LCD TV's in the bedrooms and the living room. It was designed for easy living with two bedrooms having inside access and on the same level as the pool and spa. All 3 bedrooms are equal-sized with beautiful water views and ensuite baths. An entry ramp from the driveway simplifies access for those who find stairs difficult. A fully-equipped, air-conditioned office with whole-house WIFI is available for those who need to stay connected. A large, automatic 28 kilowatt generator keeps everything running smoothly when power outages occur. Children over 8 welcome.",
        "description_paragraphs": [
            "Waterfall is a destination villa that guests often find difficult to leave. There's the enduring lure of the gorgeous National Park beaches and beautiful views of Fish Bay and beyond - all the way to St. Croix. It's a spectacular villa with privacy and amenities galore. Sit beneath the waterfall in one of St. John's largest solar-heated, infinity edge swimming pools and feel the tranquility. After an invigorating workout in the air-conditioned gym, relax in the poolside six-person spa while you contemplate dining under the stars in the romantic dining gazebo. This is a villa that casts a spell and makes you want to never leave!",
            "Waterfall offers both indoor and outdoor lounging areas. There are flat screen LCD TV's in the bedrooms and the living room. It was designed for easy living with two bedrooms having inside access and on the same level as the pool and spa. All 3 bedrooms are equal-sized with beautiful water views and ensuite baths. An entry ramp from the driveway simplifies access for those who find stairs difficult. A fully-equipped, air-conditioned office with whole-house WIFI is available for those who need to stay connected. A large, automatic 28 kilowatt generator keeps everything running smoothly when power outages occur.",
            "Children over 8 welcome.",
        ],
        "amenities": ["Internet access", "Gas grill", "Bed linen and bath towels", "Beach towels", "Beach chairs", "Beach coolers", "Outdoor shower", "Safes for valuables", "Hair dryers", "Washer and dryer", "Coffee maker", "Smart TV's", "Linen service", "AC: Full", "Home gym", "Home office", "Children over 8 welcome"],
        "amenities_layout": "panel",
        "rates": {
            "modal_id": "rates-modal-waterfall",
            "title": "Waterfall Rates",
            "rows": [
                ("Summer 2025", "May 3rd 2025 to Dec 16th 2025", ["2 per. $6000 per week (USD)", "3-4 per. $6000 per week (USD)", "5-6 per. $6000 per week (USD)"]),
                ("Winter 2026", "Jan 5th 2026 to May 2nd 2026", ["2 per. $7000 per week (USD)", "3-4 per. $7000 per week (USD)", "5-6 per. $7000 per week (USD)"]),
                ("Thanksgiving", "Nov 22nd 2025 to Nov 29th 2025", ["$6500 per week (USD)"]),
                ("Christmas/New Years", "Dec 17th 2025 to Jan 4th 2026", ["$8500 per week (USD)"]),
            ],
            "notes": ["Please note: Add 10% to Thanksgiving and President's Weeks."],
        },
        "reviews": [
            {
                "title": "Spectacular house!",
                "body": "Spectacular house with an outstanding view. Best villa we've ever stayed at on St. John and we've stayed at many. Everything was immaculate and really appreciated. The Fish Bay location - away from it all but still convenient to town and beaches. Our new favorite place on St. John!",
                "reviewer": "The Kleinberg & Coleman's"
            },
            {
                "title": "Spectacular vacation",
                "body": "Waterfall is a magnificent location for a family vacation! Out family of 5 was so happy to stay here, the pool and hot tub offer an incredibly relaxing atmosphere, along with the nice winter weather and tranquility of the location. The house is in a very peaceful and quiet area, with an awesome ocean view to the south.",
                "reviewer": "Robert D. G."
            },
            {
                "title": "Second Stay!",
                "body": "Fantastic Week - Beautiful weather, great food, good rum drinks, nice villa with a wonderful view! We really enjoyed the sunset sail on our last night out to the East End. We will be back! Our second stay at Waterfall! We love it. Great week all the beaches we visited on the North Shore, we had fun hiking. And we had a special trip to Virgin Gorda on Bad Kitty. Be back again.",
                "reviewer": "The Strouss Family, Ipswich Mass."
            },
            {
                "title": "Wonderful family vacation",
                "body": "My husband and I stayed at Waterfall with our 3 teenage daughters. We had a wonderful time and the house exceeded our expectations. We grilled a few nights and the well-stocked kitchen made it easy and enjoyable. The beds are comfortable and the AC in the bedrooms worked well. The living area stayed cool with the open doors and breeze. The pool and hot tub were used everyday. I particularly enjoyed star gazing from the hot tub at night. The gazebo was a favorite for eating dinner and breakfast. The owners provided snorkeling equipment and beach chairs. The 3rd bedroom is downstairs and can only be accessed from the outside. Which may be a problem for families with younger children. I highly recommend staying at Waterfall and hope to return soon.",
                "reviewer": "TravelinMom61"
            },
            {
                "title": "Our favorite place!",
                "body": "Our favorite place on the island! The pool was hard to leave, but we enjoyed traveling to the beaches, especially to swim and snorkel on the reef at Hawknest. Took a trip to nearby Reef Bay and Pebble Beach which is a treasure. Fish Bay and Waterfall are truly special places.",
                "reviewer": "The Strouss family"
            }
        ]
    }
]

# All villa slugs for internal linking
all_slugs = [v["slug"] for v in villas]

NAV_HTML = """    <header>
        <div class="container nav-wrapper">
            <a href="../index.html" class="logo">Seaview Homes</a>
            <button class="hamburger" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <nav class="nav-menu">
                <a href="../index.html" class="nav-link">Home</a>
                <a href="../villas.html" class="nav-link">Villas</a>
                <a href="../about.html" class="nav-link">About</a>
                <a href="../things-to-do.html" class="nav-link">Things To Do</a>
                <a href="../services.html" class="nav-link">Services</a>
                <a href="../faq.html" class="nav-link">FAQ</a>
                <a href="../contact.html" class="nav-link">Contact</a>
            </nav>
        </div>
    </header>"""

FOOTER_HTML = """    <footer>
        <div class="container">
            <div class="footer-links">
                <a href="../index.html">Home</a>
                <a href="../villas.html">Villas</a>
                <a href="../about.html">About</a>
                <a href="../things-to-do.html">Things To Do</a>
                <a href="../services.html">Services</a>
                <a href="../faq.html">FAQ</a>
                <a href="../contact.html">Contact</a>
            </div>
            <div class="footer-social">
                <a href="https://www.facebook.com/SeaviewHomes.StJohn" target="_blank" rel="noopener" aria-label="Facebook">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
                <a href="https://www.instagram.com/seaview_homes/" target="_blank" rel="noopener" aria-label="Instagram">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                </a>
                <a href="https://in.pinterest.com/seaviewhomesvacation/" target="_blank" rel="noopener" aria-label="Pinterest">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.017 0C5.396 0 .029 5.367.029 11.987c0 5.079 3.158 9.417 7.618 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.663.967-2.911 2.168-2.911 1.024 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.417 2.561-5.417 5.211 0 1.033.397 2.143.895 2.745.099.12.112.225.083.348-.09.375-.293 1.199-.334 1.367-.053.223-.175.271-.402.165-1.499-.698-2.436-2.895-2.436-4.658 0-3.794 2.755-7.281 7.951-7.281 4.176 0 7.421 2.977 7.421 6.958 0 4.154-2.62 7.495-6.253 7.495-1.222 0-2.371-.635-2.765-1.385l-.751 2.862c-.272 1.047-1.007 2.361-1.502 3.162C9.57 23.812 10.779 24 12.017 24c6.621 0 11.988-5.367 11.988-11.987C24.005 5.367 18.638 0 12.017 0z"/></svg>
                </a>
            </div>
            <p>Seaview Vacation Homes, Inc. | 5000 Estate Enighed, PMB # 350, St. John VI 00830 | 1-340-776-6805 | info@seaviewhomes.com</p>
            <p>&copy; 2026 Seaview Vacation Homes, Inc. All rights reserved.</p>
        </div>
    </footer>"""

def generate_html(villa, all_villas):
    slug = villa["slug"]
    name = villa["name"]
    image = villa["image"]
    rooms = villa["rooms"]
    baths = villa["baths"]
    sleeps = villa.get("sleeps", rooms * 2)
    vtype = villa["type"]
    short_desc = villa["short_desc"]
    desc = villa["description"]
    description_paragraphs = villa.get("description_paragraphs")
    amenities = villa["amenities"]
    amenities_layout = villa.get("amenities_layout")
    gallery = villa.get("gallery", [])
    header_image = villa.get("header_image")
    reviews = villa.get("reviews", [])
    rates = villa.get("rates")
    
    title = f"{name} | {rooms} BR {vtype} in St. John USVI | Seaview Homes"
    canonical = f"{SITE_URL}/villas/{slug}"
    image_path = f"assets/img/{image}" if image.startswith("villa-photos/") else f"{IMG_BASE}/{image}"
    image_url = f"{SITE_URL}/{image_path}"
    
    # Build amenities JSON-LD
    amenities_json = json.dumps([
        {"@type": "LocationFeatureSpecification", "name": a}
        for a in amenities
    ])
    
    # Build amenities HTML
    amenities_html = "\n                    ".join([
        f'<li style="padding: 0.5rem 0; border-bottom: 1px solid #eee; list-style: none;">✓ {a}</li>'
        for a in amenities
    ])
    
    # Build related villas (pick 4 different ones)
    related = [v for v in all_villas if v["slug"] != slug][:4]
    related_html = "\n                    ".join([
        f'<a href="{v["slug"]}.html" class="nav-link" style="display: inline-block; margin: 0.3rem; padding: 0.5rem 1rem; background: var(--color-bg-alt); border-radius: 6px; font-size: 0.9rem;">{v["name"]}</a>'
        for v in related
    ])

    gallery_html = ""
    if gallery:
        gallery_items = "\n                ".join([
            f'<img src="../assets/img/{img}" alt="{name} St. John villa photo {idx}" loading="lazy" style="width: 100%; height: 180px; object-fit: cover; border-radius: 6px; display: block;">'
            for idx, img in enumerate(gallery, start=1)
        ])
        gallery_html = f"""

        <!-- Photo Gallery -->
        <section class="container">
            <div class="section-title">
                <h2>Photo Gallery</h2>
            </div>
            <div class="villa-gallery" style="display: grid;">
                {gallery_items}
            </div>
        </section>"""

    if description_paragraphs:
        overview_body_html = '<div class="villa-description">\n                    ' + "\n                    ".join([
            f"<p>{html_lib.escape(paragraph, quote=False)}</p>"
            for paragraph in description_paragraphs
        ]) + "\n                </div>"
    else:
        overview_body_html = f'<p style="font-size: 1.1rem; line-height: 1.8; color: var(--color-text);">{desc}</p>'

    rates_button_html = ""
    rates_modal_html = ""
    if rates:
        modal_id = rates["modal_id"]
        rates_button_html = f"""

        <div style="text-align: center; margin: 2rem 0;"><button class="rates-btn" onclick="document.getElementById('{html_lib.escape(modal_id)}').classList.add('active')">View Rates</button></div>"""
        rate_rows = "\n                        ".join([
            (
                f"<tr><td>{html_lib.escape(season, quote=False)}<br><small>{html_lib.escape(dates, quote=False)}</small></td>"
                f"<td>{'<br>'.join(html_lib.escape(rate, quote=False) for rate in row_rates)}</td></tr>"
            )
            for season, dates, row_rates in rates["rows"]
        ])
        rate_notes = "\n                    ".join([
            f"<p>{html_lib.escape(note, quote=False)}</p>"
            for note in rates.get("notes", [])
        ])
        rates_modal_html = f"""

        <div class="rates-modal-overlay" id="{html_lib.escape(modal_id)}" onclick="if(event.target===this)this.classList.remove('active')">
            <div class="rates-modal">
                <button class="rates-modal-close" onclick="this.closest('.rates-modal-overlay').classList.remove('active')">&times;</button>
                <h2>{html_lib.escape(rates["title"], quote=False)}</h2>
                <table class="rates-table">
                    <thead>
                        <tr><th>Season</th><th>Rates</th></tr>
                    </thead>
                    <tbody>
                        {rate_rows}
                    </tbody>
                </table>
                <div class="rates-fees">
                    {rate_notes}
                </div>
            </div>
        </div>"""

    if amenities_layout == "panel":
        amenities_title = villa.get("amenities_title", "General Amenities")
        panel_items = "\n                        ".join([
            f"<li>{html_lib.escape(amenity, quote=False)}</li>"
            for amenity in amenities
        ])
        amenities_section_html = f"""

        <!-- Amenities -->
        <section class="amenities-section">
            <div class="container">
                <div class="section-title">
                    <h2>Amenities &amp; Features</h2>
                    <p>Everything you need for a perfect St. John stay.</p>
                </div>
                <div class="amenities-panel">
                    <h2>{html_lib.escape(amenities_title, quote=False)}</h2>
                    <ul>
                        {panel_items}
                    </ul>
                </div>
            </div>
        </section>"""
    else:
        amenities_section_html = f"""

        <!-- Amenities -->
        <section style="background: var(--color-bg-alt);">
            <div class="container">
                <div class="section-title">
                    <h2>Amenities &amp; Features</h2>
                    <p>Everything you need for a perfect St. John stay.</p>
                </div>
                <div style="max-width: 600px; margin: 0 auto;">
                    <ul style="padding: 0; margin: 0;">
                    {amenities_html}
                    </ul>
                </div>
            </div>
        </section>"""

    header_photo_html = ""
    if header_image:
        header_photo_html = f"""
    <div class="villa-page-header-photo" aria-label="{name} header photo">
        <img src="../assets/img/{header_image}" alt="{name} header photo" width="1280" height="600">
    </div>
"""

    reviews_html = ""
    if reviews:
        review_items = "\n                ".join([
            (
                '<div style="background: var(--color-bg-alt); padding: 2rem; border-radius: 8px; border-left: 4px solid var(--color-primary);">'
                f'<h3 style="margin-bottom: 0.75rem;">{html_lib.escape(review["title"], quote=False)}</h3>'
                f'<p style="font-style: italic; color: var(--color-text); margin-bottom: 1rem;">"{html_lib.escape(review["body"], quote=False)}"</p>'
                f'<p style="font-weight: 600; color: var(--color-primary); text-align: right;">- {html_lib.escape(review["reviewer"], quote=False)}</p>'
                '</div>'
            )
            for review in reviews
        ])
        reviews_html = f"""

        <!-- Reviews -->
        <section class="container">
            <div class="section-title">
                <h2>Guest Reviews</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 3rem;">
                {review_items}
            </div>
        </section>"""
    
    schema = {
        "@context": "https://schema.org",
        "@type": "LodgingBusiness",
        "name": name,
        "description": short_desc,
        "numberOfRooms": rooms,
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a} for a in amenities],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "St. John",
            "addressRegion": "VI",
            "postalCode": "00830",
            "addressCountry": "US"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 18.335,
            "longitude": -64.75
        },
        "url": canonical,
        "image": image_url,
        "priceRange": "$$-$$$$",
        "parentOrganization": {
            "@type": "LodgingBusiness",
            "name": "Seaview Vacation Homes, Inc.",
            "url": SITE_URL
        }
    }
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO Meta Tags -->
    <title>{title}</title>
    <meta name="description" content="{short_desc}">
    <meta name="keywords" content="{name}, St John villa, {vtype.lower()}, {rooms} bedroom villa St John, USVI vacation rental, Seaview Homes">
    <link rel="canonical" href="{canonical}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{name} | St. John Villa Rental">
    <meta property="og:description" content="{short_desc}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Seaview Homes">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{name} | St. John Villa Rental">
    <meta name="twitter:description" content="{short_desc}">
    <meta name="twitter:image" content="{image_url}">
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CLHXWEGPN2"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-CLHXWEGPN2');
    </script>
    
    <!-- CSS -->
    <link rel="stylesheet" href="../css/style.css">
    
    <!-- Schema.org -->
    <script type="application/ld+json">
    {json.dumps(schema, indent=2)}
    </script>
</head>
<body>
{NAV_HTML}
{header_photo_html}

    <main>
        <!-- Hero -->
        <section class="hero" style="height: 60vh; min-height: 350px; background: linear-gradient(rgba(0,30,60,0.2), rgba(0,50,100,0.3)), url('../{image_path}') center/cover no-repeat;">
            <div class="hero-content container">
                <h1>{name}</h1>
                <p style="font-size: 1.2rem; color: white; margin-bottom: 1rem;">{vtype} in St. John, USVI</p>
                <p style="color: rgba(255,255,255,0.9);">{rooms} BR | {baths} BA | Sleeps {sleeps}</p>
            </div>
        </section>

        <!-- Description -->
        <section class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="overview-heading">
                    <h2>Overview</h2>
                    <div class="overview-specs" aria-label="Villa overview details">
                        <span class="overview-spec"><svg class="overview-icon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4v16"/><path d="M2 10h20"/><path d="M22 8v12"/><path d="M6 10V7a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3"/></svg> Beds {rooms}</span>
                        <span class="overview-spec"><svg class="overview-icon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 4 8 6"/><path d="M17 19v2"/><path d="M7 19v2"/><path d="M2 12h20"/><path d="M7 12V5a3 3 0 0 1 5.1-2.1L14 4.8"/><path d="M5 12v3a4 4 0 0 0 4 4h6a4 4 0 0 0 4-4v-3"/></svg> Baths {baths}</span>
                        <span class="overview-spec"><svg class="overview-icon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg> Sleeps {sleeps}</span>
                    </div>
                </div>
                {overview_body_html}
            </div>
        </section>
{gallery_html}
{rates_button_html}
{amenities_section_html}
{reviews_html}

        <!-- Things To Do -->
        <section class="container">
            <div style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h2>Explore St. John</h2>
                <p style="color: var(--color-text-light); margin-bottom: 2rem;">St. John offers world-class beaches, hiking in Virgin Islands National Park, and vibrant Cruz Bay dining. {name} puts you close to it all.</p>
                <a href="../things-to-do.html" class="btn btn-primary">Things To Do Guide</a>
            </div>
        </section>

        <!-- CTA -->
        <section style="background: var(--color-primary); padding: 4rem 0; text-align: center;">
            <div class="container">
                <h2 style="color: white; margin-bottom: 1rem;">Ready to Book {name}?</h2>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.15rem; margin-bottom: 2rem;">Call us at 1-340-776-6805 or send a message.</p>
                <a href="../contact.html" class="btn" style="background: var(--color-accent); color: var(--color-primary); font-size: 1.1rem; padding: 1.1rem 2.5rem;">Contact Us</a>
            </div>
        </section>

        <!-- Related Villas -->
        <section class="container">
            <div class="section-title">
                <h2>Other Villas You Might Love</h2>
            </div>
            <div style="text-align: center;">
                {related_html}
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="../villas.html" class="btn btn-primary">View All Villas</a>
            </div>
        </section>
{rates_modal_html}
    </main>

{FOOTER_HTML}

    <script src="../js/main.js" defer></script>
</body>
</html>"""
    return html


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []
    
    for villa in villas:
        html_content = generate_html(villa, villas)
        filepath = os.path.join(OUTPUT_DIR, f"{villa['slug']}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        created.append(filepath)
    
    print(f"Created {len(created)} villa pages:")
    for f in created:
        print(f"  {f}")

if __name__ == "__main__":
    main()
