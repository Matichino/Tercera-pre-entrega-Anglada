# TerceraEntrega-Anglada-Python-
A la web le falta la revision de datos que existan mas inclusion de los datos en BD, estan puestos los codigos pero falta darle adaptabilidad
y funcionalidad.
Estoy encarando el proyecto final, buscando hacer una pagina a futuro funcional
Aqui los usuarios registrados y el superusuario
la idea es poner los formularios en el index para que el mismo cliente se de alta en mi sistema, con inclusion de una ventana aparte para revisar
el estatuts de su caso.
los clientes se registran con un numero para evitar la creacion de usuarios, donde el cliente tiene 
un usuario numerico que se crea y se le suben datos de su caso con el superusuario.



Superusuario
usuario Test
email matias@abc.com
contraseña maradona

usuario comun
messi
contraseña 5587messi

usuario = models.IntegerField()
    contraseña= models.CharField(max_length=8)
    numero_de_caso= models.CharField(max_length=10)