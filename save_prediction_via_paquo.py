import paquo
import os
os.environ["PAQUO_QUPATH_DIR"] = r"C:\Users\ajanowc\AppData\Local\QuPath-0.4.0"

from paquo.projects import QuPathProject
from paquo.images import QuPathImageType

from shapely.geometry import Polygon

def add_annotations(cells, qpimage):
    """
    Save the contours and a prediction value for each cell
    directly in the QuPath project.

    cells: list of annotated cells on the image (each cell is
            a dict with a contour and a pred)
    """
    
    for cell in cells:
        polygon = Polygon(cell["contour"])
        measurement = {"Prediction": cell["pred"]}
        qpimage.hierarchy.add_detection(roi=polygon, measurements=measurement)


point1={"contour":[[886, 8], [883, 42], [884, 43], [891, 8], [886, 8]],"pred":4.61}
point2={"contour": [[303, 20], [294, 30], [294, 36], [295, 37], [296, 40], [303, 20]],"pred":1.25}

with QuPathProject('./example_project', mode='w') as qpout:
    image_fname = 'example.tif'
    entry = qpout.add_image(image_fname, image_type=QuPathImageType.BRIGHTFIELD_H_E)
    add_annotations([point1,point2],entry)


