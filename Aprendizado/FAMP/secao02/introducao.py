'''
Endpoints -> Seria o caminho via URL , usamos substantivos nos nomes e não verbos
Api REST -> Temor recursos(resources) podendo sem um model da nossa aplicação

CRUD:
get -> Usado para busca de informações
put -> Atualizar um recurso ,  não usamos em URL em coleção e sim em individual
post -> Mandar dados, não usamos na URL individual e sim em coleção
delete -> Deletar dados

Request -> Requisição é quando colamos uma url no google , podendo passar informações , exemplo api/v1/produtos?order=desc&limit=10, nesse exemplo ordenaria de forma decrescente e mostraria no limite 10 produtos, sendo chamado de query string

Response -> Modo como a resposta ira vir para o usuario, tendo seus tipos de status , começando com 1 seria informacional , 2 sucesso, 3 redirecionamento , 4 client error  e 5 erro de servidor

Segurança -> Devemos limitar as requisições para o servidor não cair

Usamos tokens para autenticação , no caso uma chave publica

Metodo GET:

@app.get('/caminho') -> Usamos um decorator (@) . o metodo que no caso é get , ou seja mostrar/pegar dados e entre () o endpoint que seria o caminho da URL
asnyc def funcao_ver():
    return dicionario_com_lista

Exemplo real:
@app.get('/cursos')
async def get_cursos():
    return cursos

Tambem tem como fazer pesquisas via ID:
@app.get('/cursos/{curso_id}') -> Passamos no endpoint que o user deve colocar o id
async def get_cursos_id(curso_id:int): -> Colocamos o parametro id e sempre definimos o tipo dos parametros
    try:
        curso = cursos[curso_id] -> A variavel curso vai ser igual ao id passado no endpoint e vai pegar apenas a linha do cursos com aquele id passado
        curso.update({"id": curso_id}) -> Atualizamos para aparecer o id tambem no dic do curso
        return curso -> Retornamos o curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado") -> Tratamento de erro

Metodo POST:
No metodo POST a gente utiliza para enviar dados , mas para isso alem de ter a rota a gente tem que criar um model.py que la teria uma class onde os objetos serão oq vai ter que ser preenchido e importar do pydnatic o BaseModel e passar como argumento na sua classe e isso seria o parametro da função , exemplo:

Models.py
from pydanic import BaseModel

class Exemplo(BaseModel):
   nome: str

Arquivo.py:
@app.post("/exemplo")
asnyc def mandar_dados(exemplo: Exemplo):
   next_id = len(listas) + 1
   listas[next_id] = lista
   return lista 

Agora em um esquema real:

Models.py:
from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

Arquivo com POST:
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id:int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

Sempre importante passar os status 201 que seria a criação no decoradores de POST !!!!
'''