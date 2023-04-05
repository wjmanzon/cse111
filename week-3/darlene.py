import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """

    # Test draw
    # test_draw(canvas)
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # sky
    draw_sky(canvas,0,0)

    # sea
    draw_sea(canvas,0,0)

    # land
    land_x = 0
    land_y = 0
    draw_land(canvas, land_x, land_y)

    land_x = 700
    land_y = -50
    draw_land(canvas, land_x, land_y)

    land_x = 450
    land_y = 50
    draw_land(canvas, land_x, land_y)

    # tree
    tree_center = scene_left + 780
    tree_top = scene_top + 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 720
    tree_top = scene_top + 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 750
    tree_top = scene_top + 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 250
    tree_top = scene_top + 250
    tree_height = 120
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 200
    tree_top = scene_top + 250
    tree_height = 120
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 70
    tree_top = scene_top + 300
    tree_height = 160
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # sun
    sun_x = 400
    sun_y = -25
    sun_size = 450
    sun_opacity = "gray25"
    sun_opacity_border = "gray25"
    sun_color = "#fa900f"
    draw_sun(canvas,sun_x,sun_y, sun_size, sun_opacity, sun_opacity_border, sun_color)

    sun_x = 400
    sun_y = 50
    sun_size = 300
    sun_opacity = "gray25"
    sun_opacity_border = "gray25"
    sun_color = "#fae22f"
    draw_sun(canvas,sun_x,sun_y, sun_size, sun_opacity, sun_opacity_border, sun_color)

    sun_x = 400
    sun_y = 125
    sun_size = 150
    sun_opacity = ""
    sun_opacity_border = ""
    sun_color = "#ffc800"
    draw_sun(canvas,sun_x,sun_y, sun_size, sun_opacity, sun_opacity_border, sun_color)

    # sun reflection on sea
    sun_refl_x = 150
    sun_refl_y = 176
    sun_refl_size = 500
    color = "#fff200"
    opacity = "gray25"
    opacity_border = "gray25"
    draw_sun_reflection_on_sea(canvas,sun_refl_x,sun_refl_y, sun_refl_size, color, opacity, opacity_border)

    sun_refl_x = 225
    sun_refl_y = 182
    sun_refl_size = 350
    color = "#ffcc00"
    opacity = "gray50"
    opacity_border = "gray50"
    draw_sun_reflection_on_sea(canvas,sun_refl_x,sun_refl_y, sun_refl_size, color, opacity, opacity_border)

    sun_refl_x = 275
    sun_refl_y = 187
    sun_refl_size = 250
    color = "#ffb300"
    opacity = "gray75"
    opacity_border = "gray75"
    draw_sun_reflection_on_sea(canvas,sun_refl_x,sun_refl_y, sun_refl_size, color, opacity, opacity_border)

    sun_refl_x = 300
    sun_refl_y = 190
    sun_refl_size = 200
    color = "orange"
    opacity = ""
    opacity_border = ""
    draw_sun_reflection_on_sea(canvas,sun_refl_x,sun_refl_y, sun_refl_size, color, opacity, opacity_border)

    # clouds
    clouds_x = 500
    clouds_y = 100
    cloud_size = 70
    cloud_color = "#fff"
    draw_clouds(canvas,clouds_x,clouds_y,cloud_size,cloud_color)

    clouds_x = 0
    clouds_y = 100
    cloud_size = 70
    cloud_color = "#fff"
    draw_clouds(canvas,clouds_x,clouds_y,cloud_size,cloud_color)

    clouds_x = 75
    clouds_y = -5
    cloud_size = 80
    cloud_color = "#fff"
    draw_clouds(canvas,clouds_x,clouds_y,cloud_size,cloud_color)
    
    # Guideline
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_clouds(canvas,x,y,size,color):
    canvas.create_arc(x,y,x+size,y+size, start=0, extent=180, style="chord", fill=color, outline=color)
    canvas.create_arc(x+size/2, y-size/2, x+size+size/2, y+size+size/2, start=0, extent=180, style="chord", fill=color, outline=color)
    canvas.create_arc(x+((size/2)*3),y,x+size+((size/2)*3),y+size, start=0, extent=180, style="chord", fill=color, outline=color)
    


def draw_sea(canvas,x,y):
    canvas.create_rectangle(0,200,800,500, fill="#235d96", outline="#235d96")


def draw_sun_reflection_on_sea(canvas, x, y, size, c, st, ost):
    canvas.create_arc(x, y, x+size, y+(size/10), start=180, extent=180, fill=c, outline=c, stipple=st, outlinestipple=ost)


def draw_sky(canvas, x, y):
    canvas.create_rectangle(0,0,800,500, fill="#f79786")


def draw_sun(canvas, x, y, size, st, ost, color):
    # default size is width=150
    pos_x = x-(size/2)
    canvas.create_arc(pos_x, y, pos_x+size, y+size, start=0, extent=180, style="chord", fill=color, outline=color, stipple=st, outlinestipple=ost)


def draw_land(canvas, x, y):
    canvas.create_polygon(0+x, 350+y,
                        200+x, 300+y,
                        300+x, 350+y,
                        500+x, 400+y,
                        800+x, 250+y,
                        800+x, 500+y,
                        0+x, 500+y,
                        fill="#c25815", smooth=1)
    

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree,
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: Nothin
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green", smooth=1)


def draw_grid(canvas, left, top, right, bottom, grid_space):
    
    text_horizontal_margin = 20
    text_vertical_margin = 10
    #horizontal lines
    for i in range(top, bottom, grid_space):
        canvas.create_line(left,i,right,i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    
    #vertical lines
    for i in range(left, right, grid_space):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

# Call the main function so that
# this program will start executing
main()