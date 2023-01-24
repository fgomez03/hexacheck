# hexacheck
Python code to check if a 3D point (x,y,z) is in an hexaheron

* point_is_in_hexa(point,centers,normals)

The idea is simple, we compute the vectors for the point to each face center.
Then we compute the dot product between the face normal and each vector.
In order to be inside the hexaheron, all dot product must be <=0.
