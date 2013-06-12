# vanishing.py
# Python that controls an ArcGIS webmap

# import essential JS objects
main_map = JSObject(main_map)
esri = JSObject(esri)

# re-center map
main_map.centerAndZoom( [ -71, 42 ], 8 )

# test creating a point, adding a marker

sr = esri.SpatialReference( { "wkid": 4326 } )

pt = esri.geometry.Point( [-71, 42], sr )

symbol = esri.symbol.PictureMarkerSymbol( "marker.png", 40, 40 )

gr = esri.Graphic( pt, symbol )

main_map.graphics.add( gr )

# test output to console
JSObject(console).log(main_map)