# hexacheck
Python code to check if a 3D point (x,y,z) is in an hexaheron

* point_is_in_hexa(point,centers,normals)

The idea is simple, we calculate the vectors from the point to each face center. Next, we calculate the dot product between each normal/vector couple. To be inside the hexaheron, all dot products must be <=0.
