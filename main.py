from flask import Flask, render_template, request
from Class.flight import Flight
import requests
import folium

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/gujarat')
def gujarat():
    return render_template("gujarat.html")


@app.route('/kerala')
def kerala():
    return render_template("kerala.html")


@app.route('/maharashtra')
def maharashtra():
    return render_template("maharashtra.html")


@app.route('/place')
def place():
    return render_template("place.html")


@app.route('/place1')
def place1():
    return render_template("place1.html")


@app.route('/place2')
def place2():
    return render_template("place2.html")


@app.route('/place3')
def place3():
    return render_template("place3.html")


@app.route('/spiritual')
def spiritual():
    return render_template("spiritual.html")


@app.route('/checkitout_flights')
def chk_flight():
    return render_template("checkitout_flights.html")


@app.route('/checkitout_hotel')
def chk_accommodation():
    return render_template("checkitout_hotel.html")


@app.route('/checkitout_flights', methods=['GET', 'POST'])
def flights():
    if request.method == 'POST':
        flight = Flight()
        flight.start = request.form.get('From')
        flight.destination = request.form.get('To')

        api_flight_location_endpt = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/IN/INR/en-IN/"

        headers_flight = {
            "x-rapidapi-key": "41e69a38a1msh7031b497162d6fap141d70jsna5df11e59d82",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        # --------------------------------------START DESTINATION--------------------------------------------

        response_start = requests.request("GET", api_flight_location_endpt, headers=headers_flight,
                                          params={"query": flight.start})
        data_start = response_start.json()

        start_id = flight.location_name(data_start=data_start, location=flight.start.title())

        # --------------------------------------FINAL DESTINATION--------------------------------------------
        response_location = requests.request("GET", api_flight_location_endpt, headers=headers_flight,
                                             params={"query": flight.destination})
        data_location = response_location.json()
        # print(response_location.status_code)

        destination_id = flight.location_name(data_start=data_location, location=flight.destination.title())

        # --------------------------------------FLIGHT DETAILS------------------------------------------------

        api_flight_date_endpoint = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsedates/v1.0/IN/INR/en-IN/{start_id}/{destination_id}/{flight.date}"

        response_date = requests.request("GET", api_flight_date_endpoint, headers=headers_flight)

        data_date = response_date.json()

        return render_template("flights.html", data_date=data_date, flight=flight)


coordinates, location_list = [], []


@app.route('/checkitout_hotel', methods=['GET', 'POST'])
def hotel():
    if request.method == 'POST':
        destination = request.form.get("destination")
        check_in = request.form.get("check_in")
        check_out = request.form.get("check_out")
        # -------------------------------------HOTEL LOCATION DETAILS---------------------------------------------------

        api_location_endpoint = "https://hotels4.p.rapidapi.com/locations/search"
        api_details_endpoint = "https://hotels4.p.rapidapi.com/properties/get-details"

        headers = {
            "x-rapidapi-key": "41e69a38a1msh7031b497162d6fap141d70jsna5df11e59d82",
            'x-rapidapi-host': "hotels4.p.rapidapi.com"
        }

        params_location = {"query": destination,
                           "locale": "en_US",
                           "type": "HOTEL",
                           }
        response_location = requests.get(api_location_endpoint, headers=headers, params=params_location)
        data_location = response_location.json()

        for i in data_location['suggestions']:
            if i['group'] == 'HOTEL_GROUP':
                for j in i['entities']:
                    location_list.append([j['destinationId'], j['name']])

        hotel_details_list = []
        for i in location_list:

            # ---------------------------------- DETAILS OF HOTELS IN LIST ----------------------------------

            params_hotel_info = {"id": i[0],
                                 "check_in": check_in,
                                 "check_out": check_out,
                                 "currency": "INR",
                                 "locale": "en_IN",
                                 "adults": "1"}

            response = requests.get(api_details_endpoint, headers=headers, params=params_hotel_info)
            data_details = response.json()

            # print("\n----------HOTEL_PRICE-----------\n")
            try:
                hotel_price = data_details['data']['body']['propertyDescription']['featuredPrice']['currentPrice'][
                    'plain']
                hotel_price_description_list = data_details['data']['body']['propertyDescription']['featuredPrice'][
                    'priceSummary']
                hotel_price_description = ''.join(hotel_price_description_list)
            except KeyError:
                hotel_price, hotel_price_description = " ", "Not available"

            #     print("\n----------ADDRESS-----------\n")
            address = ''.join(data_details['data']['body']['propertyDescription']['address']['fullAddress'])

            #     print("\n----------LAT & LON-----------\n")
            lat = data_details['data']['body']['pdpHeader']['hotelLocation']['coordinates']['latitude']
            lon = data_details['data']['body']['pdpHeader']['hotelLocation']['coordinates']['longitude']
            coordinates.append([lat, lon])
            #
            #     print("\n----------STAR_RATING-----------\n")
            star_rating = data_details['data']['body']['propertyDescription']['starRating']

            details = {
                "Hotel": i[-1],
                "Address": address,
                "Price": f"Rs.{hotel_price} {hotel_price_description}",
                "Rating": star_rating,
            }
            hotel_details_list.append(details)

        return render_template("hotel.html", details=hotel_details_list, destination=destination)


@app.route('/map')
def location_on_map():
    folium_map = folium.Map(location=coordinates[0], zoom_start=10)
    fg = folium.FeatureGroup()
    for i in range(len(coordinates)):
        fg.add_child(folium.Marker(location=coordinates[i], popup=location_list[i][-1],
                                   icon=folium.Icon(color='red')))
    folium_map.add_child(fg)
    return folium_map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)
