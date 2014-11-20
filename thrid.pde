import de.fhpotsdam.unfolding.*;
import de.fhpotsdam.unfolding.data.*;
import de.fhpotsdam.unfolding.marker.*;
import de.fhpotsdam.unfolding.utils.*;
import de.fhpotsdam.unfolding.geo.*;
import de.fhpotsdam.unfolding.providers.*; 
import de.fhpotsdam.unfolding.mapdisplay.MapDisplayFactory;
import java.util.*;
import java.io.*;

UnfoldingMap map;
BufferedReader reader;
String line;
AbstractMapProvider provider;
Location prev, now;

void setup(){
  size(1200, 1200);
  provider = new Microsoft.AerialProvider();
  map = new UnfoldingMap(this, provider);
  MapUtils.createDefaultEventDispatcher(this, map);
  Location nycLocation = new Location(40.71427, -74.00597);  
  map.zoomAndPanTo(nycLocation, 12);
  map.setZoomRange(12,12);
  float maxPanningDistance = 30; // in km
  map.setPanningRestriction(nycLocation, maxPanningDistance);
  String file = "/Users/apple/Desktop/class/14fall/big_data_project/test/nyc.tsv";

  reader = createReader(file);
  try {
    line = reader.readLine();
  } catch (IOException e) {
    e.printStackTrace();
    line = null;
  }
  String[] colms = line.split("\\s+"); 
  List valid = Arrays.asList(colms);
  prev = new Location(Float.parseFloat(colms[0]), Float.parseFloat(colms[1]));
  SimplePointMarker tempMarker = new SimplePointMarker(prev);
  tempMarker.setStrokeWeight(2);
  tempMarker.setColor(color(186,255,74));
  map.addMarkers(tempMarker);
  
}

void draw(){
  map.draw(); 
//  int i = 0;
  try{
    line = reader.readLine();
  } catch (IOException e) {
     e.printStackTrace();
     line = null;
  }
  if (line == null) {
     noLoop(); 
  }
  else{
    String[] colms = line.split("\\s+"); 
    List valid = Arrays.asList(colms);
    now = new Location(Float.parseFloat(colms[0]), Float.parseFloat(colms[1]));
    SimplePointMarker tempMarker = new SimplePointMarker(now);
    SimpleLinesMarker connectionMarker = new SimpleLinesMarker(prev, now);
    tempMarker.setStrokeWeight(1);
    tempMarker.setColor(color(186,255,74));
    connectionMarker.setColor(color(186,255,74));
    map.addMarkers(tempMarker, connectionMarker);
    prev = now;
    Location location = map.getLocation(mouseX, mouseY);
    fill(204,102,0);
    text(location.getLat() + ", " + location.getLon(), mouseX, mouseY);
  }
}


