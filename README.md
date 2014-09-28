Optimal HRSS
============
Solução ótima para o problema do `Hybrid Reentrant Shop Scheduling` desenvolvida em Python.

## Requisitos ##
* Python 2.7+

### Requisitos de testes ###
Para executar a suíte de testes faz-se necessário os seguintes requisitos:
* Nose
* covereage.py

## Modo de uso ##
Utilize o comando abaixo para executar o programa:

```
$ bin/optimalhrss instance_file.txt
```

Em caso de dúvidas, utilize o argumento `-h` para exibir informações de ajuda.

```
$ bin/optimalhrss -h
usage: optimalhrss [-h] file

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
```

## Executando a suíte de testes ##
Para executar a suíte de testes utilize o script `runtests.sh` como mostrado abaixo:

```
$ ./runtests.sh
```

## Descrevendo instâncias ##
As instâncias do problema são descritas em formato de texto puro, em inglês, e seguem um padrão bem definido de estrutura e organização.

Atualmente, apenas valores inteiros para tempos de `inicialização`, `configuração` e `processamento` são suportados.

```
Number of jobs: 10  Number of machines: 2

Initialization time: 1

Setup times: 7  7  10  12  14  33  23  29  7  20  

Processing times: 196  137  185  131  183  151  182  160  156  151
```

É possível descrever inúmeras instâncias em um único arquivo e realizar o processamento sobre todas elas, em batch, de maneira automática.
