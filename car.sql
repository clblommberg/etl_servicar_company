CREATE DATABASE car_company;
USE car_company;
CREATE TABLE Inventario (
  idinventario INT PRIMARY KEY,
  idproducto INT,
  stock_inicial INT,
  stock_actual INT,
  stock_final INT
);

CREATE TABLE Vehiculoscliente (
  idvehiculo INT AUTO_INCREMENT PRIMARY KEY,
  nombrecliente VARCHAR(100),
  Marca_Modelo VARCHAR(100),
  Placa VARCHAR(20),
  Ubicacion VARCHAR(100)
);

CREATE TABLE Productos (
  idproducto INT AUTO_INCREMENT PRIMARY KEY,
  linea_negocio VARCHAR(100),
  nombreproducto VARCHAR(100),
  Precio DECIMAL(10, 2)
);

CREATE TABLE Conversion (
  idconversion INT AUTO_INCREMENT PRIMARY KEY,
  nconversion VARCHAR(50),
  galones INT,
  aplicacion VARCHAR(50),
  idinventario INT
);

CREATE TABLE Aplicacion (
  idaplicacion INT AUTO_INCREMENT PRIMARY KEY,
  aplicacion_name VARCHAR(50)
);

CREATE TABLE Servicios (
  idservicio INT AUTO_INCREMENT PRIMARY KEY,
  Descripcion VARCHAR(100),
  Precio DECIMAL(10, 2)
);

CREATE TABLE Kit (
  idkit INT PRIMARY KEY,
  kitname VARCHAR(50),
  idinventario INT,
  FOREIGN KEY (idinventario) REFERENCES Inventario(idinventario)
);
CREATE TABLE Transacciones (
  idtransaccion INT AUTO_INCREMENT PRIMARY KEY,
  Fecha DATE,
  iddocumento VARCHAR(100),
  idvehiculo ID_Vehiculo INT,
  idproductotanque INT,
  idproducto INT,
  certifica INT,
  costotanque DECIMAL(10, 2),
  costokit DECIMAL(10,2),
  costocertificacion DECIMAL(10,2),
  precioventa DECIMAL(10,2),
  Ganancia DECIMAL(10, 2),
  idconversion INT,
  idkit INT,
  idaplicacion INT
);

CREATE TABLE Pagos (
  idpago INT AUTO_INCREMENT PRIMARY KEY,
  idtransaccion INT,
  Efectivo DECIMAL(10, 2),
  BCP DECIMAL(10, 2),
  Tarjeta DECIMAL(10, 2)
);