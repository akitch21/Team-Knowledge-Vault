import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"

export function SignupForm({ ...props }: React.ComponentProps<typeof Card>) {
  return (
    <Card {...props}>
      <CardHeader>
        <CardTitle>アカウント作成</CardTitle>
        <CardDescription>
          以下にあなたのアカウント情報を記入してください。
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form>
          <FieldGroup>
            <Field>
              <FieldLabel htmlFor="name">アカウント名</FieldLabel>
              <Input id="name" type="text" placeholder="John Doe" required />
            </Field>
            <Field>
              <FieldLabel htmlFor="email">Email</FieldLabel>
              <Input
                id="email"
                type="email"
                placeholder="m@example.com"
                required
              />
            </Field>
            <Field>
              <FieldLabel htmlFor="password">パスワード</FieldLabel>
              <Input id="password" type="password" required />
              <FieldDescription>
                最低8文字以上のパスワードにしてください。
              </FieldDescription>
            </Field>
            <Field>
              <FieldLabel htmlFor="confirm-password">
                再確認用パスワード
              </FieldLabel>
              <Input id="confirm-password" type="password" required />
              <FieldDescription>もう一度同じパスワードを入力してください。</FieldDescription>
            </Field>
            <FieldGroup>
              <Field>
                <Button type="submit">アカウント作成</Button>
                <Button variant="outline" type="button">
                  Googleアカウントでアカウント作成
                </Button>
                <FieldDescription className="px-6 text-center">
                  <a href="#">アカウントを持っている方はこちら</a>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </FieldGroup>
        </form>
      </CardContent>
    </Card>
  )
}
