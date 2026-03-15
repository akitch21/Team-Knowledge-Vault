import React from 'react'

async function getArticles() {
  const res = await fetch("http://localhost:8000/articles")
  return res.json()
}

export default async function Page() {

  //仮データ
    const articles = await getArticles();

  return (
    <div>
      <h1>記事一覧</h1>
      <ul>
        {articles.map(a => (
          <li key={a.id}>{a.title}</li>
        ))}
      </ul>
    </div>
  )
}
