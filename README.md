# Explicação da implementação - Prova prática módulo 6

É possível encontrar o o codigo que detecta faces no diretório `codigo/detectaface.py`. O código faz detecção de faces usando Haar Cascade em que a detecção é feita por uma série de classificadores em cascata.

O código começa na leitura de um vídeo sem a detecção de faces, no diretório `assets/arsene.mp4`. Enquanto isso é criado uma variável/arquivo que será o vídeo com a detecção de faces, mas que, a primeiro momento, está vazio. 
Após isso é iniciado um looping lê o video frame a frame, e, nesse momento, é feita a detecção de rostos. Para isso acontecer, o frame é transformado em escalas de cinza, depois é passado o filtro de cascata que detecta faces. Por fim, a partir dessa detecção é desenhado um quadrado vermelho ao redor do rosto.

Por fim, antes do ciclo se encerrar cada frame de vídeo depois de ter passado pela detecção do Haar Cascade é gravado no arquivo criado chamado `output_{data}.mp4`.

(Existe um arquivo chamado `output_20230616161039.mp4` na raiz desse projeto que mostra um exemplo de vídeo após passar pelo código) 

Ao rodar o código, espera-se que um quadrado vermelho como na imagem abaixo seja desenhado ao redor das faces encontradas:
![image](https://github.com/emanuelemorais/prova_mod6/assets/99221221/a71f2751-fde3-4412-892f-5a680eb29e73)

