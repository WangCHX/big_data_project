import de.fhpotsdam.unfolding.*;
import de.fhpotsdam.unfolding.data.*;
import de.fhpotsdam.unfolding.marker.*;
import de.fhpotsdam.unfolding.utils.*;
import de.fhpotsdam.unfolding.geo.*;
import de.fhpotsdam.unfolding.providers.*; 
import java.util.*;
import java.io.*;

UnfoldingMap map;
BufferedReader reader;
String line;

void setup(){
  size(1200, 1200);
  map = new UnfoldingMap(this);
  MapUtils.createDefaultEventDispatcher(this, map);
  Location nycLocation = new Location(40.71427, -74.00597);  
  map.zoomAndPanTo(nycLocation, 12);
  map.setZoomRange(12,12);
  float maxPanningDistance = 30; // in km
  map.setPanningRestriction(nycLocation, maxPanningDistance);
  String file = "/Users/apple/Desktop/class/14fall/big_data_project/test/temp_nyc";

  reader = createReader(file);
  int i = 0;
  try {
    while ((line = reader.readLine()) != null) {
      System.out.println(i);
      i ++;
      String[] colms = line.split("\\s+"); 
      List valid = Arrays.asList(colms);
      if (valid.contains("NULL")){
        continue;
      }
      Location tempLocation = new Location(Float.parseFloat(colms[0]), Float.parseFloat(colms[1]));
      SimplePointMarker tempMarker = new SimplePointMarker(tempLocation);
      tempMarker.setStrokeWeight(0);
      map.addMarkers(tempMarker);
    }
  }catch (IOException e) {
     e.printStackTrace();  
  }
}

void draw(){
  map.draw(); 
  Location location = map.getLocation(mouseX, mouseY);
  fill(0);
  text(location.getLat() + ", " + location.getLon(), mouseX, mouseY);
}


