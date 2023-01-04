import geojson
import uuid

def generate_geojson(cells):
    """
    Convert  the contours and a prediction value for each cell in
    a GeoJSON file (for QuPath).

    cells: list of annotated cells on the image (each cell is
            a dict with a contour and a pred)
    """
    data = []
    for cell in cells:
        dict = {}
        coords = cell["contour"]
        # to make sure the shape is closed
        coords.append(coords[0])
        dict["type"] = "Feature"
        dict["id"] = "PathCellObject" # QuPath >= 4: can be a unique id (str(uuid.uuid1()))
        dict["geometry"] = {"type": "Polygon", "coordinates": [coords]}
        dict["properties"] = {"objectType": "cell", "isLocked": False,
                              "measurements": [{"name": "Prediction",
                                                "value": cell["pred"]}]}
        data.append(dict)
    return data


# +
point1={"contour":[[886, 8], [883, 42], [884, 43], [891, 8], [886, 8]],"pred":'4.61'}
point2={"contour": [[303, 20], [294, 30], [294, 36], [295, 37], [296, 40], [303, 20]],"pred":'1.25'}


with open(f"example_2cells.geojson", 'w') as outfile:
        geojson.dump(generate_geojson([point1,point2]), outfile)


# -


