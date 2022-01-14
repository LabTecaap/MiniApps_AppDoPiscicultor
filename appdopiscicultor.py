import streamlit as st

# criar um título
st.title('App do Piscicultor')

# input botão radial
especie = st.radio('Selecione sua espécie',['Tambatinga'])
st.write('A espécie selecionada foi:', especie)
peixes_mortos=st.number_input('Número de peixes mortos no viveiro:')
import streamlit as st
peso_medio=st.number_input('Peso médio dos peixes no viveiro(gramas):')
meu_numero=st.number_input('Digite a quantidade  de peixes no viveiro (N° peixes) :')

if peso_medio >= 1 and peso_medio <=5:
  ta=15/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.success('Biomassa é:', db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 6 alimentações)')
  divisao=racao/6
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  
elif peso_medio >= 5 and peso_medio <=15:
  ta=9/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg  (dividida em 5 frequências alimentares )')
  divisao=racao/5
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)

elif peso_medio >=15 and peso_medio<=25:
  meu_numero=st.number_input('Digite a quantidade de peixes-->')
  peixes_mortos=st.number_input('Número de peixes mortos')
  ta=7/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 4 frequências alimentares) ')
  divisao=racao/4
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  

elif peso_medio >=25 and peso_medio <=45:
  ta=5.5/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomamssa do viveiro',db, 'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total é:',round(racao),
           'kg  por dia no viveiro dividida em 4 vezes')
  divisao=racao/4
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  

elif peso_medio >=45 and peso_medio <=75:
  
  ta=4.5/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 4 frequências alimentares)')
  divisao=racao/4
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  

elif peso_medio >=75 and peso_medio <=175:
 
  ta=4/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 3 vezes)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)

elif peso_medio >=175 and peso_medio <=300:
 
  ta=3.3/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg  (dividida em 3 frequências alimentares)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  

elif peso_medio >=300 and peso_medio <=500:
  
  ta=2.7/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 3 vezes)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  

elif peso_medio >=500 and peso_medio <=700:
 
  ta=2.3/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 3 Frequências alimentares)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  
 
elif peso_medio >=700 and peso_medio <=900:
  
  ta=1.7/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('Biomassa do viveiro', db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 3 frequências alimentares)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')

  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
  
  
elif peso_medio >=900 and peso_medio <=1200:
 
  ta=1.3/100
  biomassa_viveiro=(meu_numero-peixes_mortos)*peso_medio
  db=biomassa_viveiro/1000
  st.write('A biomassa é:',db,'kg')
  quantidade_racao=biomassa_viveiro*ta
  racao=quantidade_racao/1000
  st.write('A quantidade de ração total a ser ofertada ao dia é:',round(racao),
           'kg (dividida em 3 frequências)')
  divisao=racao/3
  st.write('Adicione',round(divisao),' kg por cada oferta de ração no viveiro')
  
  from PIL import Image
  img = Image.open('arracoamento.jpg')
  st.image(img)
