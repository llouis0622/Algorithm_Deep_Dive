import math

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())
ABx, ABy, ABz = Bx - Ax, By - Ay, Bz - Az
ACx, ACy, ACz = Cx - Ax, Cy - Ay, Cz - Az
AB_num = ABx * ABx + ABy * ABy + ABz * ABz
if AB_num == 0:
    temp = math.sqrt((Ax - Cx) ** 2 + (Ay - Cy) ** 2 + (Az - Cz) ** 2)
else:
    t = (ACx * ABx + ACy * ABy + ACz * ABz) / AB_num
    if t < 0.0:
        near_x, near_y, near_z = Ax, Ay, Az
    elif t > 1.0:
        near_x, near_y, near_z = Bx, By, Bz
    else:
        near_x = Ax + t * ABx
        near_y = Ay + t * ABy
        near_z = Az + t * ABz
    temp = math.sqrt((near_x - Cx) ** 2 + (near_y - Cy) ** 2 + (near_z - Cz) ** 2)
print(f"{temp:.10f}")