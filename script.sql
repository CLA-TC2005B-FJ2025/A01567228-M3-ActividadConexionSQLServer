CREATE TABLE Productos (
    ID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(50),
    Precio DECIMAL(10, 2)
);

INSERT INTO Productos (Nombre, Precio) VALUES ('Laptop', 1500.00);
INSERT INTO Productos (Nombre, Precio) VALUES ('Mouse', 25.50);

SELECT * FROM Productos;
