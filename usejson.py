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
main_map.centerAndZoom( [ -71.08017, 42.355626 ], 11 )

# define what to do with JSON returned
def on_complete(req):
    
    if req.status==200 or req.status==0:
        # returned successfully
        mypts = JSObject( jsonparse( req.text ) )        
        
        for feature in mypts.features:

          feature = JSObject(feature)

          # can decide how to map these points using Python code
          # for example:
          # if feature.attributes.HANDICAP == "Yes":
          #   markerpng = "accessible.png"
          # else:
          #   markerpng = "unaccessible.png"
          #
          
          if feature.attributes.Voter_Entrance is None:
            JSObject(console).log(  feature.attributes.NAME + " missing Voter_Entrance details" )

          # test creating a point, adding a marker          
          pt = Point( [ feature.geometry.x.value , feature.geometry.y.value ], SpatialReference )
          symbol = PictureMarkerSymbol( "marker.png", 22, 22 )
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