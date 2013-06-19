The GIS / Mapping world is divided into desktop mappers (using Python) and web mappers (using JavaScript and other technologies, but mostly JavaScript).

Vanishing-Glass is an experiment to bridge the gap, and make interactive mapping and custom data maps accessible in 100% Python. The code is all client-side,
so projects can be hosted via GitHub Pages.

<h2>Examples</h2>

<a href="http://cityofboston.github.io/vanishing-glass/">An example map</a> which adds a marker to a map. <a href="https://github.com/cityofboston/vanishing-glass/blob/gh-pages/vanishing.py">Python source</a>

<a href="http://cityofboston.github.io/vanishing-glass/usejson.html">A more complex example</a>, loading JSON from ArcGIS Server API.

<h2>Components</h2>

<a href="http:/brython.info">Brython</a> is an open source (New BSD License) framework to write web apps and client-side code in Python.

<a href="http://arcgis.com">ArcGIS.com</a> is a web-mapping platform with JavaScript APIs and thousands of datasets.

<h2>Current Status</h2>

* Simple commands work

     // JS: map.centerAndZoom( [ -70, 40 ], 11 );
     
     # Python: map.centerAndZoom( [ -70, 40 ], 11 )

* More complex commands where JavaScript uses the 'new' keyword or anonymous functions are proving difficult:

     // JS: new esri.geometry.Point( [-70, 40], { "wkid": 4326 } );
     
     # Python: esri.geometry.Point( [-70, 40], { "wkid": 4326 } )

* The workaround for using the 'new' keyword is currently using a JavaScript function to return an initialized object to the Brython script

     // Old JS: new esri.geometry.Point( [-70, 40], { "wkid": 4326 } );
     
     becomes
     
     // New JS: ptmaker = function(lnglat, sr){ return new esri.geometry.Point( lnglat, sr ); };
     
     # Python: ptmaker( [ -70, -40 ], { "wkid": 4326 } )
