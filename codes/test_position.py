# Customized visualiazation: http://www.open3d.org/docs/release/tutorial/visualization/customized_visualization.html#mimic-draw-geometries-with-visualizer-class
# refer to https://github.com/intel-isl/Open3D/issues/1483

import open3d as o3d
import numpy as np


def custom_draw_geometry(pcd):
    # The following code achieves the same effect as:
    # o3d.visualization.draw_geometries([pcd])
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=800,height=600)
    vis.add_geometry(pcd)

    # to set the initial viewing position of a scene
    # press 'p' to capture the window(.png) and the relavent camera parameters(.json)
    # ScreenCamera_1.json ScreenCamera_1.png
    # refer to https://github.com/intel-isl/Open3D/issues/1483
    ctr = vis.get_view_control()
    parameters = o3d.io.read_pinhole_camera_parameters("ScreenCamera_1.json")
    ctr.convert_from_pinhole_camera_parameters(parameters)

    print(dir(parameters)) # class open3d.camera.PinholeCameraParameters  'extrinsic', 'intrinsic'
    print(parameters.extrinsic)   
    # class open3d.camera.PinholeCameraIntrinsic
    # 'get_focal_length', 'get_principal_point', 'get_skew', 'height', 'intrinsic_matrix', 'is_valid', 'set_intrinsics', 'width']
    print(dir(parameters.intrinsic)) 
    print(parameters.intrinsic.intrinsic_matrix)

    vis.run()
    vis.destroy_window()


if __name__ == "__main__": 
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("brain2.ply")
    # print(pcd)

    # custom_draw_geometry(pcd)

    # Bounding volumes
    # aabb - AxisAlignedBoundingBox
    # obb - OrientedBoundingBox
    aabb = pcd.get_axis_aligned_bounding_box()
    aabb.color = (1,0,0)
    obb = pcd.get_oriented_bounding_box()
    obb.color = (0,1,0)
    o3d.visualization.draw_geometries([pcd, aabb, obb],
                                      width=800,
                                      height=600)



