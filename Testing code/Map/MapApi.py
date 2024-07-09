# encoding: utf-8
import googlemaps

GOOGLE_MAPS_API_KEY = "AIzaSyB1rTtnge-FZLhl0As4Lq6VhiCBKZGEYM4"

def get_reviews_from_lat_long(name=None, latlon=None, radius=50):

    if name and latlon:
        print("Please provide either name or latlon, not both.")
        return "Error"

    if not name and not latlon:
        print("Please provide either name or latlon.")
        return "Error"

    API_KEY = GOOGLE_MAPS_API_KEY
    gmaps = googlemaps.Client(key=API_KEY)
    if name:
        places_result = gmaps.places_nearby(
            location=name, radius=radius, language="zh-TW", type="restaurant")
    else:
        places_result = gmaps.places_nearby(
            location=latlon, radius=radius, language="zh-TW", type="restaurant")

    # Step 2: Retrieve Place Details and Reviews
    if not places_result['results']:
        return ""

    place = places_result['results'][0]
    place_id = place['place_id']
    place_details = gmaps.place(place_id=place_id, language="zh-TW")

    reviews = ""
    if 'reviews' in place_details['result']:
        review_count = len(place_details['result']['reviews'])
        print(f"Number of reviews found: {review_count}")
        for review in place_details['result']['reviews']:
            reviews += f"""{review['text']}\n"""

    return reviews

if __name__ == "__main__":
    reviews = get_reviews_from_lat_long(latlon=(25.015746592992212, 121.53153581136522))
    print(reviews)
    # Restaurant second floor: 25.015746592992212, 121.53153581136522
    # Current location: 25.018912764487222, 121.54362550425198
