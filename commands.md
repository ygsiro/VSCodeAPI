# commands

コマンドを処理するための名前空間。
コマンドは一意の識別子をもつ関数です。
この関数はコマンドハンドラーと呼ばれることもあります。

[registerCommand](#registercommand)関数と[registerTextEditorCommand](#registertexteditorcommand)関数を使用してコマンドをエディタに追加できます。

コマンドは手動で実行することもUIジェスチャーから実行することもできます。

+ コマンドパレットに表示するには`package.json`の`commands`セクションに記載します。
+ 拡張機能のキーバインドを有効にするには`package.json`の`keybindings`セクションに記載します。

他の拡張機能やエディタ自体からのコマンドは、拡張機能からアクセスできます。
ただし、エディターコマンドを呼び出す場合、全ての引数の型がサポートされるわけではありません。

## サンプル

コマンドハンドラーを登録し、そのコマンドのエントリをコマンドパレットに追加するサンプルです。
まずは`extension.sayHello`という識別子でコマンドハンドラーを登録します。

```typescript
commands.registerCommand('extension.sayHello', () => {
  window.showInformationMessage('Hello World!');
});
```

次に`package.json`の`commands`セクションに識別子とパレットに表示されるタイトルを記載します。

```json
{
  "contributes": {
    "commands": [
      {
        "command": "extension.sayHello",
        "title": "Hello World"
      }
    ]
  }
}
```

## Functions

### executeCommand

```typescript
executeCommand<T>(command: string, ...rest: any[]): Thenable<T>
```

### getCommands

```typescript
getCommands(filterInternal?: boolean): Thenable<string[]>
```

### registerCommand

```typescript
registerCommand(command: string, callback: (args: any[]) => any, thisArg?: any): Disposable
```

### registerTextEditorCommand

```typescript
registerTextEditorCommand(command: string, callback: (textEditor: TextEditor, edit: TextEditorEdit, args: any[]) => void, thisArg?: any): Disposable
```

[TextEditorEdit]: TextEditorEdit.md
[window]: window.md
[Disposable]: Disposable.md
[TextEditor]: TextEditor.md
