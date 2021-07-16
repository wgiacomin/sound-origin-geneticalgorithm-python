# Rastreando a origem de um sinal sonoro 

Um sistema para rastreamento de origem de sinais sonoros (SRSS) dispõe de três torres com sensores sonoros instalados nas seguintes respectivas coordenadas em um sistema de referência, previamente estabelecido em metros: 

​	a) Sensor 1 (0, 0, 0);

​	b) Sensor 2 (2300, 1100, 20);

​	c) Sensor 3 (-170, 915, 11); 

O SRSS também conta com algoritmo para a identificação de sinais de interesse, que registra os tempos em que um mesmo sinal chegou a cada um dos sensores, (t1, t2 , t 3), em cronômetros sincronizados. Considerando a velocidade do som como 340 m/s: 

construir uma solução, em um algoritmo genético (AG), para facilitar a identificação da origem de  um  estampido  no  sistema  de  referência  utilizado,  a  partir  dos  tempos  observados  nos sensores. 



## Função Objetivo

A função objetivo foi determinada utilizando-se como base a distância euclidiana sendo alimentada por um ponto Tx contendo 3 coordenadas do espaço, conforme a imagem abaixo.

![img](https://github.com/wgiacomin/geneticalgorithm-python/blob/main/images/image%20(1).png)

Após calculada a distância entre o ponto alimentado e as três torres, a distância dada em metros é convertida em tempo na unidade de milissegundos. A partir desse dado, é então calculado o custo da função com base em um ponto relativo. Por exemplo, na imagem abaixo, o custo da função é o tempo relativo entre T0 e Tx usando-se como base o ponto T2. Assim tempo que o custo é a diferença entre os tempos calculados dos dois pontos menos a diferença dos tempos informados entre os dois pontos.

![img](https://github.com/wgiacomin/geneticalgorithm-python/blob/main/images/image%20(2).png)

Esse raciocínio é generalizado para os demais pontos e então penalizado para se promover uma curva mais acentuada e melhorar a conversão de pontos mais distantes. Em notações matemáticas, a distância entre 2 pontos se dará como:

![img](https://github.com/wgiacomin/geneticalgorithm-python/blob/main/images/image%20(3).png)

o cálculo da função do desvio é então dado como:

![img](https://github.com/wgiacomin/geneticalgorithm-python/blob/main/images/image%20(4).png)

sendo,

​     k, o tempo informado

​     t, o tempo calculado

​     x, o ponto informado como argumento na função

​     T, uma coordenada de 3 dimensões

Em poucas palavras, as diferenças entre o tempo informado e o tempo calculado deve ser zero para todos os pontos.
