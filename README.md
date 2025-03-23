# Color Math

Too many teams in the dodgeball league are the same color.
This project tires to solve this issue with math and the 
Lab colorspace.

# Part 1: Best colors for the spring

Part 1 explores the current colors selected for the
spring season, and which colors would be the best
to add.
# Useful Links Part 1

- Pros and Cons of Lab color: https://graphicdesign.stackexchange.com/questions/76824/what-are-the-pros-and-cons-of-using-lab-color
- iOS Dev Guidelines: https://developer.apple.com/design/human-interface-guidelines/layout
- Plotly Text and Annotations in Python: https://plotly.com/python/text-and-annotations/#font-color-size-and-familiy
- JSON in Javascript: https://www.freecodecamp.org/news/how-to-read-json-file-in-javascript/

# Useful Links Part 2
- Maximum Diversity Problem: https://grafo.etsii.urjc.es/optsicom/mdp.html
- Convex Hull Algo: https://www.geeksforgeeks.org/convex-hull-algorithm/
- SciPy Convex Hull: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
- Only Website That Notes if LAB Conversion Doesn't Exist: https://www.e-paint.co.uk/convert-lab.asp
- What is an Observer Angle: https://www.xrite.com/service-support/what_is_meant_by_the_term_observer_angle
- Understanding Standard Illuminants: https://sensing.konicaminolta.us/us/blog/understanding-standard-illuminants-in-color-measurement/

Approaches for part 2

## Finding Solutions
- Greedy Algorithm: Greedily traverse the space for the point with
the furthest minimum distance 
- Random Selection: Randomly select points 

## Scoring Solutions

- Average Euclidean Distance
  - Done
- Average CIE2000 Distance
  - Done

- Create a convex hull of all the points and see what happens 
  - Done, very easy
  - Convex hull volume is a metric we can use to show how "colorful" a set of options are
  - 
  - Remove center points to make computation feasible for selecting every combo and scoring via volume

- Volume of the Solid in Euclidean/CIE2000 Space
  - Want to come up with a perfect volume based off the CIE space and compare overlap with
  selected points (this is very difficult currently)
  - Can use the volume created by the current set of points, and determine the subset 
  with the most overlap
  - Consider the current convex hull of the space the "high resolution space" and then
  downscale to 16 or 24 or n points

- Surface Area?
- What sphere at 0,0 has a surface that intersects the most points?

- K-Means Clustering / Voronoi Cells
- If I have a point cloud and want to preserve the convex hull, how
do I downscale most effectively? - How to score similarities between
volumes?

# Heading

**Bold**

some text

more text here, text go brr