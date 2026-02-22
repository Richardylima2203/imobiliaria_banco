CREATE TABLE ceps (
     cep INT PRIMARY KEY,  
     endereco VARCHAR(100) NOT NULL, 
     bairro VARCHAR(20) NOT NULL, 
     cidade VARCHAR(20) NOT NULL, 
     estado VARCHAR(2) NOT NULL
)

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    cep INT NOT NULL,
    numero INT NOT NULL,
    complemento VARCHAR(20),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cep) REFERENCES ceps(cep)
)


CREATE TABLE imoveis (
    id_imovel INT PRIMARY KEY AUTO_INCREMENT,
    id_proprietario INT NOT NULL,
    cep INT NOT NULL,
    numero INT NOT NULL,
    complemento VARCHAR(30),
    tipo VARCHAR(30) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_proprietario) REFERENCES clientes(id_cliente),
    FOREIGN KEY (cep) REFERENCES ceps(cep)
)
    

CREATE TABLE contratos (
    id_contrato INT PRIMARY KEY AUTO_INCREMENT,
    id_inquilino INT NOT NULL,
    id_fiador INT NOT NULL,
    id_imovel INT NOT NULL,
    prazo INT NOT NULL,
    inicio DATE NOT NULL,
    fim DATE NOT NULL,
    FOREIGN KEY (id_inquilino) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_fiador) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_imovel) REFERENCES imoveis(id_imovel)
)







