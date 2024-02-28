# Crime Influenced Walking/Biking App

A walking or biking application that weighs high crime areas lower to keep the user in safer areas.

# TODO (In somewhat order...):
1. Use openstreet maps to determine closest node to a lat and lon point. ✅
2. Django hosted page to show map live.
    -- Leaflet
    -- OpenLayers
3. Use webpage clicking interaction to choose nodes A and B, and return a route
4. Implement crime data weighting for the route.
5. Fine tune route.
6. Create better UI
7. Implement searching an address -> node -> route? --- Maybe ---
8. Expand to nearby areas, as long as data is present.
9. Research what other map applications use? Osm? Google? Hodge Podge?


# Saved Information For Future Processing:

How mapping typically finds routes:
The route finding process starts by obtaining the coordinates of points A and B. Then, it creates a virtual line connecting A and B and queries the database for road segments located within a specified distance from that line. If a path cannot be determined initially, the process is repeated with an increased distance.
