'''
API(Diretorio) -> Diretorio onde ficara armazendo um subdiretorio v1 que nele tera um arquivo chamado api.py e uma pasta chamada endpoints e no endpoints tem dois arquivos python usuario e artigo , onde tem as rotas como POST, GET ,DELETE e PUT. Entrando em detalhes:
    - api.py: Sempre chamamos o fastapi para pegar o ApiRouter e api.v1.endpoints onde a gente tem acesso aos dois arquivos py , no api.py temos que fazer a inclusão das rotas com incloude_router(artigo.router , prefix="/artigos", tags=["artigos"]) , o artigo.router seria a rota padrão dos endpoints , exemplo :@router.get, @router.post, etc. Já o prefix será o caminho que teremos que utilizar para colocar na url , exemplo: http://127.0.0.1:8000/api/v1/artigos/1 e por fim a tags servem para separar na documentação por meio de "secções"

    - artigo.py: Nesse arquivo importamos as seguintes libs: typing(para uso no get quando queremos retornar todos artigos que seram em formato de lista): List , fastapi (ApiRouter: Seria para usar nos endpoints @, status: passar os status de requisição , httpexception: para erro juntamento com status informar o usuario, depends: utilizado para dependencias dos endpoints com o banco de dados) , sqlalchemy.ext.asyncio (AsyncSession: sessão assincrona , utilizada para passar qual tipo do banco de dados) , sqlalchemy.future(select: usado para consultas em querys internas dentro de um async with db as session), models.artigo_model (ArtigoModel: Para trazer o modelo do banco de dados com os atributos para a utilização em parametros como post , put), schemas.artigo_schema(Validar dados de entrada e formatar dados de saída (JSON).), core.deps (get_session , get_current_user: Usado para pegar o usuario atual que esta acessando/querendo acessar um endpoint). Os endpoints criados foram: @router.post("/") -> Utilizado para criar uma novo artigo ,@router.get("/") -> Utilizamos para retornar todos artigos usando o List[ArtigoSchema], @router.get("/{artigo_id}") -> Pesquisa unica onde verifica se o id existe e se existir retorna , @router.put("/{artigo_id}")-> Verifica se o id existe e faz a devida atualização,@router.delete("/{artigo_id}")-> Verifica se o id existe e faz o devido deletamento

    - usuario.py: Segue o mesmo molde do artigo entao não irei entrar em detalhes
    
    - Importante:
        - Sempre passar o status_code e response_model(menos no delete)
        - Sempre fazer o await db.commit() e await db.refresh() (menos no get pois é so visualização e refresh no delete nao é necessario pois não retorna nada)
        - Sempre especificar o tipo dos parametros com :

CORE -> Utilizado para funcionalidades essenciais e configurações internas da aplicação. Sua principal função é isolar a lógica fundamental que é compartilhada por toda a API, garantindo modularidade, organização e escalabilidade, especialmente em projetos maiores.

configs.py:
    Utilizamos para passar uma classe herdando uma BaseSetting e la passamos o caminho basico da url de endpoints , banco de dados , declaramos a sua base , senha secreta , entre outras coisas

database.py:
    criamos uma engine assincrona passando a url da configs e logo abaixo criamos uma Session que vai ser = a um sessionmaker com as configurações necessarias

deps.py:
    Dependencias

MODELS: Modelagem dos dados no banco de dados como criação de tabelas , colunas , etc

SCHEMAS: São utilizado para validar os dados que entram e saem em JSON
'''