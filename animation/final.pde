import de.fhpotsdam.unfolding.*;
import de.fhpotsdam.unfolding.data.*;
import de.fhpotsdam.unfolding.marker.*;
import de.fhpotsdam.unfolding.utils.*;
import de.fhpotsdam.unfolding.geo.*;
import de.fhpotsdam.unfolding.providers.*; 
import de.fhpotsdam.unfolding.mapdisplay.MapDisplayFactory;
import processing.core.*;
import java.util.*;
import java.io.*;


public class LabeledMarker extends AbstractMarker {

        public String name;
        protected Location location;
        protected float size;

        public int color1 = 0;
        public int highlightColor = -256;

        protected boolean selected = false;
        protected boolean visible = true;

//        private PFont font;

        public LabeledMarker(Location location, float size) {
                this.location = location;
                this.size = size;
        }

        public LabeledMarker( String name, Location location, float size) {
                this(location, size);
                this.name = name;
//                this.font = font;
        }

        @Override
        public Location getLocation() {
                return location;
        }

        public void draw(PGraphics pg, float x, float y) {
                if (!isVisible()) {
                        return;
                }

                pg.fill(color1, 200);
                pg.stroke(color1, 10);
                pg.strokeWeight(1);
                pg.ellipse(x, y, size, size);
                pg.strokeWeight(2);
                pg.stroke(color1, 100);
                pg.point(x, y);
        }

        /**
         * Displays this marker's name in a box.
         */
        public void drawOuter(PGraphics pg, float x, float y) {
                if (selected && name != null) {
//                        pg.textFont(font);
                        pg.fill(color1, 200);
                        pg.noStroke();
                        pg.rect(x + 1, y - 15, pg.textWidth(name) + 2, 12);
                        pg.fill(highlightColor, 200);
                        pg.text(name, x + 2, y - 5);
                }
        }

        /**
         * Checks whether the given position is in close proximity to this Marker. Used e.g. for
         * indicating whether this Marker is selected.
         */
        protected boolean isInside(float checkX, float checkY, float x, float y) {
                // FIXME Marker's size is not scaled according to map transformation.
                return PApplet.dist(checkX, checkY, x, y) < size / 2;
        }

        /**
         * Indicates whether this marker is visible, and shall be drawn.
         * 
         * @return true if visible, false otherwise.
         */
        public boolean isVisible() {
                return visible;
        }
        
        public void setVisible(boolean visible) {
                this.visible = visible;
        }

        public boolean isSelected() {
                return selected;
        }

        public void setSelected(boolean selected) {
                this.selected = selected;
        }

}

UnfoldingMap map;
BufferedReader reader;
String line;
Location now;
AbstractMapProvider provider;
String file = "/Users/apple/Desktop/class/14fall/big_data_project/test/d3_graph/check_in_hour.tsv";
int time ;
int count;
class Point {
    public double x;
    public double y;
    public Point(double x, double y) {
      this.x = x;
      this.y = y;
  }
}
ArrayList<ArrayList<SimplePointMarker>> pointsOfTime;
//ArrayList<ArrayList<LabeledMarker>> pointsOfTime;
MarkerManager<Marker> markerManager;
//MarkerManager markerManager;

void setup(){
  size(900, 800);
  provider = new Microsoft.AerialProvider();
  map = new UnfoldingMap(this, provider);
  markerManager = map.getDefaultMarkerManager();
  MapUtils.createDefaultEventDispatcher(this, map);
  Location nycLocation = new Location(40.71427, -74.00597);  
  map.zoomAndPanTo(nycLocation, 12);
  map.setZoomRange(12,12);
  float maxPanningDistance = 30; // in km
  map.setPanningRestriction(nycLocation, maxPanningDistance);
  reader = createReader(file);
  time = -1;
  count = 1;
  pointsOfTime = new ArrayList<ArrayList<SimplePointMarker>>();
//  pointsOfTime = new ArrayList<ArrayList<LabeledMarker>>();
//  markerManager = new MarkerManager(map, pointsOfTime);
}

void removePrevTwo(){
  for (SimplePointMarker item : pointsOfTime.get(time - 1))
    markerManager.removeMarker(item);
  for (SimplePointMarker item : pointsOfTime.get(time - 2))
    markerManager.removeMarker(item);
}

//void mouseMoved() {
//        
//        // Deselect all marker
//        for (LabeledMarker lm :  markerManager.getMarkers()) {
//                lm.setSelected(false);
//        }
//        
//        // Select hit marker
//        LabeledMarker marker = (LabeledMarker) markerManager.getFirstHitMarker(mouseX, mouseY);
//        if (marker != null) {
//                marker.setSelected(true);
//        }
//
//}

void draw(){
  map.draw();
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
    String[] colms = line.split("\t"); 
    int currTime = Integer.parseInt(colms[2]);
    double lat = Float.parseFloat(colms[0]);
    double lng = Float.parseFloat(colms[1]);
    String tex = colms[3]; 
    if (currTime != time){
      ArrayList<SimplePointMarker> temp = new ArrayList<SimplePointMarker>();
      pointsOfTime.add(temp);
      time = currTime;
      println(count);
      count = 1;
      println(time);
      if (currTime - 2 >= 0){
        removePrevTwo();
      }
    }
    count += 1;
    textSize(50);
    fill(0, 102, 153, 204);
    text(String.valueOf(time) + ":00  " + String.valueOf(count), 100, 100); 
//    Point tempPoint = new Point(lat, lng);
    now = new Location(lat, lng);
//    LabeledMarker tempMarker = new LabeledMarker(text, now,10);
    SimplePointMarker tempMarker = new SimplePointMarker(now);
    tempMarker.setStrokeWeight(0);
    tempMarker.setColor(color((186 *  time + time * 10)%255,(255* time + time * 10) % 255,(74 * time + time * 10) % 255));
    
    ScreenPosition pos = tempMarker.getScreenPosition(map);
    textSize(5);
    fill(0);
    text(tex, pos.x - textWidth(tex) / 2, pos.y + 4);
    pointsOfTime.get(time).add(tempMarker);
//    map.addMarkers(tempMarker);
    markerManager.addMarker(tempMarker);
    Location location = map.getLocation(mouseX, mouseY);
    fill(204,102,0);
    textSize(10);
    text(location.getLat() + ", " + location.getLon(), mouseX, mouseY);
  }
}

