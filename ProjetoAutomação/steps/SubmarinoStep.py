import time

@given(u'que estou na tela home do Submarino')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given que estou na tela home do Submarino')
    context.subP.acessarSite()

@when(u'digitar "Notebook" no campo Pesquisa')
def step_impl(context):
    context.subP.sendText("h_search-input", "notebook")
    context.subP.clickButton("#h_search-btn")
    time.sleep(10)


@when(u'ser apresentado os resultados da Pesquisa')
def step_impl(context):
    pass


@then(u'Clicar na opção desejada')
def step_impl(context):
    context.subP.clickItem(2)