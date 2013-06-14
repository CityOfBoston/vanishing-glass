# vanishing.py
# Python that controls an ArcGIS webmap

# import some Brython libraries
# import html
# import json

# import essential JS objects
main_map = JSObject(main_map)
esri = JSObject(esri)

SpatialReference = JSObject(wgs84)
Point = JSObject(ptmaker)
PictureMarkerSymbol = JSObject(picmaker)
Graphic = JSObject(grmaker)
jsonparse = JSObject(jsonparse)

# re-center map
main_map.centerAndZoom( [ -71, 42 ], 8 )

# define what to do with JSON returned
def on_complete(req):
    
    if req.status==200 or req.status==0:
        # returned successfully
        mypts = jsonparse( req.text )
        JSObject(console).log("about to look at points")
        
        for feature in mypts["features"]:
          JSObject(console).log( "found a feature" )
          JSObject(console).log( feature )
          continue
        
          # test creating a point, adding a marker
          pt = Point( [ feature["geometry"]["x"] , feature["geometry"]["y"] ], SpatialReference )
          symbol = PictureMarkerSymbol( "marker.png", 40, 40 )
          gr = Graphic( pt, symbol )
          main_map.graphics.add(gr)
    else:
        # failed
        alert( req.text )

# make an AJAX request
req = ajax()
req.on_complete = on_complete
#req.set_timeout(timeout, err_msg)
req.open('GET', 'samplejson.json?v=2', True)
req.send()