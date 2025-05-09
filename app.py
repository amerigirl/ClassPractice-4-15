#to create a development environment
#python3 -m venv venv 

#to activate env
#source venv/bin/activate

#to deactivete env
#deactivate

#pip install -r requirements.txt    
from flask import Flask, jsonify, request, abort 

airbnb_listings = [
    {
        "id": "1001",
        "name": "Cozy Downtown Loft",
        "location": "New York, NY",
        "price": 150,
        "description": "Modern loft in the heart of downtown Manhattan. Walk to major attractions.",
        "guests": 2,
        "beds": 1,
        "amenities": ["WiFi", "Air conditioning", "Kitchen", "Washer"],
        "rating": 4.85,
        "reviews": 120,
        "image": "https://example.com/images/loft1.jpg",
        "url": "https://www.airbnb.com/rooms/1001"
    },
    {
        "id": "1002",
        "name": "Beachfront Bungalow",
        "location": "Santa Monica, CA",
        "price": 220,
        "description": "Relax in this charming bungalow steps from the beach. Perfect for couples.",
        "guests": 3,
        "beds": 2,
        "amenities": ["WiFi", "Beach access", "Free parking", "Patio"],
        "rating": 4.92,
        "reviews": 87,
        "image": "https://example.com/images/beach2.jpg",
        "url": "https://www.airbnb.com/rooms/1002"
    },
    {
        "id": "1003",
        "name": "Mountain Cabin Retreat",
        "location": "Aspen, CO",
        "price": 300,
        "description": "Secluded cabin with mountain views, fireplace, and hot tub.",
        "guests": 6,
        "beds": 3,
        "amenities": ["Hot tub", "Fireplace", "Kitchen", "Mountain view"],
        "rating": 4.78,
        "reviews": 54,
        "image": "https://example.com/images/cabin3.jpg",
        "url": "https://www.airbnb.com/rooms/1003"
    },
    {
        "id": "1004",
        "name": "Historic City Apartment",
        "location": "Boston, MA",
        "price": 180,
        "description": "Stay in a renovated historic apartment close to museums and parks.",
        "guests": 4,
        "beds": 2,
        "amenities": ["WiFi", "Washer", "Dishwasher", "Elevator"],
        "rating": 4.67,
        "reviews": 65,
        "image": "https://example.com/images/apartment4.jpg",
        "url": "https://www.airbnb.com/rooms/1004"
    },
    {
        "id": "1005",
        "name": "Lake House Escape",
        "location": "Lake Tahoe, NV",
        "price": 350,
        "description": "Spacious lake house with private dock and canoe. Family-friendly.",
        "guests": 8,
        "beds": 4,
        "amenities": ["Lake view", "Canoe", "Fire pit", "BBQ grill"],
        "rating": 4.95,
        "reviews": 33,
        "image": "https://example.com/images/lakehouse5.jpg",
        "url": "https://www.airbnb.com/rooms/1005"
    },
    {
        "id": "1006",
        "name": "Urban Studio with Balcony",
        "location": "Chicago, IL",
        "price": 130,
        "description": "Bright studio with balcony overlooking the city skyline.",
    }
    ]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to the Airbnb Listings API!"

@app.route("/rentals", methods=["GET"])
def rentals():

    #for r in airbnb_listings: return r if r[id] is == id
    rental = [r for r in airbnb_listings if r["id"] ==id]
    return jsonify(airbnb_listings)
