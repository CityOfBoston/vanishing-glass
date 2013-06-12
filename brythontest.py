dojo.require("esri.map")

esri.Map("map", {
  "basemap": "topo",
  "center": [-103.272, 39.096],
  "zoom": 4,
  "slider": False
})

# doc["map"].innerHTML = "Hello World"