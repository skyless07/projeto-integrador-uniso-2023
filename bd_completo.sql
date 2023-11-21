create database basepj;
use basepj;

create table ativos(
id int primary key auto_increment,
marca varchar(50),
valor int
);


create table setores (
id int primary key auto_increment,
nome varchar (50)
);

create table funcionarios(
id int primary key auto_increment,
nome varchar (50),
salario int
);

create table ondetrabalha (
id_setor int,
id_funcionario int,
PRIMARY KEY (id_setor, id_funcionario),
foreign key (id_setor) references setores(id),
foreign key (id_funcionario) references funcionarios(id)
);

create table qualsetor (
id_setor int,
id_ativo int,
primary key (id_setor, id_ativo),
foreign key (id_setor) references setores(id),
foreign key (id_ativo) references ativos(id)
);

insert into setores values
(1, "RH"),
(2, "Financeiro"),
(3, "Desenvolvimento"),
(4, "Suporte"),
(5, "Comercial"),
(6, "Produção");	