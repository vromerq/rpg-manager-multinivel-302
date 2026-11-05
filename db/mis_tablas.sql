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
    nivel INT CHECK (nivel BETWEEN 1 AND 100),
    vida INT CHECK (vida BETWEEN 10 AND 50),
    FOREIGN KEY (id_clase) REFERENCES clase (id_clase)
);

CREATE TABLE item (
  id_item INT AUTO_INCREMENT PRIMARY KEY,
  nombre  VARCHAR(50) NOT NULL UNIQUE,
  tipo    ENUM('arma','armadura','pocion','reliquia'),
  valor   DECIMAL(10,2) NOT NULL DEFAULT 0,
  peso    DECIMAL(6,2)  NOT NULL DEFAULT 0
);

-- Relación muchos a muchos: un personaje tiene varios items y un item lo tienen varios personajes
CREATE TABLE inventario (
  id_personaje INT NOT NULL,
  id_item      INT NOT NULL,
  cantidad     INT NOT NULL DEFAULT 1,
  PRIMARY KEY (id_personaje, id_item),
  FOREIGN KEY (id_personaje) REFERENCES personaje(id_personaje),
  FOREIGN KEY (id_item) REFERENCES item(id_item)
);
 
CREATE TABLE mision (
  id_mision  INT AUTO_INCREMENT PRIMARY KEY,
  titulo     VARCHAR(80) NOT NULL UNIQUE,
  dificultad ENUM('facil','media','dificil','legendaria') NOT NULL,
  recompensa INT NOT NULL
);
 
CREATE TABLE personaje_mision (
  id_personaje INT NOT NULL,
  id_mision    INT NOT NULL,
  estado       ENUM('aceptada','completada') NOT NULL,
  PRIMARY KEY (id_personaje, id_mision),
  FOREIGN KEY (id_personaje) REFERENCES personaje(id_personaje),
  FOREIGN KEY (id_mision) REFERENCES mision(id_mision)
);
 
 CREATE TABLE combate (
  id_combate  INT AUTO_INCREMENT PRIMARY KEY,
  id_atacante INT NOT NULL,
  id_defensor INT NOT NULL,
  id_ganador  INT NULL,
  fecha       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_atacante) REFERENCES personaje(id_personaje),
  FOREIGN KEY (id_defensor) REFERENCES personaje(id_personaje),
  FOREIGN KEY (id_ganador)  REFERENCES personaje(id_personaje),
  CHECK (id_atacante <> id_defensor),
  CHECK (id_ganador IS NULL OR id_ganador IN (id_atacante, id_defensor))
);