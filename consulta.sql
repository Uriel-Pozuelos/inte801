# consulta para saber cual es la galleta mas vendida
SELECT g.nombre, SUM(dv.cantidad) as cantidad_vendida FROM detalleventa dv
JOIN galletas g ON g.id = dv.galleta_id
GROUP BY g.nombre
ORDER BY cantidad_vendida DESC;

# consulta para saber la galleta que mas merma produce
SELECT g.nombre, SUM(m.cantidad) as cantidad_merma FROM merma_galletas m
JOIN inventariogalletas ig ON ig.idLoteGalletas = m.idInventarioGalletas
JOIN galletas g ON g.id = ig.idGalleta
GROUP BY g.nombre
ORDER BY cantidad_merma DESC;

# AUN NO ESTA BIEN
# consulta para saber que galleta deberia producir para obtener la mayor utilidad usando row_number
SELECT g.nombre, 
SUM(dv.cantidad * g.`pesoGalleta`) as total_vendido,
SUM(m.cantidad * g.`pesoGalleta`) as total_merma, 
SUM(dv.cantidad * g.`pesoGalleta`) - SUM(m.cantidad * g.`pesoGalleta`) as utilidad FROM detalleventa dv
JOIN galletas g ON g.id = dv.galleta_id
JOIN merma_galletas m ON m.idInventarioGalletas = dv.galleta_id
GROUP BY g.nombre
ORDER BY utilidad DESC;


# AUN NO ESTA BIEN CREo
# consulta para saber acorde a las materias primas que tengo, si se escoge una receta, cuanto me costara la produccion de cada tipo de galleta
select sum(costo_produccion) from(
SELECT 
    nombre_material,
    sum(costo_material) as costo_produccion,
    cantidad_utilizada
FROM
    (SELECT
        mp.material AS nombre_material,
        i.cantidad AS cantidad_utilizada,
        ROUND((i.cantidad * g.precio), 2) / 100 AS costo_material
    FROM
        ingredientes i
    JOIN
        materiaprima mp ON i.material_id = mp.id
    JOIN
        galletas g ON i.galleta_id = g.id
    WHERE
        g.id = 4) AS materiales
GROUP BY
    nombre_material) as p;
    

#saber cuanto cuesta cada gramo de materia prima
SELECT 
    mp.material,
    mpp.precio,
    c.cantidadConvertida,
    c.tipoConvertido,
    c.`tipoConvertido` as tipo,
    ROUND((mpp.precio / c.cantidadConvertida), 2) as precio_por_gramo
FROM
    materia_prima_proveedor mpp
LEFT JOIN
    conversiones c ON c.tipoSinConvertir = mpp.tipo
   left JOIN
    materiaprima mp ON mpp.materiaprima_id = mp.id;
    
#unir con la consulta anterior con la tabla de ingredientes y galletas para saber cuanto cuesta producir una galleta
SELECT 
    g.nombre,
    mp.material,
    i.cantidad,
    mpp.precio,
    c.cantidadConvertida,
    c.tipoConvertido,
    ROUND((mpp.precio / c.cantidadConvertida), 2) as precio_por_gramo,
    ROUND((i.cantidad * (mpp.precio / c.cantidadConvertida)), 2) as costo_produccion
FROM
    ingredientes i
left JOIN
    galletas g ON i.galleta_id = g.id
left JOIN
    materiaprima mp ON i.material_id = mp.id
left JOIN
    materia_prima_proveedor mpp ON mpp.materiaprima_id = mp.id
left JOIN
    conversiones c ON c.tipoSinConvertir = mp.tipo;


#consulta para convertir la cantidad de materia prima que se necesita para una receta a gramos
SELECT 
    mp.material,
    i.cantidad,
    c.cantidadConvertida,
    c.tipoConvertido
FROM
    ingredientes i
left JOIN
    materiaprima mp ON i.material_id = mp.id
left JOIN
    conversiones c ON c.tipoSinConvertir = mp.tipo;
    
SELECT galletas.id, galletas.nombre, galletas.precio, galletas.estatus, galletas.created_at, galletas.updated_at, galletas.deleted_at, materiaprima.material, materiaprima.tipo
FROM galletas
JOIN (
    SELECT galletas.id, galletas.nombre, galletas.precio, galletas.estatus, galletas.created_at, galletas.updated_at, galletas.deleted_at, materia_prima_galleta.materiaprima_id
    FROM galletas
    JOIN materia_prima_galleta ON materia_prima_galleta.galleta_id = galletas.id
    WHERE galletas.id = 1
) AS galletas_materia_prima ON galletas_materia_prima.id = galletas.id;

select * from inventariogalletas;
select * from produccion;
select * from solicitudproduccion;
# consulta para saber un determinado lote de galletas, saber que empreado la produjo
SELECT inventariogalletas.idLoteGalletas, inventariogalletas.idGalleta, inventariogalletas.cantidad, inventariogalletas.fechaCaducidad, inventariogalletas.estatus, inventariogalletas.created_at, inventariogalletas.updated_at, inventariogalletas.deleted_at, usuario.nombre, usuario.apellido
FROM inventariogalletas
JOIN produccion ON produccion.idProduccion = inventariogalletas.idLoteGalletas
JOIN usuario ON usuario.id = produccion.idUsuario
WHERE inventariogalletas.idLoteGalletas = 22;

# consulta para saber un determinado lote de galletas, saber que proveedor proporciono la materia prima
SELECT inventariogalletas.idLoteGalletas, inventariogalletas.idGalleta, inventariogalletas.cantidad, inventariogalletas.fechaCaducidad, inventariogalletas.estatus, inventariogalletas.created_at, inventariogalletas.updated_at, inventariogalletas.deleted_at, proveedor.nombre_empresa
FROM inventariogalletas
JOIN materia_prima_proveedor ON materia_prima_proveedor.materiaprima_id = inventariogalletas.idGalleta
JOIN proveedor ON proveedor.id = materia_prima_proveedor.proveedor_id
WHERE inventariogalletas.idLoteGalletas = 22;


select concat(u.nombre, ' ', u.apellido) as nombre_empleado, ig.idLoteGalletas
JOIN produccion p ON p.idSolicitud = ig.idSolicitud
JOIN usuario u ON u.id = p.idUsuario;