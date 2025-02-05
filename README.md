# Projeto Bons Fluidos

Projeto de um sistema de Controle de Entrada de Produtos/Estoque/Doações desenvolvido para a disciplina Certificadora Da Competência 1 - EC45G - 2024/2

## Equipe
- Bruno Garcia Baricelo
- Gabriel Marcondes Trigolo
- Mateus Bernardi Alves
- Pedro Coppo Silva
- Pedro Henrique Silva Oliveira

## Descrição
O sistema de Controle de Entrada de Produtos/Estoque/Doações será uma plataforma desenvolvida para otimizar a gestão e o monitoramento de doações e estoques de itens essenciais, como absorventes, itens de higiene pessoal, e outros produtos necessários para atender às beneficiárias do projeto "Bons Fluidos". A iniciativa busca garantir uma distribuição eficiente, equitativa e transparente dos recursos arrecadados, contribuindo para o impacto social positivo e a sustentabilidade do projeto.

### Objetivo
O sistema tem como objetivo atender às demandas operacionais e administrativas relacionadas à arrecadação, gerenciamento e distribuição de recursos. O sistema busca resolver os possíveis problemas de ineficiência, desorganização e falta de transparência que podem surgir no gerenciamento do projeto, garantindo uma operação mais estruturada e confiável. Ele atenderá às necessidades de beneficiários, voluntários, apoiadores e coordenadores de forma clara e eficiente.

## Como executar o projeto  

Para executar o **Projeto Bons Fluidos** corretamente, siga os passos abaixo:  

### 1. Requisitos  
Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:  
- **Python 3.12.2**
- **MySQL Server**  
- **Biblioteca `mysql-connector-python`**  
- **Uma IDE compatível com Python**, como PyCharm, Visual Studio Code ou outra de sua preferência  

### 2. Preparando o Banco de Dados  
1. Abra o MySQL Workbench ou o terminal do MySQL.  
2. Execute o script `BD.SQL` que acompanha o projeto para criar e configurar o banco de dados necessário.  
   - Esse script cria as tabelas e insere os dados iniciais necessários para o funcionamento do sistema.  
   - Certifique-se de que o banco de dados foi criado corretamente e está ativo.  

### 3. Instalando Dependências  
No terminal, instale o driver MySQL para Python com o seguinte comando:  `pip install mysql-connector-python`

### 4. Abrindo o Projeto  
1. Faça o download ou clone o repositório do projeto em sua máquina.  
2. Abra o diretório do projeto na sua IDE. Certifique-se de abrir a pasta raiz chamada `ProjetoBonsFluidosCompleto` para evitar problemas de importação.  

### 5. Executando o Sistema  
1. Verifique se o banco de dados está em execução.  
2. Na sua IDE, abra o arquivo principal (`PaginaLogin.py` ou outro arquivo principal definido no seu projeto).  
3. Execute o projeto a partir da sua IDE clicando no botão de execução ou usando o atalho padrão (`Shift+F10` no PyCharm, por exemplo).  

Se tudo estiver configurado corretamente, o sistema estará pronto para uso.  

