
# SEARCH A CATALOG
  

Um simples projeto para uma busca em um catálogo de produtos.

O único pré-requisito para executar o programa é um ambiente de execução Python3.

```bash
python3 search.py
```

## Write-up

Um ponto importante a ser mencionado é a interpretação do enunciado do desafio.

Se este programa precisasse ser executado em ambiente de produção, com um grande volume de acessos e uma necessidade de performance e segurança, várias decisões diferentes seriam tomadas. Mas, não sendo este o caso, o tamanho da lista original e a situação na qual o programa será executado foram levados em consideração.

Considerando que o objetivo principal é uma busca em uma lista, algoritmos brute-force como busca linear e busca binária inevitavelmente vêm à mente. Porém ao buscar pelos itens de uma lista de tamanho M em outra lista de tamanho N, as buscas linear e binária têm execução O(n.m) e O(n+m), respectivamente.
Outra alternativa é usar um banco de dados (relacional ou chave-valor). No entanto, num desafio que consiste justamente em uma busca, entregar todo o "trabalho pesado" de indexação e buscas/queries a um DBMS não parece o caminho certo a seguir.

Hashtables sempre são uma opção. Porém, num catálogo que já tem seus IDs únicos, passar todos os itens por uma hash function seria um passo desnecessário.

Então a solução que encontrei foi utilizar uma estrutura "dicionário" do próprio Python. Utilizando o ID de cada produto como chave, e outro dicionário representando o produto como valor.

```python
produto = {
    'id': {
        'id':'int',
        'name':'str',
        'price':'float'
    }
}
```

Desta forma posso buscar o produto diretamente pelo ID sem iterar a lista inteira.

Tendo o catálogo em memória e "indexado" com os IDs, basta pegar cada item selecionado no input, ordenar a lista por preço e retirar os itens que não cabem no orçamento passado.

Respondendo às perguntas propostas no PDF do desafio:

1. Qual a complexidade da solução proposta? Justifique.

Tanto a preparação da estrutura (executada apenas no início do programa) quanto a execução da busca em si têm complexidade de tempo e de espaço como O(n), sendo n o tamanho de seus respectivos arrays (catálogo, e a lista de compras).

2. Qual estrutura de dados você escolheu e por que?

Escolhi uma estrutura "dicionário" justamente por ser uma estrutura que permite uma boa performance sem adicionar complexidade desnecessária ao projeto.o


