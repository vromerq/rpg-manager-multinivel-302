USE rpg_manager;

CREATE TABLE clase (
    id_clase INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(200)
);

CREATE TABLE personaje (
    id_personaje INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    id_clase INT,
    nivel INT CHECK (nivel BETWEEN 1 AND 5),
    vida INT CHECK (vida BETWEEN 1 AND 100),
    FOREIGN KEY (id_clase) REFERENCES clase (id_clase)
);