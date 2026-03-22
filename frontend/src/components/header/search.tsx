import React from 'react'
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default function Search() {
    return (
        <div className='flex'>
            <Input placeholder="Enter text" />
            <Button type="submit">検索</Button>
        </div>
    )
}
