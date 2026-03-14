# 記事のAPIエンドポイントのテストコード
def test_get_articles(client):
    response = client.get("/articles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 記事の異常系のテストコード
def test_get_article_not_found(client):
    response = client.get("/articles/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Article not found"}
