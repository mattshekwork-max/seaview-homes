#!/usr/bin/env python3
"""Generate 16 individual SEO-optimized villa pages for seaviewhomes.com"""

import os
import json

OUTPUT_DIR = "/Users/macai/.openclaw/workspace/seaview-homes-site/villas"
SITE_URL = "https://seaviewhomes.com"
IMG_BASE = "assets/img/villas"

villas = [
    {
        "slug": "villa-splendore",
        "name": "Villa Splendore",
        "image": "villa-splendore.jpg",
        "rooms": 3, "baths": "2.5", "sleeps": 6,
        "type": "Hillside Romantic Retreat",
        "short_desc": "Romantic 1-bedroom hillside villa with plunge pool and panoramic ocean views in St. John, USVI.",
        "description": "Nestled on a lush hillside overlooking the sparkling Caribbean Sea, Villa Splendore offers the perfect romantic escape in St. John, USVI. This intimate 1-bedroom villa combines modern luxury with breathtaking natural beauty. Wake up to panoramic views of the ocean and surrounding hills, then spend your days relaxing by your private plunge pool or exploring the pristine beaches of St. John just minutes away. The open-air design lets the tropical breeze flow through the living spaces, creating an unforgettable island experience. Villa Splendore is ideally situated near Cruz Bay, giving you easy access to dining, shopping, and the ferry to St. Thomas while maintaining total privacy and tranquility. Trunk Bay, voted one of the most beautiful beaches in the world, is just a short drive away.",
        "amenities": ["Private plunge pool", "Full kitchen", "Air conditioning", "WiFi", "Ocean view", "Parking", "Outdoor shower", "King bed"]
    },
    {
        "slug": "surfside",
        "name": "Surfside",
        "image": "surfside.jpg",
        "rooms": 3, "baths": 3, "sleeps": 6,
        "type": "Oceanfront Family Villa",
        "short_desc": "3-bedroom oceanfront villa perfect for families, with pool and easy beach access in St. John, USVI.",
        "description": "Surfside is a welcoming 3-bedroom oceanfront villa designed with families in mind. Located on St. John's beautiful north shore, this villa offers easy access to some of the Caribbean's most celebrated beaches including Trunk Bay, Cinnamon Bay, and Maho Bay. The spacious living area opens to a large pool deck with panoramic ocean views, making it easy to keep an eye on the kids while relaxing in comfort. Each bedroom is air-conditioned with its own bathroom, ensuring privacy for everyone. The fully equipped kitchen makes meal prep a breeze, and the outdoor grill is perfect for evening barbecues. Surfside combines the comforts of home with the beauty of a St. John oceanfront location.",
        "amenities": ["Private pool", "Oceanfront location", "Full kitchen", "Air conditioning", "WiFi", "3 bedrooms", "Parking", "Outdoor grill", "Beach gear", "Washer/dryer"]
    },
    {
        "slug": "seaside-breeze",
        "name": "Seaside Breeze",
        "image": "seaside-breeze.jpg",
        "rooms": 4, "baths": 3, "sleeps": 8,
        "type": "Hillside Panoramic Villa",
        "short_desc": "2-bedroom hillside villa with panoramic ocean views and cooling trade winds in St. John, USVI.",
        "description": "Seaside Breeze is a charming 2-bedroom hillside villa that lives up to its name with constant cooling trade winds and panoramic views of the Caribbean Sea. Perched above Cruz Bay, this villa offers the perfect balance of convenience and tranquility. You're just minutes from town yet worlds away in your private hillside retreat. The villa features an open-air great room that flows seamlessly to the pool deck, where you can watch sailboats navigate the channel between St. John and St. Thomas. Both bedrooms offer comfortable accommodations with ocean views. Seaside Breeze is ideal for small families or two couples traveling together who want to experience the best of St. John without breaking the budget.",
        "amenities": ["Private pool", "Panoramic ocean views", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Outdoor deck", "Grill"]
    },
    {
        "slug": "cinnamon-ridge",
        "name": "Cinnamon Ridge",
        "image": "cinnamon-ridge.jpg",
        "rooms": 5, "baths": "5.5", "sleeps": 10,
        "type": "Near-Beach Bright Villa",
        "short_desc": "Bright and airy 2-bedroom villa just steps from Cinnamon Bay Beach in St. John, USVI.",
        "description": "Cinnamon Ridge is a bright and airy 2-bedroom villa located just moments from one of St. John's most beloved beaches, Cinnamon Bay. This inviting villa is perfect for beach lovers who want to be close to the action while enjoying the privacy of their own space. The interior is filled with natural light and decorated in a casual Caribbean style. The covered porch offers a relaxing spot for morning coffee or evening sunsets. Cinnamon Bay Beach, with its soft white sand and excellent snorkeling, is just a short walk or drive away. The nearby Cinnamon Bay Campground offers kayak rentals and a small cafe. For those wanting to explore further, the Virgin Islands National Park visitor center is close by.",
        "amenities": ["Near beach", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Covered porch", "Grill", "Beach towels provided"]
    },
    {
        "slug": "rainbow-beach-house",
        "name": "Rainbow Beach House",
        "image": "rainbow-beach-house.jpg",
        "rooms": 4, "baths": 4, "sleeps": 8,
        "type": "Beachfront Colorful Villa",
        "short_desc": "Vibrant 2-bedroom beachfront villa with direct sand access and colorful Caribbean decor in St. John.",
        "description": "Rainbow Beach House is a vibrant and joyful 2-bedroom beachfront villa that captures the colorful spirit of the Caribbean. With direct access to a quiet stretch of sand, this villa is a beach lover's dream. The interior is decorated with bright island colors and local artwork, creating a fun and relaxed atmosphere. The open kitchen and living area flow right out to the beach deck, where you can spend your days swimming, sunbathing, or watching the spectacular St. John sunsets. Both bedrooms are air-conditioned and comfortably appointed. Rainbow Beach House is perfect for a small family or couples who want a true toes-in-the-sand St. John experience without the luxury price tag.",
        "amenities": ["Beachfront access", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Beach deck", "Grill", "Kayak storage"]
    },
    {
        "slug": "solemare",
        "name": "Solemare",
        "image": "solemare.jpg",
        "rooms": 3, "baths": "3.5", "sleeps": 8,
        "type": "Elegant Oceanview Villa",
        "short_desc": "Elegant 3-bedroom oceanview villa with pool and sophisticated design in St. John, USVI.",
        "description": "Solemare is an elegant 3-bedroom villa perched on a hillside with sweeping ocean views on St. John's south shore. The name means 'sun and sea' in Italian, and this villa delivers on that promise. The sophisticated design features clean lines, natural materials, and expansive glass walls that blur the boundary between inside and out. The infinity-edge pool seems to drop into the ocean below. Each of the three bedrooms is a private retreat with en-suite bathroom and ocean views. Solemare is perfect for a group of friends or a multi-generational family seeking a refined St. John experience. The south shore location offers a quieter alternative to the north shore while still being close to Cruz Bay and Coral Bay's dining and shopping.",
        "amenities": ["Infinity pool", "Ocean views", "Gourmet kitchen", "Air conditioning", "WiFi", "3 en-suite bedrooms", "Parking", "Outdoor lounge", "Wine fridge"]
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
        "type": "Spacious Hillside Villa",
        "short_desc": "Spacious 4-bedroom hillside villa with pool and panoramic views of St. John and surrounding islands.",
        "description": "Island Rider is a spacious 4-bedroom hillside villa that commands panoramic views of St. John, St. Thomas, and the British Virgin Islands. This expansive property is perfect for larger families or groups of friends traveling together. The open-air great room is the heart of the villa, with comfortable seating, a dining area, and a well-equipped kitchen. Outside, the large pool deck offers plenty of space for sunbathing, and the covered pavilion is perfect for al fresco dining. Each of the four bedrooms is air-conditioned with its own bathroom. Island Rider is conveniently located between Cruz Bay and Coral Bay, giving you easy access to both sides of the island. The nearby Centerline Road offers quick trips to both north and south shore beaches.",
        "amenities": ["Large pool", "Panoramic views", "Full kitchen", "Air conditioning", "WiFi", "4 bedrooms", "Parking", "Outdoor pavilion", "Grill", "Washer/dryer"]
    },
    {
        "slug": "mango-bay",
        "name": "Mango Bay",
        "image": "mango-bay.jpg",
        "rooms": 4, "baths": "4.5", "sleeps": 8,
        "type": "Tropical Garden Serene Villa",
        "short_desc": "Serene 2-bedroom villa surrounded by lush tropical gardens near St. John's best beaches.",
        "description": "Mango Bay is a serene 2-bedroom villa surrounded by lush tropical gardens filled with mango trees, banana plants, and vibrant island flowers. This peaceful retreat is perfect for travelers seeking a quiet, nature-immersed St. John experience. The villa's covered deck looks out over the gardens to the sea beyond, and the sound of tree frogs at night creates a magical Caribbean ambiance. Despite its secluded feel, Mango Bay is just minutes from some of St. John's most famous beaches including Trunk Bay and Hawksnest Bay. The interior is comfortable and casual, with everything you need for a relaxing stay. Mango Bay is ideal for nature lovers and those who want to experience the lush, green side of St. John.",
        "amenities": ["Tropical gardens", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Covered deck", "Outdoor shower", "Fruit trees", "Hammock"]
    },
    {
        "slug": "vista-caribe",
        "name": "Vista Caribe",
        "image": "vista-caribe.jpg",
        "rooms": 4, "baths": 4, "sleeps": 8,
        "type": "Cliffside Panoramic Estate",
        "short_desc": "Grand 5-bedroom cliffside estate with jaw-dropping panoramic views of the Caribbean Sea in St. John.",
        "description": "Vista Caribe is a grand 5-bedroom cliffside estate that offers some of the most spectacular views in all of St. John. Perched on a dramatic cliff overlooking the Caribbean Sea, this luxury villa provides 180-degree panoramas from the British Virgin Islands to the south shore of St. John. The expansive property features a large infinity pool, multiple outdoor living areas, and a dramatic great room with walls of glass. Each of the five bedrooms is generously sized with en-suite bathrooms and private views. Vista Caribe is perfect for extended family gatherings, corporate retreats, or special celebrations. The villa is staffed with a property manager who can arrange concierge services, private chef, and island tours. Experience St. John at its most magnificent.",
        "amenities": ["Infinity pool", "180-degree views", "Gourmet kitchen", "Air conditioning", "WiFi", "5 en-suite bedrooms", "Parking", "Multiple decks", "Concierge service", "Outdoor kitchen", "Washer/dryer"]
    },
    {
        "slug": "reef-break-vista",
        "name": "Reef Break Vista",
        "image": "reef-break-vista.jpg",
        "rooms": 4, "baths": 3, "sleeps": 10,
        "type": "Oceanview Surf Villa",
        "short_desc": "2-bedroom oceanview villa near St. John's best surf spots with stunning reef and wave views.",
        "description": "Reef Break Vista is a 2-bedroom oceanview villa that takes its name from the visible reef break just offshore. Located on St. John's east end, this villa is a favorite among surfers, snorkelers, and ocean enthusiasts. The deck offers a front-row view of the reef where you can watch waves break and sea turtles surface. The villa is casual and comfortable, designed for active travelers who spend their days in the water. Both bedrooms are air-conditioned with ocean views. The east end location puts you near some of St. John's best snorkeling spots including Saltpond Bay and Drunk Bay. Coral Bay, with its laid-back restaurants and bars, is just a few minutes away.",
        "amenities": ["Ocean views", "Full kitchen", "Air conditioning", "WiFi", "2 bedrooms", "Parking", "Deck with reef views", "Outdoor shower", "Snorkel gear", "Board storage"]
    },
    {
        "slug": "sea-forever",
        "name": "Sea Forever",
        "image": "sea-forever.jpg",
        "rooms": 5, "baths": "5.5", "sleeps": 10,
        "type": "Luxury Grand Estate",
        "short_desc": "Magnificent 6-bedroom luxury estate with pool, tennis court, and panoramic ocean views in St. John.",
        "description": "Sea Forever is the crown jewel of Seaview Homes' portfolio, a magnificent 6-bedroom luxury estate that sets the standard for St. John villas. This grand property features a stunning infinity pool, a private tennis court, and panoramic ocean views that stretch to the horizon. The great room is designed for entertaining, with a chef's kitchen, formal dining area, and comfortable lounging spaces. Each of the six bedrooms is a private suite with luxury bedding, en-suite bathroom, and individual climate control. The outdoor spaces are equally impressive, with multiple covered pavilions, an outdoor kitchen, and landscaped grounds. Sea Forever is perfect for large family reunions, destination weddings, or corporate retreats. The villa includes a full-time property manager and concierge service to ensure every detail of your stay is perfect.",
        "amenities": ["Infinity pool", "Tennis court", "Chef's kitchen", "Air conditioning", "WiFi", "6 en-suite bedrooms", "Parking", "Outdoor kitchen", "Concierge service", "Washer/dryer", "Beach gear", "Multiple decks"]
    },
    {
        "slug": "rhapsody",
        "name": "Rhapsody",
        "image": "rhapsody.jpg",
        "rooms": 5, "baths": "5.5", "sleeps": 10,
        "type": "Artistic Luxury Villa",
        "short_desc": "Artistic 4-bedroom luxury villa with unique design elements and stunning ocean views in St. John.",
        "description": "Rhapsody is an artistic 4-bedroom luxury villa that stands apart from the typical St. John rental. Every corner of this villa showcases unique design elements, from custom-built furniture to locally commissioned artwork. The great room features soaring ceilings and a wall of glass that frames the ocean view like a living painting. The pool deck is an extension of the artistic vision, with sculptural elements and a negative-edge pool. Each bedroom is individually designed with its own color palette and character. Rhapsody is perfect for design-conscious travelers who appreciate architecture and art as much as natural beauty. Located on St. John's prestigious south shore, the villa offers privacy and stunning views while being just 15 minutes from Cruz Bay.",
        "amenities": ["Infinity pool", "Ocean views", "Designer kitchen", "Air conditioning", "WiFi", "4 en-suite bedrooms", "Parking", "Art collection", "Outdoor lounge", "Wine cellar", "Washer/dryer"]
    },
    {
        "slug": "waterfall",
        "name": "Waterfall",
        "image": "waterfall.jpg",
        "rooms": 3, "baths": "3.5", "sleeps": 6,
        "type": "Hillside Pool Villa",
        "short_desc": "Luxurious 3-bedroom hillside villa with infinity pool and cascading water features in St. John, USVI.",
        "description": "Waterfall is a luxurious 3-bedroom hillside villa named for its stunning cascading water features that flow from the pool into the tropical landscape below. This villa is a serene sanctuary that combines luxury amenities with the natural beauty of St. John. The infinity pool appears to spill into the ocean, creating a seamless visual connection between the villa and the sea. The open-air living area is elegantly furnished and flows to the pool deck. Each of the three bedrooms offers privacy, comfort, and garden or ocean views. Waterfall is located in one of St. John's most desirable neighborhoods, offering both privacy and convenience. The villa is close to hiking trails in the Virgin Islands National Park and some of the island's best beaches.",
        "amenities": ["Infinity pool", "Water features", "Full kitchen", "Air conditioning", "WiFi", "3 en-suite bedrooms", "Parking", "Tropical landscaping", "Outdoor dining", "Grill", "Washer/dryer"]
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
    amenities = villa["amenities"]
    
    title = f"{name} | {rooms} BR {vtype} in St. John USVI | Seaview Homes"
    canonical = f"{SITE_URL}/villas/{slug}"
    image_url = f"{SITE_URL}/{IMG_BASE}/{image}"
    
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

    <main>
        <!-- Hero -->
        <section class="hero" style="height: 60vh; min-height: 350px; background: linear-gradient(rgba(0,30,60,0.2), rgba(0,50,100,0.3)), url('../{IMG_BASE}/{image}') center/cover no-repeat;">
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
                <p style="font-size: 1.1rem; line-height: 1.8; color: var(--color-text);">{desc}</p>
            </div>
        </section>

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
        </section>

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
