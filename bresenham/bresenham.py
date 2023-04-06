def get_line(x0, y0, x1, y1):
    points = [] # lista para almacenar puntos generados
    # 1er paso: dx, dy
    dx = x1 - x0
    dy = y1 - y0
    # variables para iterar xk, yk
    xk = x0
    yk = y0
    y_inc = 1

    if dy < 0:
        dy = -1 * dy
        y_inc = -1

    # determinar si la línea es más vertical u horizontal
    is_steep = abs(dy) > abs(dx)

    # si la línea es más vertical que horizontal, intercambiar x y y
    if is_steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        dx, dy = dy, dx

    # determinar la dirección de x
    x_inc = 1
    if dx < 0:
        dx = -dx
        x_inc = -1

    # 2do paso: parametro de decision Pk
    Pk = 2 * dy - dx

    # 3er paso: iterar hasta el punto final:
    while xk != x1:
        # agregar punto a la lista
        if is_steep:
            points.append((yk, xk))
        else:
            points.append((xk, yk))

        xk += x_inc
        # decido en base a Pk si y incrementa o no
        if Pk < 0:
            Pk += 2 * dy
        else:
            Pk += 2 * dy - 2 * dx
            yk += y_inc

    # agregar el punto final a la lista
    if is_steep:
        points.append((y1, x1))
    else:
        points.append((x1, y1))

    return points
