import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
filename = 'rforest.sav'
rforest = pickle.load(open(filename, 'rb'))

X = pd.DataFrame({'Financiamento': 0, 'Age': 0, 'Children': 0, 'YearsEmpl' : 0, 'Income': 0, 'source_MGM':0,
                  'source_adw': 0, 'source_dr': 0, 'source_i9': 0, 'source_org': 0, 'source_outros': 0,
                  'source_recomendacao':0, 'source_ree':0, 'source_suporte':0,
                  'Operação_Aquisição de novo imóvel com Crédito Habitação':0,
                  'Operação_ac':0, 'Operação_hpp':0, 'Operação_hps':0, 'Operação_mo':0,
                  'Operação_obras':0, 'Operação_outro':0, 'Operação_terreno':0,
                  'Operação_transferencia':0, 'Gender_0':0, 'Gender_feminino':0,
                  'Gender_masculino':0, 'CivilStatus_0':0, 'CivilStatus_Separado':0,
                  'CivilStatus_casado-comunhao-adquiridos':0,
                  'CivilStatus_casado-comunhao-geral':0, 'CivilStatus_divorciado':0,
                  'CivilStatus_solteiro':0, 'CivilStatus_uniao-facto':0, 'CivilStatus_viuvo':0,
                  'JobType_0':0, 'JobType_Contra de Outrem':0, 'JobType_Reformado':0,
                  'JobType_desempregado':0, 'JobType_empresario':0, 'JobType_liberal':0,
                  'JobType_outro':0, 'JobType_recibos-verdes':0, 'JobType_vive-rendimentos':0,
                  'JobSector_0':0, 'JobSector_privado':0, 'JobSector_publico':0},index=[0])

st.title('Previsão de Aprovação de Crédito Habitação')

#INPUT PART

financiamento = st.number_input('Valor a financiar:')
X["Financiamento"] = financiamento

age = st.number_input('Idade:', min_value=0, max_value=100, value= 0, step=1)
X["Age"] = age

filhos = st.number_input('Número de filhos:', min_value=0, max_value=100, value= 0, step=1)
X["Children"] = filhos

anos_empregado = st.number_input('Anos no corrente trabalho:', min_value=0, max_value=100, value= 0, step=1)
X['YearsEmpl'] = anos_empregado

salario = st.number_input('Salário Bruto:')
X["Income"] = salario

#start source options
source = st.selectbox(
    'Source do Paciente:',
    ('Google Ads', 'Facebook Ads', 'Orgânico', 'Suporte', 'Recomendação', 'MGM','DR',
     'REE','Outros'))

if source == 'Google Ads':
    X['source_adw'] = 1
elif source == 'Facebook Ads':
    X['source_i9'] = 1
elif source == 'Orgânico':
    X['source_org'] = 1
elif source == 'Suporte':
    X['source_suporte'] = 1
elif source == 'Recomendação':
    X['source_recomendacao'] = 1
elif source == 'MGM':
    X['source_MGM'] = 1
elif source == 'DR':
    X['source_dr'] = 1
elif source == 'REE':
    X['source_ree'] = 1
elif source == 'Outros':
    X['source_outros'] = 1
# end of source options

#start of operation options:
operation = st.selectbox(
    'Tipo de Operação:',
    ('Aquisição de novo imóvel',
     'Auto-Construção','Principal Habitação', 'Habitação Secundária', 'MO',
     'Obras','Compra de Terreno', 'Transferência','Outros'))

if operation == 'Aquisição de novo imóvel':
    X['Operação_Aquisição de novo imóvel com Crédito Habitação'] = 1
elif operation == 'Auto-Construção':
    X['Operação_ac'] = 1
elif operation == 'Primeira Habitação':
    X['Operação_hpp'] = 1
elif operation == 'Habitação Secundária':
    X['Operação_hps'] = 1
elif operation == 'MO':
    X['Operação_mo'] = 1
elif operation == 'Obras':
    X['Operação_obras'] = 1
elif operation == 'Compra de Terreno':
    X['Operação_terreno'] = 1
elif operation == 'Transferência':
    X['Operação_transferencia'] = 1
elif operation == 'Outros':
    X['Operação_outro'] = 1
# end of operation options

# start of Gender Options:
gender = st.selectbox(
    'Sexo:',
    ('N/R','Masculino','Feminino'))
if gender == 'Masculino':
    X['Gender_masculino'] = 1
elif gender == 'Feminino':
    X['Gender_feminino'] = 1
# end of Gender Options

#start of Civil Status options:
civil = st.selectbox(
    'Estado Civil:',
    ('N/R','Separado/a',
     'Casado/a - Comunhão de adquiridos',
     'Casado/a - Comunhão geral', 'Divorciado/a',
     'Solteiro/a', 'União de Facto', 'Viúvo/a'))
if civil == 'Separado/a':
    X['CivilStatus_Separado'] = 1
elif civil == 'Casado/a - Comunhão de adquiridos':
    X['CivilStatus_casado-comunhao-adquiridos'] = 1
elif civil == 'Casado/a - Comunhão geral':
    X['CivilStatus_casado-comunhao-geral'] = 1
elif civil == 'Divorciado/a':
    X['CivilStatus_divorciado'] = 1
elif civil == 'Solteiro/a':
    X['CivilStatus_solteiro'] = 1
elif civil == 'União de Facto':
    X['CivilStatus_uniao-facto'] = 1
elif civil == 'Viúvo/a':
    X['CivilStatus_viuvo'] = 1
#end of Civil Status option

#Job Type Start
trabalho = st.selectbox(
    'Tipo de trabalho:',
    ('N/R','Conta de Outrem','Reformado/a', 'Desempregado/a', 'Empresário/a', 'Profissional Liberal',
     'Recibos Verdes', 'Vive dos Rendimentos', 'Outros'))
if trabalho == 'Conta de Outrem':
    X['JobType_Contra de Outrem'] = 1
elif trabalho == 'Reformado/a':
    X['JobType_Reformado'] = 1
elif trabalho == 'Desempregado/a':
    X['JobType_desempregado'] = 1
elif trabalho == 'Empresário/a':
    X['JobType_empresario'] = 1
elif trabalho == 'Profissional Liberal':
    X['JobType_liberal'] = 1
elif trabalho == 'Recibos Verdes':
    X['JobType_recibos-verdes'] = 1
elif trabalho == 'Vive dos Rendimentos':
    X['JobType_vive-rendimentos'] = 1
elif trabalho == 'Outro':
    X['JobType_outro'] = 1
#Job Type End

#Sector start
sector = st.selectbox(
    'Sector',
    ('N/R','Público','Privado'))
if sector == 'Público':
    X['JobSector_publico'] = 1
elif sector == 'Privado':
    X['JobSector_privado'] = 1
#Sector end

#PREDICTION PART

if st.button('Previsão'):
    predict_proba = pd.DataFrame(rforest.predict_proba(X))
    X["predict"]  = rforest.predict(X)
    X["predict_text"] = X["predict"].apply(lambda x: "ser aprovado." if x == 1 else "não ser aprovado.")
    if predict_proba[1][0] == 0:
        st.write('O pedido de financiamento tem 0.1 % de probabilidade de ser aprovado.')
    elif predict_proba[1][0] == 1:
        st.write('O pedido de financiamento tem 99.9 % de probabilidade de ser aprovado.')
    else:
        st.write('O pedido de financiamento tem', round((predict_proba[1][0]) * 100), '% de probabilidade de ser aprovado.')
