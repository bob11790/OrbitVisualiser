from vpython import *

# ---------------- Scene Setup ----------------
scene.background = color.black
scene.title = "Orbit Visualisation\n" \
"Controls:\n" \
"Right-click: rotate\n" \
"shift + left-click: pan\n" \
"mouse-wheel: zoom"
scene.width = 1200
scene.height = 700

# ---------------- Scale ----------------
scale = 1/1000

# ---------------- Bodies ----------------
earth = sphere(
    pos=vector(0,0,0),
    radius=6371*scale,
    color=color.blue
)

moon = sphere(
    pos=vector(384400*scale, 0, 0),
    radius=1737.4*scale,
    color=vector(0.6, 0.6, 0.6)
)

# ---------------- Labels ----------------
label(pos=earth.pos, xoffset=0, yoffset=20, text="Earth", height=10, box=False, line=False, space=30)
label(pos=moon.pos, xoffset=0, yoffset=20, text="Moon", height=10, box=False, line=False, space=30)

# ---------------- Camera Focus Function ----------------
def focus_on_body(clicked_obj):
    if clicked_obj:
        scene.center = clicked_obj.pos
        scene.range = 20  

# --- single click to focus camera ---
while True:
    m = scene.waitfor('click')  # wait for user click
    if m.pick:
        scene.center = m.pick.pos
        scene.range = 20