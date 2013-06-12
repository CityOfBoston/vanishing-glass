# vanishing.py
# Python that controls an ArcGIS webmap

# import essential JS objects
map = JSObject(main_map)
console = JSObject(console)
esri = JSObject(esri)
Point = JSObject(pointmaker)
PictureMarkerSymbol = JSObject(picturemaker)
Graphic = JSObject(graphicmaker)
SpatialReference = JSObject(srmaker)

# re-center map
map.centerAndZoom( [ -71, 42 ], 8 )

# test creating a point, adding a marker

sr = SpatialReference( { "wkid": 4326 } )
console.log(sr)

pt = Point( [-71, 42], sr )

symbol = PictureMarkerSymbol( "marker.png", 40, 40 )

gr = Graphic( pt, symbol )

map.graphics.add( gr )

# test output to console
console.log( map )