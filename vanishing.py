# vanishing.py
# Python that controls an ArcGIS webmap

# import essential JS objects
main_map = JSObject(main_map)
esri = JSObject(esri)

SpatialReference = JSObject(wgs84)
Point = JSObject(ptmaker)
PictureMarkerSymbol = JSObject(picmaker)
Graphic = JSObject(grmaker)

# re-center map
main_map.centerAndZoom( [ -71, 42 ], 8 )

# test creating a point, adding a marker

pt = Point( [-71, 42], SpatialReference )

symbol = PictureMarkerSymbol( "marker.png", 40, 40 )

gr = Graphic( pt, symbol )

main_map.graphics.add(gr)

# test output to console
JSObject(console).log(main_map)