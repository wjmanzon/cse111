# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

    # Draw a cloud
    cloud_center_x = 150
    cloud_bottom = 300
    cloud_height = 150
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)

    # Draw another cloud
    cloud_center_x = 450
    cloud_bottom = 230
    cloud_height = 130
    draw_cloud(canvas, cloud_center_x,
            cloud_bottom, cloud_height)

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 700
    tree_bottom = 20
    tree_height = 450
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 600
    tree_bottom = 0
    tree_height = 450
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw a row of 20 fences.
    draw_fence(canvas)

    # Draw a row of grass
    draw_grass(canvas)

def draw_cloud(canvas, center_x, bottom, height):
    """Draw a single cloud.
    Parameters
        canvas: The canvas where this function
            will draw a cloud.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a cloud.
        height: The height in pixels of the cloud that
            this function will draw.
    Return: nothing
    """
    # cloud_left
    draw_oval(canvas, center_x - 150, bottom, center_x, bottom + height - 50, width=0, fill="white")
    
    # cloud_middle
    draw_oval(canvas, center_x - 100, bottom, center_x + 50, bottom + height, width=0, fill="white")
   
    # cloud_right
    draw_oval(canvas, center_x -30, bottom, center_x + 120, bottom + height - 40, width=0, fill="white")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 12
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 3
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_fence(canvas):
    """
    This draws the fence.
    """
    width = 20
    height = 220
    space = 30
    interval = width + space

    # Draw a row of 27 fences.
    x = 5
    y = 0
    for i in range(27):
        draw_rectangle(canvas, x, y, x + width, y + height,
                fill="white")
        x += interval
    
    # Draw the horizontal lines of the fence
    draw_rectangle(canvas, 0,135,800,150,fill="white")
    draw_rectangle(canvas, 0,50,800,65,fill="white")

def draw_grass(canvas):
    """
    This draws the grass.
    """
  
    width = 2
    height = 45
    space = 2
    interval = width + space

    # Draw a row of grass.
    x = 0
    y = 0
    for i in range(200):
        draw_rectangle(canvas, x, y, x + width, y + height, outline="green",
                fill="green")
        x += interval

# Call the main function so that
# this program will start executing.
main()