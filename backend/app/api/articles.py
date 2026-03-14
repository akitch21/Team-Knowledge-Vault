from fastapi import APIRouter,Depends,HTTPException,status
from typing import Any

from schemas.articles import ResponseArticle as article_schemas
from schemas.articles import CreateArticleRequest as create_article_request_schemas
from schemas.articles import UpdateArticleRequest as update_article_request_schemas

from schemas.articles import ArticleQueryParams as article_query_params_schemas

router = APIRouter(prefix="/articles",tags=["articles"])

articles = [
    {"id": 1, "author_id":1,"title": "FastAPIメモ", "content": "FastAPIの基本","status": "published", "created_at": "2024-06-01T12:00:00Z", "updated_at": "2024-06-01T12:00:00Z"},
    {"id": 2, "author_id":2,"title": "Next.jsメモ", "content": "Next.jsの基本","status": "draft", "created_at": "2024-06-02T12:00:00Z","updated_at": "2024-06-02T12:00:00Z"},
]


@router.get("/",response_model=list[article_schemas])
async def get_articles(query_params: article_query_params_schemas = Depends()) -> list[article_schemas]:
    if query_params:
        print(f"Depends:{query_params}")
        articles_filtered = [
            article for article in articles
            if (query_params.status is None or article["status"] == query_params.status)
        ]
    else:
        articles_filtered = articles
    return [article_schemas(**article) for article in articles_filtered]

@router.get("/{article_id}")
async def get_article(article_id: int) -> article_schemas:
    try:
        article = articles[article_id - 1]
        return article_schemas(**article)
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")

@router.post("/",response_model=article_schemas)
async def create_article(article: create_article_request_schemas):
    new_article = article.model_dump()
    new_article["id"] = len(articles) + 1
    articles.append(new_article)
    return article_schemas(**new_article)

@router.put("/{article_id}",response_model=article_schemas)
async def update_article(article_id: int, article: update_article_request_schemas):
    existing_article = articles[article_id - 1]
    updated_data = article.model_dump(exclude_unset=True)
    existing_article.update(updated_data)
    return article_schemas(**existing_article)

@router.delete("/{article_id}")
async def delete_article(article_id: int) -> Any:
    articles.pop(article_id - 1)
    return {"message": "Article deleted successfully"}