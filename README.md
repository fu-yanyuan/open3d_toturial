# open3d_toturial
my open3d tutorial

### point cloud 
read, draw, customized draw, bounding volume

### mesh  
#### read and draw  
```python
    mesh2 = o3d.io.read_triangle_mesh("data/bun_zipper.ply")
    # mesh2.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh2],width=800,height=600)
```  
[result]()  
```python
    mesh2 = o3d.io.read_triangle_mesh("data/bun_zipper.ply")
    mesh2.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh2],width=800,height=600)
```  
[result]()  

