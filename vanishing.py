# vanishing.py
# Python that controls an ArcGIS webmap

# import essential JS objects
map = JSObject(main_map);
console = JSObject(console);
esri = JSObject(esri);

# re-center map
map.centerAndZoom( [ -71, 42 ], 8 )

# test creating a point, adding a marker

pt = esri.geometry.Point( [-71, 42], esri.SpatialReference({ "wkid": 4326 } ) )

symbol = esri.symbol.PictureMarkerSymbol( "marker.png", 40, 40 )

graphic = esri.Graphic( pt, symbol )

map.graphics.add(graphic)

# test output to console
console.log( map )