# Forest Fire Controlled Model

## Resumo

Nesta versão da simulação de incêndios na floresta, são combinados dois métodos de controle para observar o quanto conseguem conservar da área verde original de acordo com as condições do evento. Os dois procedimentos são: A  probabilidade de foco de incêndio ser controlado por bombeiros e apagado antes de se espalhar para a próxima árvore e pela queima intencional de pontos para criar obstáculos ao avanço do fogo.

A propriedade "probability of extinguishment" pode ser alterada por meio da interface, ela altera o valor da variável "ext_prob" no arquigo agent.py. Assim para que o fogo passe para a próxima árvore, o valor padrão é de 50%.

Já a propriedade "burned density", também alterada na interface diz respeito à densidade de árvores que já estarão queimadas no início da simulação. São criados clusters de árvores já queimadas que servem como obstáculos à ploriferação do fogo. Para evitar que grandes clusteres sejam queimados, os valores selecionados devem ser pequenos, uma vez que, para valores muito altos, grande parte da área verde é perdida. No _init_ do models.py, após todas árvores serem instanciadas, os clusteres são criados.

O indíce de sucesso é calculado no modelo na função saved_tress, que retorna a porcentagem das árvores saudáveis em relação às árvores queimadas. Este é salvo nos dados coletados do modelo, juntamente com a "burning density" e extinguish probability" escolhida. Estes dois últimos também estão salvos nos dados coletados do agente, agrupados com o estado de cada árvore. 

Obs: Para evitar conflitos de nomeação no windows, os arquivos seguem o padrão:  _burn_dens_1_ para burning density de 0,1% e _burn_dens_200 para 20%, assim como ext_prob_50 para 50% e _ext_prob_100 para 100%.

## Como usar

Para carregar o modelo com uma interface interativa, use ``mesa runserver`` neste diretório. e.g.

```
    $ mesa runserver
```

Abra o navegador de preferência no link [http://127.0.0.1:8521/](http://127.0.0.1:8521/) pressione Reset, e então Run.

start.spring.io 14/09
     -Maven project /Java /2.7.3
     -br.com.bb.letscode.nome
     -Dependencias:Spring mvc, lombok
      -Criar get 1:06:00, 1:11:00, 1:15:00,
     -1:21:00 Application properties
      -Internamente usa log4j
      -1:27:00 sl4j
      -1:31:00 nível de log 1:33-:00
      -1:54:00 exportar log
      -Entidades criadas normalmente
      -Excluir equals infinito 2:12:00
      -POST 2:26:00
     -RequestMapping 2:29:00
      -Get parametrizado 2:34:02
      -GetAll 2:37:00

16/09
     -22:00 parametros n obrigatorios
     -27:00 banco de dados 30:00 e31:00 properties
     -37:00 Entidade banco de daos. 40:00 relacionamento
     -43:00 coniguração
     -53 Repositoruy
     -1:00:00 inheção auo wired
     -1:03:00 Gerated value gerar id
     -1:08:00 OnetoOne 
     -1:20:00 tabela  column nome diferente
     -1:24:00 enumerated
     -1:25:00 flyway
     -1:34:00 injeção por cosntrutor.
      -2:03:00 Validation 
    -2:07:00 @Pattern regex 2:10:00 Vailidar
       -2:16:00 validação de erro
        - 2:21:00 personalizar mensagem de null
       -2:24:00 tamanho minimo e maximo;
      -2:31:: Service interfaces e 33 notação.
      -2:36 conexxões
       -2:43 mais de um service parecido
       -2:53 mudanças no servie

