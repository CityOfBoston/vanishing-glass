The GIS / Mapping world is divided into desktop mappers (using Python) and web mappers (using JavaScript and other technologies, but mostly JavaScript)

Vanishing-Glass is an experiment to bridge the gap, and make interactive mapping and custom data maps accessible in 100% Python. The code is all client-side,
so projects can be hosted via GitHub Pages.

<h2>Components</h2>

<a href="http:/brython.info">Brython</a> is an open source (New BSD License) framework to write web apps and client-side code in Python

<a href="http://arcgis.com">ArcGIS.com</a> is a web-mapping platform with JavaScript APIs and thousands of datasets

<h2>Current Status</h2>

* Simple commands work

     // JS: map.centerAndZoom( [ -70, 40 ], 11 );
     # Python: map.centerAndZoom( [ -70, 40 ], 11 )

* More complex commands where JavaScript uses the 'new' keyword or anonymous functions are proving difficult:

     // JS: new esri.geometry.Point( [-70, 40], { "wkid": 4326 } );
     // # Python: esri.geometry.Point( [-70, 40], { "wkid": 4326 } )
