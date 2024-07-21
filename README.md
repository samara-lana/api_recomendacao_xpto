# Documentação da api de recomendação de produtos da Xpto

## Justificativa
Como não se tem informações dos usuários que vão receber as recomendações, a escolha dos produtos recomendados é feita selecionando os cinco produtos com o maior número absoluto de vendas.

## Instruções de uso da API via endpoints

> GET /:user_id/recommended

Saída esperada:
```json
{
    "products": [1, 2, 3, 4, 5] // 5 ids de produtos
}
```

### Exemplo de uso: 

Para recomendar os produtos para o usuário com o id = 2704635, utilize o url:
*locahost:5000/2704635/recommended*

**Erro comum:** 
404 Not Found - o usuário não é válido.

## Limitações atuais da solução e possíveis evoluções

Uma limitação dessa api é não conhecer o perfil dos usuários e por isso não ter uma relação do novo usuário com os usuários antigos. Uma vez que tenha-se informações dos usuários será possível recomendar o produto para o novo usuário de acordo com características do seu perfil, como: renda, gênero, localização, idade, quem o indicou, etc. que se assemelham com de usuários antigos.

Além disso, uma forma de melhorar esta solução é verificar se os novos usuários compraram um dos produtos recomendados e utilizar esses dados para aperfeiçoar o algoritmo de recomendação.