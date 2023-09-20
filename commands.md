# commands

```typescript
commands.registerCommand('extension.sayHello', () => {
  window.showInformationMessage('Hello World!');
});
```

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
