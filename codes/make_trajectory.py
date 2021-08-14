import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os

# load data
pcd = o3d.io.read_triangle_mesh("data/bun_zipper.ply")
pcd.compute_vertex_normals()
print(pcd) # print the number of points.

# 
def custom_draw_geometry_with_rotation(pcd):

    def rotate_view(vis):
        ctr = vis.get_view_control()
        ctr.rotate(5.0,0.0)
        return False

    vis = o3d.visualization.Visualizer()
    vis.create_window(width=512,height=512)
    vis.add_geometry(pcd)
    ctr = vis.get_view_control()
    ctr.set_zoom(zoom=0.8)
    vis.register_animation_callback(rotate_view)
    vis.run()
    vis.destroy_window()

    # o3d.visualization.draw_geometries_with_animation_callback([pcd],
    #                                                           rotate_view,
    #                                                           width=1024, height=1024)


if __name__ == "__main__":

    # help(o3d.visualization.draw_geometries_with_animation_callback)
    custom_draw_geometry_with_rotation(pcd)