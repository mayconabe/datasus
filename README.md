# Relatório Projeto Integrador DATASUS\
DATASUS é o Departamento de Informática do Sistema Único de Saúde no Brasil. Trata-\
se de um órgão vinculado ao Ministério da Saúde, responsável por gerenciar e disponibilizar\
informações sobre saúde no país. O principal objetivo do DATASUS é coletar, processar, analisar\
e disseminar dados relacionados à saúde para apoiar o planejamento, gestão e avaliação do\
sistema de saúde brasileiro.\
O propósito deste projeto consiste na elaboração de uma base de dados contendo\
informações sobre as internações hospitalares ocorridas entre os anos de 2019 e 2023, com uma\
granularidade temporal mensal e uma agregação geográfica por município.\

# Web Scraping\
A coleta dos dados foram feitas com uma biblioteca em Python chamada "Selenium".\
Selenium é uma ferramenta muito poderosa e popular no ecossistema Python, especialmente no\
campo da automação de testes e interações com navegadores web. Ela oferece uma gama de\
funcionalidades para controlar e interagir com navegadores da web de forma programática.\
O código feito utilizou o "Chromium", que é um Webdriver do navegador Chrome. No\
código acessamos o site do DATASUS e pegamos as informações de 2019 até 2023, após toda\
a coleta, foi gerado um arquivo em CSV para a leitura no Python ou SAS Viya.\

#Carga de Dados\
Após a conclusão de todos os estágios de tratamento dos dados, procedemos com a\
carga manual utilizando a ferramenta DBeaver para realizar a inserção dos dados no banco de\
dados PostgreSQL.\

# Dicionário de Dados

| Variável                                                                          | Descrição                                                                                               |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Município                                                                         | Código do município onde as ações de saúde estão sendo realizadas.                                       |
| 0101 Ações coletivas/individuais em saúde                                         | Número de ações de saúde coletivas ou individuais realizadas.                                             |
| 0201 Coleta de material                                                           | Número de procedimentos de coleta de material médico realizados.                                           |
| 0202 Diagnóstico em laboratório clínico                                           | Número de diagnósticos realizados em laboratório clínico.                                                 |
| 0203 Diagnóstico por anatomia patológica e citopatologia                          | Número de diagnósticos realizados por anatomia patológica e citopatologia.                                |
| 0204 Diagnóstico por radiologia                                                   | Número de diagnósticos realizados por radiologia.                                                          |
| 0205 Diagnóstico por ultrassonografia                                             | Número de diagnósticos realizados por ultrassonografia.                                                    |
| 0206 Diagnóstico por tomografia                                                   | Número de diagnósticos realizados por tomografia.                                                          |
| 0207 Diagnóstico por ressonância magnética                                        | Número de diagnósticos realizados por ressonância magnética.                                               |
| 0208 Diagnóstico por medicina nuclear in vivo                                     | Número de diagnósticos realizados por medicina nuclear in vivo.                                            |
| 0209 Diagnóstico por endoscopia                                                   | Número de diagnósticos realizados por endoscopia.                                                          |
| 0210 Diagnóstico por radiologia intervencionista                                   | Número de diagnósticos realizados por radiologia intervencionista.                                          |
| 0211 Métodos diagnósticos em especialidades                                       | Número de diagnósticos realizados por métodos específicos em diferentes especialidades médicas.           |
| 0212 Diagnóstico e procedimentos especiais em hemoterapia                         | Número de diagnósticos e procedimentos especiais realizados em hemoterapia.                                |
| 0214 Diagnóstico por teste rápido                                                 | Número de diagnósticos realizados por teste rápido.                                                        |
| 0301 Consultas / Atendimentos / Acompanhamentos                                    | Número de consultas, atendimentos ou acompanhamentos realizados.                                           |
| 0302 Fisioterapia                                                                 | Número de sessões de fisioterapia realizadas.                                                              |
| 0303 Tratamentos clínicos (outras especialidades)                                  | Número de tratamentos clínicos realizados em outras especialidades médicas.                                |
| 0304 Tratamento em oncologia                                                      | Número de tratamentos realizados em oncologia.                                                             |
| 0305 Tratamento em nefrologia                                                     | Número de tratamentos realizados em nefrologia.                                                            |
| 0306 Hemoterapia                                                                   | Número de procedimentos de hemoterapia realizados.                                                         |
| 0307 Tratamentos odontológicos                                                     | Número de tratamentos odontológicos realizados.                                                           |
| 0308 Tratamento de lesões, envenenamentos e outros, decorrentes de causas externas | Número de tratamentos realizados para lesões, envenenamentos e outros casos decorrentes de causas externas. |
| 0309 Terapias especializadas                                                       | Número de terapias especializadas realizadas.                                                             |
| 0310 Parto e nascimento                                                            | Número de partos e nascimentos ocorridos.                                                                 |
| 0401 Pequenas cirurgias e cirurgias de pele, tecido subcutâneo e mucosa            | Número de pequenas cirurgias e cirurgias de pele, tecido subcutâneo e mucosa realizadas.                  |
| 0402 Cirurgia de glândulas endócrinas                                              | Número de cirurgias realizadas nas glândulas endócrinas.                                                   |
| 0403 Cirurgia do sistema nervoso central e periférico                              | Número de cirurgias realizadas no sistema nervoso central e periférico.                                   |
| 0404 Cirurgia das vias aéreas superiores, da face, da cabeça e do pescoço          | Número de cirurgias realizadas nas vias aéreas superiores, face, cabeça e pescoço.                        |
| 0405 Cirurgia do aparelho da visão                                                 | Número de cirurgias realizadas no aparelho da visão.                                                       |
| 0406 Cirurgia do aparelho circulatório                                             | Número de cirurgias realizadas no aparelho circulatório.                                                   |
| 0407 Cirurgia do aparelho digestivo, orgãos anexos e parede abdominal               | Número de cirurgias realizadas no aparelho digestivo, órgãos anexos e parede abdominal.                    |
| 0408 Cirurgia do sistema osteomuscular                                             | Número de cirurgias realizadas no sistema osteomuscular.                                                   |
| 0409 Cirurgia do aparelho geniturinário                                            | Número de cirurgias realizadas no aparelho geniturinário.                                                  |
| 0410 Cirurgia de mama                                                              | Número de cirurgias realizadas na mama.                                                                    |
| 0411 Cirurgia obstétrica                                                           | Número de cirurgias obstétricas realizadas.                                                               |
| 0412 Cirurgia torácica                                                             | Número de cirurgias torácicas realizadas.                                                                 |
| 0413 Cirurgia reparadora                                                           | Número de cirurgias reparadoras realizadas.                                                                |
| 0414 Bucomaxilofacial                                                              | Número de cirurgias bucomaxilofaciais realizadas.                                                          |
| 0415 Outras cirurgias                                                              | Número de outras cirurgias realizadas.                                                                    |
| 0416 Cirurgia em oncologia                                                         | Número de cirurgias realizadas em oncologia.                                                               |
| 0418 Cirurgia em nefrologia                                                        | Número de cirurgias realizadas em nefrologia.                                                              |
| 0501 Coleta e exames para fins de doação de orgãos, tecidos e células e de transplante | Número de coletas e exames realizados para fins de doação de órgãos, tecidos e células e de transplante. |
| 0502 Avaliação de morte encefálica                                                | Número de avaliações de morte encefálica realizadas.                                                       |
| 0503 Ações relacionadas à doação de orgãos e tecidos para transplante             | Número de ações relacionadas à doação de órgãos e tecidos para transplante.                                |
| 0504 Processamento de tecidos para transplante                                     | Número de processamentos de tecidos realizados para transplante.                                           |
| 0505 Transplante de órgãos, tecidos e células                                      | Número de transplantes de órgãos, tecidos e células realizados.                                             |
| 0506 Acompanhamento e intercorrências no pré e pós-transplante                     | Número de acompanhamentos e intercorrências no pré e pós-transplante.                                       |
| 0603 Medicamentos de âmbito hospitalar e urgência                                  | Número de medicamentos de âmbito hospitalar e urgência administrados.                                       |
| 0702 Órteses, próteses e materiais especiais relacionados ao ato cirúrgico          | Número de órteses, próteses e materiais especiais relacionados ao ato cirúrgico utilizados.               |
| 0801 Ações relacionadas ao estabelecimento                                         | Número de ações relacionadas ao estabelecimento de saúde.                                                  |
| 0802 Ações relacionadas ao atendimento                                             | Número de ações relacionadas ao atendimento em saúde.                                                      |
| Total                                                                             | Total de todas as ações ou procedimentos realizados.                                                       |
| Mes                                                                               | Mês em que os dados foram coletados.                                                                      |
| Ano                                                                               | Ano em que os dados foram coletados.                                                                      |
| Conteudo                                                                          | Conteúdo associado ao mês e ano da primeira coleta de dados.                                               |
| Mes.1                                                                             | Mês em que os dados foram coletados pela segunda vez.                                                      |
| Ano.1                                                                             | Ano em que os dados foram coletados pela segunda vez.                                                      |
| Conteudo.1                                                                        | Conteúdo associado ao mês e ano da segunda coleta de dados.                                                |
