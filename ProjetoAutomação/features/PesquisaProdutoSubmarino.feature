Feature: Pesquisa de um produto no site Submarino
    Scenario: Pesquisar um notebook
        Given que estou na tela home do Submarino
        When digitar "Notebook" no campo Pesquisa
        And ser apresentado os resultados da Pesquisa
        Then Clicar na opção desejada
  