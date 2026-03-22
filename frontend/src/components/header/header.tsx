import React from "react"
import { Button } from "@/components/ui/button"
import Search from "./search"
import Title from "./title"

export default function Header() {
  return (
    <div className="grid grid-cols-[1fr_auto_1fr] items-center gap-4 border-b p-3">
      <div />
      <div className="justify-self-center text-center">
        <Title>ナレッジ管理アプリ</Title>
      </div>
      <div className="flex items-center justify-self-end gap-3">
        <Search />
        <Button type="submit">新規投稿</Button>
      </div>
    </div>
  )
}
