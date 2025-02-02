CREATE DATABASE IF NOT EXISTS testeprojeto;
USE testeprojeto;
CREATE TABLE produto (
    produto_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    descricao VARCHAR(255),
    quantidade INT,
    data_doacao DATE
);
CREATE TABLE beneficiario (
    beneficiario_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    cnpj_cpf VARCHAR(255) UNIQUE
);
CREATE TABLE distribuicao (
    distribuicao_id INT AUTO_INCREMENT PRIMARY KEY,
    beneficiario_id INT,
    produto_id INT,
    data_distribuicao DATE,
    quantidade INT,
    FOREIGN KEY (beneficiario_id) REFERENCES beneficiario(beneficiario_id),
    FOREIGN KEY (produto_id) REFERENCES produto(produto_id)
);
CREATE TABLE doacao (
    doacao_id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    data_doacao DATE,
    quantidade INT,
    doador VARCHAR(255),
    FOREIGN KEY (produto_id) REFERENCES produto(produto_id)
);
CREATE TABLE usuario (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    senha VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    cargo VARCHAR(255)
);
