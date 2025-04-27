--- Creacion de la base de datos

GO
DROP DATABASE IF exists Com2900G03
CREATE DATABASE Com2900G03 COLLATE modern_spanish_ci_as
GO
--- Pasamos a usar la base de datos creada
GO
use Com2900G03
GO

--Creacion del esquema administracion

GO
DROP SCHEMA IF exists administracion3
GO
CREATE SCHEMA administracion3
GO

--Creacion del esquema ventas

GO
DROP SCHEMA IF exists ventas3
GO
CREATE SCHEMA ventas3
GO

--Creacion del esquema grupo3

GO
DROP SCHEMA IF exists grupo3
GO
CREATE SCHEMA grupo3
GO

--Creacion del esquema IMPORT

GO
DROP SCHEMA IF exists import3
GO
CREATE SCHEMA import3

GO
DROP SCHEMA IF exists seguridad
GO
Create schema seguridad3
GO


---Creacion de tablas

--CREACION TABLA SUCURSAL
GO
DROP TABLE IF exists administracion3.Sucursal
CREATE TABLE administracion3.Sucursal( id_sucursal int identity(1,1) primary key,
							   Ciudad varchar(20) UNIQUE,
							   Sucursal varchar(30) UNIQUE,
							   Direccion varchar(100) not null,
							   Horario varchar(60),
							   Telefono char(9),
							   FechaBaja date)
GO

--CREACION TABLA EMPLEADO
GO
DROP TABLE IF exists administracion3.Empleado
CREATE TABLE administracion3.Empleado(id_Empleado int identity (257020,1) primary key,
							 Nombre varchar (40),
							 Apellido varchar (40),
							 DNI int,
							 Direccion varchar (100),
							 email_Personal varchar(60),
							 email_Empresa varchar(60),
							 CUIL char(13),
							 Cargo varchar (30),
							 id_Sucursal int not null references administracion3.Sucursal(id_sucursal),
							 Turno varchar(20),
							 FechaBaja date,
							 constraint chk_Turno CHECK(Turno IN('TM','TT','Jornada Completa')))
GO

--CREACION TABLA PRODUCTO
GO
DROP TABLE IF exists administracion3.Producto
CREATE TABLE administracion3.Producto(id_Producto int identity(1,1)  primary key,
                             Categoria varchar(40),
                             Linea_De_Producto varchar(25),
                             Nombre varchar(100),
                             Precio_Unitario decimal(10,2),
                             Precio_De_Referencia decimal(10,2),
                             Unidad_De_Referencia varchar(25),
                             FechaAlta date,
							 FechaBaja date,
							 CONSTRAINT chk_Precio_U_Pos CHECK(Precio_Unitario > 0),
							 CONSTRAINT chk_Precio_Ref_Pos CHECK(Precio_De_Referencia > 0))
GO

--CREACION TABLA FACTURA
GO
DROP TABLE IF exists ventas3.Factura
CREATE TABLE ventas3.Factura(id_Factura int identity (1,1) primary key,
							Numero_Fac char(11) UNIQUE,
							Tipo_Factura char(1),
							Fecha date,
							Hora time,
							Metodo_Pago varchar(15),
							Identificador_de_pago varchar(30),
							Estado varchar(10) default 'Por Pagar',
							Total decimal(10,2),
							Total_Iva decimal (10,2),
							CUIL_Supermercado char(13) default '233-60-0010',
							constraint chk_Metodo_Pago CHECK(Metodo_Pago IN ('Cash','Credit card', 'Ewallet')),
							constraint chk_Tipo_Fac CHECK(Tipo_Factura IN ('A','B','C')))
GO

--CREACION TABLA VENTA
GO
DROP TABLE IF exists ventas3.Venta
CREATE TABLE ventas3.Venta(id_Venta int identity(1,1) primary key,
						  Tipo_Cliente varchar(10),
						  Genero varchar(10),
						  id_Sucursal int references administracion3.Sucursal(id_sucursal),
						  id_Empleado int references administracion3.Empleado(id_Empleado),
						  id_Factura int references ventas3.Factura(id_Factura) UNIQUE,
						  cuil_cte char(13),
						  Fecha date,
						  Fechabaja date,
						  constraint chk_Genero CHECK(Genero IN('Male','Female')),
						  constraint chk_Tipo CHECK(Tipo_Cliente IN ('Normal','Member')))
GO

--CREACION TABLA DETALLE DE VENTA
GO
DROP TABLE IF exists ventas3.Detalle_Venta
CREATE TABLE ventas3.Detalle_Venta(id_Detalle int identity(1,1) primary key,
									Cantidad int not null,
									id_Producto int references administracion3.Producto(id_Producto),
									Precio_Unitario decimal(10,2),
									id_Venta int references ventas3.Venta(id_Venta),
									FechaBaja date)
GO

---CREACION TABLA NOTA DE CREDITO
GO
DROP TABLE IF exists administracion3.Notadecredito
CREATE TABLE administracion3.Notadecredito(id_Nota int identity (1,1) primary key not null,
						id_Factura int not null,
						Total decimal (10,2) not null,
						FechaNota date default getdate(),
						FOREIGN KEY (id_Factura) REFERENCES ventas3.Factura (id_Factura));
GO

