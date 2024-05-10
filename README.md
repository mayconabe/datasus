# Relatório Projeto Integrador DATASUS
DATASUS é o Departamento de Informática do Sistema Único de Saúde no Brasil. Trata-
se de um órgão vinculado ao Ministério da Saúde, responsável por gerenciar e disponibilizar
informações sobre saúde no país. O principal objetivo do DATASUS é coletar, processar, analisar
e disseminar dados relacionados à saúde para apoiar o planejamento, gestão e avaliação do
sistema de saúde brasileiro.
O propósito deste projeto consiste na elaboração de uma base de dados contendo
informações sobre as internações hospitalares ocorridas entre os anos de 2019 e 2023, com uma
granularidade temporal mensal e uma agregação geográfica por município.

# Web Scraping
A coleta dos dados foram feitas com uma biblioteca em Python chamada "Selenium".
Selenium é uma ferramenta muito poderosa e popular no ecossistema Python, especialmente no
campo da automação de testes e interações com navegadores web. Ela oferece uma gama de
funcionalidades para controlar e interagir com navegadores da web de forma programática.
O código feito utilizou o "Chromium", que é um Webdriver do navegador Chrome. No
código acessamos o site do DATASUS e pegamos as informações de 2019 até 2023, após toda
a coleta, foi gerado um arquivo em CSV para a leitura no Python ou SAS Viya.

# Carga de Dados
Após a conclusão de todos os estágios de tratamento dos dados, procedemos com a
carga manual utilizando a ferramenta DBeaver para realizar a inserção dos dados no banco de
dados PostgreSQL.

# Dicionário de Dados

| Variável                                                                          | Descrição                                                                                               |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Município                                                                         | Código do município onde as ações de saúde estão sendo realizadas.                                       |
| Ações coletivas/individuais em saúde                                         | Número de ações de saúde coletivas ou individuais realizadas.                                             |
| Coleta de material                                                           | Número de procedimentos de coleta de material médico realizados.                                           |
| Diagnóstico em laboratório clínico                                           | Número de diagnósticos realizados em laboratório clínico.                                                 |
| Diagnóstico por anatomia patológica e citopatologia                          | Número de diagnósticos realizados por anatomia patológica e citopatologia.                                |
| Diagnóstico por radiologia                                                   | Número de diagnósticos realizados por radiologia.                                                          |
| Diagnóstico por ultrassonografia                                             | Número de diagnósticos realizados por ultrassonografia.                                                    |
| Diagnóstico por tomografia                                                   | Número de diagnósticos realizados por tomografia.                                                          |
| Diagnóstico por ressonância magnética                                        | Número de diagnósticos realizados por ressonância magnética.                                               |
| Diagnóstico por medicina nuclear in vivo                                     | Número de diagnósticos realizados por medicina nuclear in vivo.                                            |
| Diagnóstico por endoscopia                                                   | Número de diagnósticos realizados por endoscopia.                                                          |
| Diagnóstico por radiologia intervencionista                                   | Número de diagnósticos realizados por radiologia intervencionista.                                          |
| Métodos diagnósticos em especialidades                                       | Número de diagnósticos realizados por métodos específicos em diferentes especialidades médicas.           |
| Diagnóstico e procedimentos especiais em hemoterapia                         | Número de diagnósticos e procedimentos especiais realizados em hemoterapia.                                |
| Diagnóstico por teste rápido                                                 | Número de diagnósticos realizados por teste rápido.                                                        |
| Consultas / Atendimentos / Acompanhamentos                                    | Número de consultas, atendimentos ou acompanhamentos realizados.                                           |
| Fisioterapia                                                                 | Número de sessões de fisioterapia realizadas.                                                              |
| Tratamentos clínicos (outras especialidades)                                  | Número de tratamentos clínicos realizados em outras especialidades médicas.                                |
| Tratamento em oncologia                                                      | Número de tratamentos realizados em oncologia.                                                             |
| Tratamento em nefrologia                                                     | Número de tratamentos realizados em nefrologia.                                                            |
| Hemoterapia                                                                   | Número de procedimentos de hemoterapia realizados.                                                         |
| Tratamentos odontológicos                                                     | Número de tratamentos odontológicos realizados.                                                           |
| Tratamento de lesões, envenenamentos e outros, decorrentes de causas externas | Número de tratamentos realizados para lesões, envenenamentos e outros casos decorrentes de causas externas. |
| Terapias especializadas                                                       | Número de terapias especializadas realizadas.                                                             |
| Parto e nascimento                                                            | Número de partos e nascimentos ocorridos.                                                                 |
| Pequenas cirurgias e cirurgias de pele, tecido subcutâneo e mucosa            | Número de pequenas cirurgias e cirurgias de pele, tecido subcutâneo e mucosa realizadas.                  |
| Cirurgia de glândulas endócrinas                                              | Número de cirurgias realizadas nas glândulas endócrinas.                                                   |
| Cirurgia do sistema nervoso central e periférico                              | Número de cirurgias realizadas no sistema nervoso central e periférico.                                   |
| Cirurgia das vias aéreas superiores, da face, da cabeça e do pescoço          | Número de cirurgias realizadas nas vias aéreas superiores, face, cabeça e pescoço.                        |
| Cirurgia do aparelho da visão                                                 | Número de cirurgias realizadas no aparelho da visão.                                                       |
| Cirurgia do aparelho circulatório                                             | Número de cirurgias realizadas no aparelho circulatório.                                                   |
| Cirurgia do aparelho digestivo, orgãos anexos e parede abdominal               | Número de cirurgias realizadas no aparelho digestivo, órgãos anexos e parede abdominal.                    |
| Cirurgia do sistema osteomuscular                                             | Número de cirurgias realizadas no sistema osteomuscular.                                                   |
| Cirurgia do aparelho geniturinário                                            | Número de cirurgias realizadas no aparelho geniturinário.                                                  |
| Cirurgia de mama                                                              | Número de cirurgias realizadas na mama.                                                                    |
| Cirurgia obstétrica                                                           | Número de cirurgias obstétricas realizadas.                                                               |
| Cirurgia torácica                                                             | Número de cirurgias torácicas realizadas.                                                                 |
| Cirurgia reparadora                                                           | Número de cirurgias reparadoras realizadas.                                                                |
| Bucomaxilofacial                                                              | Número de cirurgias bucomaxilofaciais realizadas.                                                          |
| Outras cirurgias                                                              | Número de outras cirurgias realizadas.                                                                    |
| Cirurgia em oncologia                                                         | Número de cirurgias realizadas em oncologia.                                                               |
| Cirurgia em nefrologia                                                        | Número de cirurgias realizadas em nefrologia.                                                              |
| Coleta e exames para fins de doação de orgãos, tecidos e células e de transplante | Número de coletas e exames realizados para fins de doação de órgãos, tecidos e células e de transplante. |
| Avaliação de morte encefálica                                                | Número de avaliações de morte encefálica realizadas.                                                       |
| Ações relacionadas à doação de orgãos e tecidos para transplante             | Número de ações relacionadas à doação de órgãos e tecidos para transplante.                                |
| Processamento de tecidos para transplante                                     | Número de processamentos de tecidos realizados para transplante.                                           |
| Transplante de órgãos, tecidos e células                                      | Número de transplantes de órgãos, tecidos e células realizados.                                             |
| Acompanhamento e intercorrências no pré e pós-transplante                     | Número de acompanhamentos e intercorrências no pré e pós-transplante.                                       |
| Medicamentos de âmbito hospitalar e urgência                                  | Número de medicamentos de âmbito hospitalar e urgência administrados.                                       |
| Órteses, próteses e materiais especiais relacionados ao ato cirúrgico          | Número de órteses, próteses e materiais especiais relacionados ao ato cirúrgico utilizados.               |
| Ações relacionadas ao estabelecimento                                         | Número de ações relacionadas ao estabelecimento de saúde.                                                  |
| Ações relacionadas ao atendimento                                             | Número de ações relacionadas ao atendimento em saúde.                                                      |
| Total                                                                             | Total de todas as ações ou procedimentos realizados.                                                       |
| Mes                                                                               | Mês em que os dados foram coletados.                                                                      |
| Ano                                                                               | Ano em que os dados foram coletados.                                                                      |
| Conteudo                                                                          | Conteúdo associado ao mês e ano da primeira coleta de dados.                                               |
