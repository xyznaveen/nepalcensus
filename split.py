import json

f = open('./nepal-districts-new.geojson')
geojson = json.load(f)

for feature in geojson["features"]:
    properties = feature["properties"]
    district = properties["DIST_EN"].lower()

    gj = {
        "type": geojson["type"],
        "name": geojson["name"],
        "crs": {
            "type": geojson["crs"]["type"],
            "properties": {
                "name": geojson["crs"]["properties"]["name"]
            },
        },
        "features": [
            feature
        ]
    }

    with open(f"./districts/{district}.geojson", 'w') as f:
        json.dump(gj, sort_keys=True, fp = f)
        print(f"wrote -> {district}")
