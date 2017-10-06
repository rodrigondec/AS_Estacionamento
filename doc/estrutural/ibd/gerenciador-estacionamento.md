![](/doc/img/GerenciadorEstacionamento.jpg)

---

# **GerenciadorEstacionamento**

No **GerenciadorEstacionamento** temos componentes tanto simples, quanto compostos.



## Simples

### ControladorVagaCP

O **ControladorVagaCP** age como uma interface para o banco de dados, fornecendo informações pertinentes às vagas.

### ControladorRelatorioCP

O **ControladorRelatorioCP** age como uma interface e filtro para o banco de dados, fornecendo as informações pertinentes para gerar os relatórios.

### ControladorTicketCP

O **ControladorTicketCP** age tanto como uma interface para o banco de dados, quanto um processador de dados para o funcionamento das entradas, saídas e pagamentos.



## Compostos

### EntradaCP

Possui os componentes responsáveis pelas entradas do estacionamento.

### SaídaCP

Possui os componentes responsáveis pelas saídas do estacionamento.

### GerenciadorCancelaCP

Possui os componentes responsáveis pelas cancelas do estacionamento e o processamento de seus comandos.

### GerenciadorPagamentoCP

Possui os componentes responsáveis pelas centrais de pagamento e seus processamentos.

### GerenciadorVagaCP

Possui os componentes responsáveis pelas vagas e seus processamentos.

### GerenciadorRelatorioCP

Possui os componentes responsáveis pelos relatórios e seus processamentos.

