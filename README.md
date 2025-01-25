# Verificador de Parentesco

Este projeto é um algoritmo simples escrito em Python que utiliza a estrutura de dados **pilha** para verificar se um nome fornecido pelo usuário está relacionado a uma lista de nomes pré-definida, considerada como "membros da família" da pessoa que utilizou o seguro de modo fraudulento ou não.

O objetivo principal do programa é identificar se um nome digitado é parente de um nome de referência, neste caso, **Miguel Silva de Castro**. Se alguém de sua família o ajudou na fraude ou não. 

---

## Estrutura do Código

### Classe `Pilha`

A classe `Pilha` é a implementação de uma estrutura de dados do tipo **pilha (stack)**. Essa estrutura segue o princípio **LIFO** (Last In, First Out), onde o último item adicionado é o primeiro a ser removido.

#### Métodos da classe:

1. **`__init__(self)`**  
   - Inicializa a pilha como uma lista vazia.  
   - **Exemplo:**  
     ```python
     pilha = Pilha()
     ```

2. **`__repr__(self)`**  
   - Retorna a representação da pilha como uma string. Isso é útil para depuração e exibição do estado atual da pilha.  
   - **Exemplo:**  
     ```python
     print(pilha)  # Exibe a pilha como lista
     ```

3. **`empilha(self, valor)`**  
   - Adiciona um elemento ao topo da pilha.  
   - **Parâmetros:**  
     - `valor`: O valor a ser adicionado.  
   - **Exemplo:**  
     ```python
     pilha.empilha("José de Castro")
     ```

4. **`desempilha(self)`**  
   - Remove e retorna o elemento no topo da pilha.  
   - Gera um erro se a pilha estiver vazia.  
   - **Exemplo:**  
     ```python
     topo = pilha.desempilha()
     ```

5. **`busca(self, alvo)`**  
   - Verifica se um determinado valor está presente na pilha.  
   - **Parâmetros:**  
     - `alvo`: O valor a ser procurado na pilha.  
   - **Retorna:**  
     - `True` se o valor for encontrado, caso contrário, `False`.  
   - **Exemplo:**  
     ```python
     encontrado = pilha.busca("Eugênio de Castro")
     ```

---

### Função `main()`

A função principal do programa realiza as seguintes operações:

1. **Criação da pilha:**  
   - Um objeto da classe `Pilha` chamado `familia` é criado para armazenar os nomes dos parentes.  

2. **Adição de nomes à pilha:**  
   - Os seguintes nomes são adicionados à pilha como exemplo:  
     - "Miguel Silva de Castro"  
     - "José de Castro"  
     - "Eugênio de Castro"  
     - "Pedro Paulo de Castro"  

3. **Entrada do usuário:**  
   - Solicita que o usuário digite um nome.  

4. **Verificação de parentesco:**  
   - Utiliza o método `busca` da classe `Pilha` para verificar se o nome digitado pelo usuário é encontrado na pilha.  
   - O nome de referência é **"Miguel Silva de Castro"**.  

5. **Exibição do resultado:**  
   - Se o nome estiver na pilha, exibe:  
     `"Fulano é parente de Miguel Silva de Castro!"`  
   - Caso contrário, exibe:  
     `"Fulano não é parente de Miguel Silva de Castro!"`

---

## Como Utilizar

1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Baixe ou copie o código e salve-o em um arquivo chamado, por exemplo, `verificador_parentesco.py`.
3. Execute o script em seu terminal ou editor de preferência:  
   ```bash
   python verificador_parentesco.py
   ```
4. Digite o nome que deseja verificar quando solicitado.  

---

## Exemplo de Execução

### Cenário 1: Nome presente na pilha
**Entrada do usuário:**  
```
Digite o seu nome: José de Castro
```
**Saída do programa:**  
```
José de Castro é parente de Miguel Silva de Castro!
```

### Cenário 2: Nome ausente na pilha
**Entrada do usuário:**  
```
Digite o seu nome: Ana Maria
```
**Saída do programa:**  
```
Ana Maria não é parente de Miguel Silva de Castro!
```

---

## Personalização

Você pode adicionar mais nomes à pilha para ampliar a lista de parentes utilizando o método `empilha`.  
**Exemplo:**
```python
familia.empilha("Ana Beatriz de Castro")
```

---

## Conclusão

Este programa é um exemplo simples, mas funcional, de como usar a estrutura de dados **pilha** para resolver problemas do mundo real, como verificação de parentesco. Ele pode ser facilmente adaptado ou expandido para incluir mais funcionalidades, como adicionar nomes dinamicamente ou armazenar os dados em um banco de dados.
