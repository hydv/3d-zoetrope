import bpy
import math

def delete_all():
    for item in bpy.context.scene.objects:
        bpy.context.scene.objects.unlink(item)
    for item in bpy.data.objects:
        bpy.data.objects.remove(item)
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)
    for item in bpy.data.materials:
        bpy.data.materials.remove(item)

def make_boolean_union():
    base_cube = bpy.data.objects[0]
    bpy.context.scene.objects.active = base_cube
    for i, cube in enumerate(bpy.data.objects):
        if i == 0:
            continue
        boolean = base_cube.modifiers.new('ConeBoolean', 'BOOLEAN')
        boolean.object = cube
        boolean.operation = 'UNION'
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='CubeBoolean')
        bpy.context.scene.objects.unlink(cube)

class Object:
    def __init__(self, num, size, lx, ly, lz, r):
        self.num = num
        self.size = size
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.r = r

delete_all()

cubes = []

for i in range(450):
    angle = math.radians(137.5*i)
    x = (700-1.2*i)/500*math.cos(angle)
    y = (700-1.2*i)/500*math.sin(angle)
    z = -0.3+i/50
    ln = math.sqrt(x*x + y*y + z*z)
    x = 10*x/ln
    y = 10*y/ln
    z = 10*z/ln
    cubes.append(Object(i, 120/(60+pow(i/1.2,1.01)), x, y, z, angle))

for cube in cubes:
    bpy.ops.mesh.primitive_cube_add(location=(cube.lx, cube.ly, cube.lz), rotation=(0.4, 0.17*cube.r, cube.r))
    ob = bpy.context.scene.objects.active
    ob.scale = (cube.size, cube.size, cube.size)
    #ob.rotation_euler = (0, 0, 0)
    #print(cube.x, cube.y, cube.z)

make_boolean_union()
