# Formulario
Esse formulário é a versão automatizada do Formulário 2 da disciplina de Ondas Eletromagnética do Walter Carpes.

## Como usar
Para usar essas formulas basta colocar na mesma pasta que você for rodar o seu python e escrever ```import formulario```. Assim você pode usar qualquer uma delas. A sintaxe fica "formulario.y(R, L, G, C, w)", para a constante de atenuação, por exemplo.
Para facilitar, sugiro escrever ```import formulario as f```. Assim você pode usar "f.y(R, L, G, C, w)", em vez da versão cumprida lá de cima.

Lembrando que qualquer dúvida em alguma função, ou caso queira consultar todas as funções do formulário em si, basta usar o doc. Por exemplo:
```
import formulario as f

print(f.__doc__)     #Exibe a documentação da biblioteca, com todas as fórmulas/funções disponíveis
print(f.Zin.__doc__) #Exibe a documentação da função Zin, com a descrição da função, suas variáveis e o que retorna
```
Obs: o formato para números complexos é "a + bj", sendo 'a' e 'b' números reais. Note que necessariamente deve haver um número multiplicando o 'j'. Para mais informações sobre  biblioteta de números complexos, acesse esse [link](https://docs.python.org/3.6/library/cmath.html).
