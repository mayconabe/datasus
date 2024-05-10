from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

def navigate_to_website(driver):
    driver.get('http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/spabr.def')

def select_options(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()

def get_data():
    driver = initialize_driver()
    navigate_to_website(driver)

    select_options(driver, '/html/body/div/div/center/div/form/div[3]/div/select/option[1]')
    select_options(driver, '/html/body/div/div/center/div/form/div[4]/div[2]/div[1]/div[2]/input[3]')
    select_options(driver, '/html/body/div/div/center/div/form/div[2]/div/div[2]/select/option[8]')
    time.sleep(1)

    column_headers = 'Código Município; Município; Ações coletivas/individuais em saúde; Coleta de material; Diagnóstico em laboratório clínico; Diagnóstico por anatomia patológica e citopatologia; Diagnóstico por radiologia; Diagnóstico por ultrasonografia; Diagnóstico por tomografia; Diagnóstico por ressonância magnética; Diagnóstico por medicina nuclear in vivo; Diagnóstico por endoscopia; Diagnóstico por radiologia intervencionista; Métodos diagnósticos em especialidades; Diagnóstico e procedimentos especiais em hemoterapia; Diagnóstico por teste rápido; Consultas / Atendimentos / Acompanhamentos; Fisioterapia; Tratamentos clínicos (outras especialidades); Tratamento em oncologia; Tratamento em nefrologia; Hemoterapia; Tratamentos odontológicos; Tratamento de lesões, envenenamentos e outros, decorrentes de causas externas; Terapias especializadas; Parto e nascimento; Pequenas cirurgias e cirurgias de pele, tecido subcutâneo e mucosa; Cirurgia de glândulas endócrinas; Cirurgia do sistema nervoso central e periférico; Cirurgia das vias aéreas superiores, da face, da cabeça e do pescoço; Cirurgia do aparelho da visão; Cirurgia do aparelho circulatório; Cirurgia do aparelho digestivo, orgãos anexos e parede abdominal; Cirurgia do sistema osteomuscular; Cirurgia do aparelho geniturinário; Cirurgia de mama; Cirurgia obstétrica; Cirurgia torácica; Cirurgia reparadora; Bucomaxilofacial; Outras cirurgias; Cirurgia em oncologia; Cirurgia em nefrologia; Coleta e exames para fins de doação de orgãos, tecidos e células e de transplante; Avaliação de morte encefálica; Ações relacionadas à doação de orgãos e tecidos para transplante; Processamento de tecidos para transplante; Transplante de orgãos, tecidos e células; Acompanhamento e intercorrências no pré e pós-transplante; Medicamentos de âmbito hospitalar e urgência; Órteses, próteses e materiais especiais relacionados ao ato cirúrgico; Ações relacionadas ao estabelecimento; Ações relacionadas ao atendimento; Total; Mes; Ano; Conteudo\n'
    with open('resultado.csv', 'w') as file:
        file.write(column_headers)

    for i in range(2):
        content_option = driver.find_element(By.XPATH, f'/html/body/div/div/center/div/form/div[2]/div/div[3]/select/option[{i+1}]')

        if i != 0:
            driver.find_element(By.XPATH, f'/html/body/div/div/center/div/form/div[2]/div/div[3]/select/option[{i}]').click()
            content_option.click()
            time.sleep(1)
        
        content_text = content_option.text

        for j in range(2, 5*12+2):
            date_option = driver.find_element(By.XPATH, f'/html/body/div/div/center/div/form/div[3]/div/select/option[{j+1}]')
            date_option.click()
            date_text = date_option.text
            time.sleep(1)

            driver.find_element(By.XPATH, '/html/body/div/div/center/div/form/div[4]/div[2]/div[2]/input[1]').click()

            time.sleep(5)

            windows = driver.window_handles
            driver.switch_to.window(windows[1])

            time.sleep(1)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            data = driver.find_element(By.XPATH, '/html/body/div/div/pre').text
            data = data.replace('"', '').split('\n')
            data = data[1:-2]

            result = ''

            for row in data:
                result += row[0:6].replace('"', '') + ';' + row[7:len(row)].replace('-', '0').replace('"', '').replace(",", ".") + ';' + date_text.replace('/', ';') + ';' + content_text +'\n'

            print(len(data), date_text, content_text)

            time.sleep(3)

            with open('resultado.csv', 'a') as file:
                file.write(result)

            driver.close()
            driver.switch_to.window(windows[0])

            date_option.click()

    driver.quit()
    return 'Arquivo gerado com sucesso!'

if __name__ == '__main__':
    get_data()
